import json
import boto3
import urllib.parse

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Extract source bucket and uploaded file key from S3 event payload
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        output_bucket = source_bucket.replace('raw-input', 'clean-output')

        # Read JSON file from raw S3 bucket
        response = s3_client.get_object(Bucket=source_bucket, Key=key)
        raw_content = response['Body'].read().decode('utf-8')
        data = json.loads(raw_content)

        # Sanitize and structure the product payload
        clean_payload = {
            "item_id": data.get("id", "UNKNOWN"),
            "product_title": str(data.get("title", "")).strip().title(),
            "price_usd": round(float(data.get("price", 0.0)), 2),
            "status": "PROCESSED",
            "tags": [tag.lower() for tag in data.get("tags", [])]
        }

        # Save processed JSON to destination S3 bucket
        output_key = f"clean_{key}"
        s3_client.put_object(
            Bucket=output_bucket,
            Key=output_key,
            Body=json.dumps(clean_payload, indent=2),
            ContentType='application/json'
        )

        print(f"Successfully processed {key} -> {output_bucket}/{output_key}")
        return {"statusCode": 200, "body": json.dumps("Payload Processed")}

    except Exception as e:
        print(f"Processing Error: {str(e)}")
        raise e
