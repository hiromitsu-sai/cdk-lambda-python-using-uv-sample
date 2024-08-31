import boto3

from libs.log import logger

if __name__ == "__main__":
    if boto3.client("s3"):
        logger.info("S3 client created successfully")
        print("S3 client created successfully")
