# AWS Serverless Event-Driven JSON Pipeline

An asynchronous, cloud-native data processing pipeline built on AWS to automatically ingest, sanitize, and transform raw e-commerce payloads.

## System Architecture
1. **Ingestion:** Raw JSON objects are uploaded to the source S3 bucket (`autolister-raw-input`).
2. **Event Trigger:** S3 `ObjectCreated` event automatically invokes an AWS Lambda function.
3. **Compute & Processing:** Python 3.14 Lambda function parses incoming bytes, normalizes string formatting, cleans numerical types, and transforms tags.
4. **Output Storage:** Processed JSON payload is saved directly to the destination S3 bucket (`autolister-clean-output`).
5. **Security:** Least-privilege IAM Execution Role (`LambdaS3PipelineRole`) grants granular access between S3 and Lambda.

## Tech Stack
- **Cloud Provider:** Amazon Web Services (AWS)
- **Services:** AWS Lambda, Amazon S3, AWS IAM
- **Language/SDK:** Python 3.14, `boto3`
