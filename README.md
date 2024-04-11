# Deploying Large Language Models (LLMs) on AWS SageMaker

This guide will walk you through the process of deploying Large Language Models (LLMs) on AWS SageMaker.

## Prerequisites
Before you begin, ensure you have the following:
- An AWS account with the necessary permissions to create and manage SageMaker resources.
- A trained language model saved in a format compatible with SageMaker, such as TensorFlow SavedModel or PyTorch model.
- Basic knowledge of AWS SageMaker concepts and usage.

## Steps

### 1. Prepare your model
- Ensure your language model is trained and saved in a format compatible with SageMaker.
- If necessary, package your model code and dependencies into a Docker container for SageMaker inference.

### 2. Upload your model to Amazon S3 or from HuggingFace
- Upload your trained model artifacts to an Amazon S3 bucket.
- Ensure that the IAM role used by SageMaker has permissions to access the S3 bucket.

### 3. Set up SageMaker
- Log in to the AWS Management Console and navigate to Amazon SageMaker.
- Create a new SageMaker notebook instance or use an existing one.
- Open a Jupyter notebook and create a SageMaker endpoint configuration.

### 4. Deploy your model
- Use the SageMaker SDK to deploy your model to a SageMaker endpoint.
- Specify the model artifacts location on S3 and configure the instance type and count.

### 5. Test your deployment
- Once the deployment is complete, test your model by sending sample input data to the SageMaker endpoint.
- Verify that the model inference results are as expected.

### 6. Monitor and manage your endpoint
- Monitor the performance and usage of your SageMaker endpoint using Amazon CloudWatch.
- If necessary, update or delete your SageMaker endpoint to manage costs and resources.

## Additional Resources
- [AWS SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
- [SageMaker Python SDK Documentation](https://sagemaker.readthedocs.io/en/stable/)
- [SageMaker Model Deployment Best Practices](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practices.html)

## Example Code Snippet (Python - SageMaker SDK)
```python
import sagemaker
from sagemaker import Model

# Set up SageMaker session and role
sagemaker_session = sagemaker.Session()
role = "arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole-20220318T124567"

# Define model artifacts location on S3
model_data = "s3://your-bucket-name/path/to/model.tar.gz"

# Create a SageMaker model
model = Model(
    model_data=model_data,
    image_uri="your-model-image-uri",
    role=role,
    sagemaker_session=sagemaker_session
)

# Deploy the model to a SageMaker endpoint
predictor = model.deploy(
    instance_type="ml.m5.large",
    initial_instance_count=1
)

# Test the deployed model
result = predictor.predict("Sample input data")
print(result)

# Requirements for this repo
  - [Python 3.8 using venv](https://awstip.com/how-to-use-a-newer-python-version-in-aws-sagemaker-notebook-1682a89625ef)
  - Lamba Function with the code in lambda_function.py
