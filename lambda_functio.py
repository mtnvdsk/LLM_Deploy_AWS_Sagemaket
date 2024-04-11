import json
import boto3

END_POINT="huggingface-pytorch-tgi-inference-0000-00-00-00-00-00-000"
runtime=boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    
    query_params=event["queryStringParameters"]
    query=query_params.get("query")
    payload={
        'inputs':query,
        'parameters':{
            'do_sample':True,
            'top_p':0.7,
            'top_k':50,
            'temperature':0.3,
            'max_new_tokens':512,
            'repition_penalty':1.03
        }
    }
    
    response=runtime.invoke_endpoint(EndpointName=END_POINT,ContentType="application/json",Body=json.dumps(payload))
    prediction=json.loads(response['Body'].read().decode('utf-8'))
    final_result=prediction[0]['generated_text']
    
    return {
        'statusCode': 200,
        'body': json.dumps(final_result)
    }
