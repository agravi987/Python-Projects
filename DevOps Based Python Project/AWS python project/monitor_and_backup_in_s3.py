import boto3
import psutil
import platform
import socket
from datetime import datetime
from botocore.exceptions import ClientError


def create_bucket(bucket_name):

    session = boto3.session.Session()
    region = session.region_name

    s3 = boto3.client('s3')

    try:

        # us-east-1 special case
        if region == "us-east-1":

            s3.create_bucket(
                Bucket=bucket_name
            )

        else:

            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
            )

        print(f"Bucket '{bucket_name}' created successfully.")

    except ClientError as e:

        # Ignore if bucket already exists
        error_code = e.response['Error']['Code']

        if error_code == "BucketAlreadyOwnedByYou":
            print(f"Bucket '{bucket_name}' already exists.")

        else:
            print(f"Bucket creation error: {e}")


def collect_system_info():

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage('/')

    hostname = socket.gethostname()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
========== SYSTEM MONITORING REPORT ==========

Timestamp    : {timestamp}
Hostname     : {hostname}

CPU Usage    : {cpu} %

Memory Usage : {memory.percent} %

Disk Usage   : {disk.percent} %

================================================
"""

    return report


def save_report(report):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"system_report_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(report)

    print(f"Report saved locally: {filename}")

    return filename


def upload_to_s3(file_name, bucket_name):

    s3 = boto3.client('s3')

    try:

        s3.upload_file(
            file_name,
            bucket_name,
            file_name
        )

        print(f"File uploaded successfully to bucket '{bucket_name}'")

    except ClientError as e:

        print(f"S3 Upload Error: {e}")


if __name__ == "__main__":

    # Make bucket name globally unique
    bucket_name = "ravi-monitoring-backup-2026-001"

    # Step 1: Create bucket
    create_bucket(bucket_name)

    # Step 2: Collect monitoring data
    report = collect_system_info()

    # Step 3: Save report locally
    file_name = save_report(report)

    # Step 4: Upload to S3
    upload_to_s3(file_name, bucket_name)