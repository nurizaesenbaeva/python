import boto3

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    # TODO implement
    setBucketPolicy(target_bucket='logs-bucket-nuriza')


def setBucketPolicy(target_bucket: str):
    for bucket in s3.buckets.all():
        if bucket.name.startswith("myapp-") :
            bucket_logging = s3.BucketLogging(bucket.name)
            if not bucket_logging.logging_enabled:
                bucket_logging.put(
                    BucketLoggingStatus={
                        'LoggingEnabled': {
                            'TargetBucket': target_bucket,
                            'TargetPrefix': f'{bucket.name}/'
                        }
                    }
                )
