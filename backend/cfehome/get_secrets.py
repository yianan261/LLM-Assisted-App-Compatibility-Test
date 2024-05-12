# import boto3

# def get_secret():
#     secret_name = "YOUR_SECRET_NAME"
#     region_name = "YOUR_AWS_REGION"

#     # Create a Secrets Manager client
#     session = boto3.session.Session()
#     client = session.client(service_name="secretsmanager", region_name=region_name)

#     try:
#         get_secret_value_response = client.get_secret_value(SecretId=secret_name)
#     except Exception as e:
#         raise e
#     else:
#         # Decryption happens automatically with boto3
#         secret = get_secret_value_response["SecretString"]
#         return json.loads(secret)

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "rds!db-95a014cb-5977-4e51-9de7-d9658fee7db9"
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response["SecretString"]
    print("SECRET",secret)
    # Your code goes here.


# Use the secret in your database configuration
# secrets = get_secret()
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": secrets["dbname"],
#         "USER": secrets["username"],
#         "PASSWORD": secrets["password"],
#         "HOST": secrets["host"],
#         "PORT": secrets["port"],
#     }
# }
