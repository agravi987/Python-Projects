import boto3 
from botocore.exceptions import ClientError

def show_buckets():
    s3 = boto3.client('s3')
    try:
        response = s3.list_buckets()
        print("Buckets: ")
        for bucket in response['Buckets']:
            print(f" - {bucket['Name']}")

    except ClientError as e:
        print(f"Error listing buckets: {e}")



def create_bucket(bucket_name, region=None):
    s3 = boto3.client('s3')
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
        print(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"Error creating bucket: {e}")


def delete_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except ClientError as e:
        print(f"Error deleting bucket: {e}")


if __name__ == "__main__":
    show_buckets()
    # create_bucket("ravi-devops-demo-ravi-2026-001")
    # delete_bucket("ravi-devops-demo-ravi-2026-001")
    # delete_bucket("empty-bucket-102938")