
# AWS Lambda Code Generator Using Amazon Bedrock

## Overview

This project demonstrates how to use an AWS Lambda function to generate code using the Amazon Bedrock service and save the generated code to an Amazon S3 bucket. The code utilizes the `boto3` library to interact with AWS services.

## Prerequisites

Before you begin, ensure that you have the following set up:

1. **AWS Account**: You must have an AWS account with access to the following services:
   - AWS Lambda
   - Amazon S3
   - Amazon Bedrock

2. **AWS CLI**: Install the AWS Command Line Interface (CLI) and configure it with your AWS credentials.

3. **Boto3 Library**: Ensure you have the `boto3` library installed. You can install it using pip:

   ```bash
   pip install boto3
   ```

4. **IAM Roles**: Ensure that your Lambda function has the necessary IAM roles to access Amazon Bedrock and S3 services.

## Code Description

### Functions

1. **`code_generator_using_bedrock(message: str) -> str`**:
   - This function generates code based on the provided message using the Amazon Bedrock service.
   - **Parameters**:
     - `message` (str): The task or description for which code needs to be generated.
   - **Returns**:
     - `generated_code` (str): The generated code as a string. If there's an error, it returns an empty string.

2. **`save_code_s3(s3_key: str, s3_bucket: str, generate_code: str)`**:
   - This function saves the generated code to an S3 bucket.
   - **Parameters**:
     - `s3_key` (str): The key (path) under which the generated code will be saved in the S3 bucket.
     - `s3_bucket` (str): The name of the S3 bucket.
     - `generate_code` (str): The generated code to be saved.
   - **Returns**:
     - None. It prints a success or error message.

3. **`lambda_handler(event, context) -> dict`**:
   - The main Lambda function handler. It triggers the code generation and saving process.
   - **Parameters**:
     - `event`: The event data passed to the Lambda function, containing the message for code generation.
     - `context`: The runtime information provided by AWS Lambda.
   - **Returns**:
     - A dictionary containing the status code and a message indicating the completion of code generation.

### Workflow

1. **Event Trigger**:
   - The Lambda function is triggered by an event that contains a JSON body with a `msg` field.

2. **Code Generation**:
   - The `code_generator_using_bedrock` function generates code using Amazon Bedrock based on the provided `message`.

3. **Saving to S3**:
   - The generated code is saved to an S3 bucket with a unique key based on the current timestamp.

4. **Response**:
   - The Lambda function returns a response indicating whether the code generation process was completed successfully.

## Usage

1. Deploy the code to an AWS Lambda function.
2. Trigger the Lambda function with an event containing the `msg` field in the body, which describes the task for which you want to generate code.
3. The Lambda function will generate the code and save it to the specified S3 bucket.
4. Check the S3 bucket for the generated code.

## Example Event

```json
{
    "body": "{\"msg\": \"Create a Python function to reverse a string\"}"
}
```

## Notes

- Ensure that the Lambda function has the correct permissions to invoke the Amazon Bedrock service and write to the S3 bucket.
- The model ID `meta.llama3-70b-instruct-v1:0` is used in this example. You may need to update it based on your specific use case.

## Troubleshooting

- **Error in Code Generation**: Check the logs for any issues related to the invocation of Amazon Bedrock.
- **S3 Upload Issues**: Ensure that the S3 bucket name is correct and that the Lambda function has write permissions to the bucket.

---
