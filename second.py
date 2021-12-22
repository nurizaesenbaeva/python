import json
import boto3
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement

    # print("hanlder:event")
    # print(event)
    # bucketDump()
    setBucketPolicy(bucketDump())


def bucketDump():
    ##This program lists all exsisting buckets within an aws account (Tommy's Personal Account)
    response = s3.list_buckets()

    buckets = []
    for bucket in response['Buckets']:
            value = bucket["Name"]
            buckets.append(value)
    return buckets

##setting a bucket policy
def setBucketPolicy(buckets):
    for bucket in buckets:
        value = s3.get_bucket_logging(bucket)
        print(value)


        ##TODO if bucket in buckets does not have loggin enabled, enable it!

        # print(bucket)
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
