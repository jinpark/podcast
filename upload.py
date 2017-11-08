import boto3
import click
import os

def s3_upload(file, filename):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS'),
        aws_secret_access_key=os.getenv('AWS_SECRET')
    )
    bucket_name = 'jin-pleb-podcast'
    keyname = 'audio/podcast/' + filename
    s3_client.upload_file(file, bucket_name, keyname)


@click.command()
@click.option('--file', required=True)
@click.option('--filename', required=True)
def main(file, filename):
    s3_upload(file, filename)

if __name__ == '__main__':
    main()
