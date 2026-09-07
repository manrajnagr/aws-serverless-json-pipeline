# AWS Serverless Event-Driven JSON Pipeline

An asynchronous, cloud-native data processing pipeline built on AWS.

## Architecture
1. **Ingestion:** Raw JSON files uploaded to `autolister-raw-input`.
2. **Event Trigger:** S3 `ObjectCreated` event invokes an AWS Lambda function.
3. **Processing:** Python 3.14 function parses, sanitizes, and formats product metadata.
4. **Storage:** Processed JSON is written to `autolister-clean-output`.
5. **Security:** Restricted execution via AWS IAM Roles.

## Tech Stack
- **Cloud Provider:** AWS (S3, Lambda, IAM)
- **Runtime:** Python 3.14 (`boto3`, `urllib.parse`, `json`)
