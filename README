# PyWa AWS Lambda (Serverless Infrastructure)

This project demonstrates how to use the [PyWa](https://pywa.readthedocs.io/en/latest/) module to interact with the WhatsApp Cloud API in a serverless environment using AWS Lambda and Docker.

## Prerequisites

- AWS account
- Docker installed locally
- AWS CLI configured
- Python 3.9 or later installed

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ArielS1/pywa-aws-lambda.git
cd pywa-aws-lambda
```

### 2. Create AWS ECR Repository

```bash
aws ecr create-repository --repository-name pywa-aws-lambda
```

### 3. Build and Push Docker Image

I followed [this guide](https://blog.searce.com/fastapi-container-app-deployment-using-aws-lambda-and-api-gateway-6721904531d0) but made some adjustments to overcome specific issues. Here’s the modified process:

```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-ecr-url>.amazonaws.com
docker build --provenance=false --platform linux/arm64 -t pywa-aws-lambda .
docker tag pywa-aws-lambda:latest <your-ecr-url>.amazonaws.com/pywa-aws-lambda:latest
docker push <your-ecr-url>.amazonaws.com/pywa-aws-lambda:latest
```

### 4. Create Lambda Function

In the AWS Console:
- Go to **Lambda** and create a new function.
- Select **Container Image** as the deployment package.
- Choose your ECR image from the previous step.

### 5. Configure Function URL

- Go to the **Configuration** tab of your Lambda function.
- Under **Function URL**, enable the URL and note it down for future use.

### 6. Set Environment Variables

In the Lambda function's environment variables, configure the following:

- `WHATSAPP_PHONE_ID`
- `WHATSAPP_TOKEN`
- `WHATSAPP_BUSINESS_ACCOUNT_ID`
- `WHATSAPP_VERIFY_TOKEN`
- `WHATSAPP_APP_ID`
- `WHATSAPP_APP_SECRET`

Refer to the [PyWa documentation](https://pywa.readthedocs.io/en/latest/) to learn how to configure each of these environment variables.

### 7. Register Webhook

After your first function deployment, register the webhook by invoking the following `PATCH` request:

```bash
https://<your-deployed-lambda-url>/RegisterWebhook
```

### 8. Test

Once the webhook is registered, test the function by sending WhatsApp messages to your connected phone number. The function should receive and respond to the messages.
