import boto3
import json
import botocore.config
from datetime import datetime

def code_generator_using_bedrock(message:str):
    prompt =f"Generate code for the task below {message}"

    body={
        "prompt":prompt,
        "max_gen_len":512,
        "temperature":0.5,
        "top_p":0.9
    }

    try:
        bedrock=boto3.client("bedrock-runtime", region_name="us-east-1", config=botocore.config.Config(read_timeout=300,retries={'max_attempts':3}))
        response=bedrock.invoke_model(body=json.dumps(body), modelId= "meta.llama3-70b-instruct-v1:0")

        response_content = response.get('body').read()
        response_data = json.loads(response_content)
        print(response_data)
        generated_code = response_data['generation']
        return generated_code
    
    except Exception as e:
        print(f"Error while generating code:{e}")
        return ""

def save_code_s3(s3_key, s3_bucket,generate_code):
    s3=boto3.client('s3')
    try:
        s3.put_object(Bucket = s3_bucket, Key = s3_key, Body = generate_code )
        print("Code saved to s3")

    except Exception as e:
        print("Error when saving the code to s3")
    
def lambda_handler(event, context):
    event=json.loads(event['body'])
    message = event['msg']

    generate_code = code_generator_using_bedrock(message=message)

    if generate_code:
        current_time = datetime.now().strftime('%H%M%S')
        s3_key = f"code-output/{current_time}.txt"
        s3_bucket="awscodegeneratordemo"
        save_code_s3(s3_key, s3_bucket, generate_code)
    else:
        print("No Code generated")
    
    return{
        'statusCode':200,
        'body':json.dumps('Code generation is completed')
    }
