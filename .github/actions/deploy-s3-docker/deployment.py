import os
import boto3
from botocore.config import Config as cfg

def run():
    bucket_name = os.environ['INPUT_BUCKET-NAME']
    bucket_region = os.environ['INPUT_BUCKET-REGION']
    dist_older = os.environ['INPUT_DIST-FOLDER']

    configuration = cfg(region_name=bucket_region)

    s3_client = boto3.client('s3', config=configuration)

    for root, subdirs, files in os.walk(dist_older):
        for file in files:
            s3_client.upload_file(os.path.join(root, file), bucket_name, file)

    website_url = f'http://${bucket_name}.s3-website-${bucket_region}.amazonaws.com'
    # print(f'::set-output name=website_url::{website_url}')
    os.system(f'echo \"website-url={website_url}\" >> $GITHUB_OUTPUT')

if __name__ == '__main__':
    run()