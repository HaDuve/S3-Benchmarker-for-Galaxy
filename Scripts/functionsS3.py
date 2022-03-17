# Time-testable functions to be called by benchmarker.py - timeit
# Author: Hannes Duve
import os
from tkinter import TRUE
import boto3
from botocore.utils import fix_s3_host
from hashlib import md5

class FunctionManager:
    def __init__(self, args):
        self.args = args
        self.access_key = os.environ.get('AWS_ACCESS_KEY_ID')
        self.secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

        self.s3 = boto3.resource('s3',
                            aws_access_key_id=self.access_key,
                            aws_secret_access_key=self.secret_key,
                            region_name=self.args.default_region,
                            endpoint_url=self.args.s3_url)
        self.s3.meta.client.meta.events.unregister('before-sign.s3', fix_s3_host)

    # Upload / Copy
    def uploadS3(self,
                 sourceDir : str = "~/testdata",
                 targetDir : str = "/testdata/raw",
                 targetBucket : str = "s3ws:frct-hadu-bench-ec61-01"):
        """uploads the folder or file to the S3 Bucket via rclone

        Args:
            sourceDir (str, optional): [Source Directory]. Defaults to "/testdata".
            targetDir (str, optional): [Target Directory]. Defaults to "/testdata/raw".
            targetBucket (str, optional): [Target Bucket]. Defaults to "s3ws:frct-hadu-bench-ec61-01".
        """
        os.system("rclone copy -P --transfers=4 "+sourceDir+" "+targetBucket+targetDir)

    # Delete / remove
    def deleteS3(self, directory : str = "/testdata", bucket : str = "frct-hadu-bench-ec61-01"):
        """delete the S3 Bucket, directory TODO: or object

        Args:
            directory (str, optional): Defaults to "/testdata".

        """
        if(directory != ""):
            os.system("rclone delete s3ws:"+directory)
        else:
            raise Exception("Specification of bucket path needed!")

    # Read
    def readS3(self, key: str = 'testdata/raw/test.txt', bucket: str = 'frct-hadu-bench-ec61-01', ):
        """reads a file directly from s3 using boto3 connection

        Args:
            bucket (str, optional): [name of the bucket]. Defaults to 'frct-hadu-bench-ec61-01'.
            key (str, optional): [path / name of the file]. Defaults to 'testdata/raw/test.txt'.
        """
        obj = self.s3.Object(bucket, key)
        body = (obj.get()['Body'].read().decode('utf-8'))
        return body

    # Seek
    def seekS3(self,
               key: str = 'testdata/raw/test.txt',
               num : str = '1000',
               bucket: str = 'frct-hadu-bench-ec61-01'):
        """download from S3 and then seek the file

        Args:
            pathName (str, optional): [pathName]. Defaults to "s3ws:frct-hadu-bench-ec61-01/testdata/".
            fileName (str, optional): [fileName]. Defaults to "test.txt".
            num (str, optional): [seek pointer integer]. Has to be a string of an integer. Defaults to 0.
        """
        obj = self.s3.Object(bucket, key)
        point = obj.get(Range='bytes='+num+'-')['Body']
        return point

    # Checksum
    def checksumS3(self,
                   key: str = 'testdata/raw/test.txt',
                   bucket: str = 'frct-hadu-bench-ec61-01'):
        """Download from S3 and then checksum

        Args:
            pathName (str, optional): [description]. Defaults to "s3ws:frct-hadu-bench-ec61-01/testdata/".
            fileName (str, optional): [description]. Defaults to "test.txt".
        """
        f = open("tmp", "w")
        self.s3.meta.client.download_file(bucket, key, 'tmp')
        hash = md5()
        with open('tmp', "rb") as f:
            for chunk in iter(lambda: f.read(128 * hash.block_size), b""):
                hash.update(chunk)
        digest = hash.hexdigest()
        f.close()
        return digest




    # Test and Debug Functions
    def testS3(self, max : str = 1000000):
        """Random test function, puts a list of 1 mio ints together"""
        max = int(max)
        l = []
        for i in range(max):
            l.append(i)

    def debugS3(self, arg1:str = "default 1", arg2:str= "default 2", arg3:str= "default 3"):
        print('debug called')
        print(r'arg1: ', arg1)
        print(r'arg2: ', arg2)
        print(r'arg3: ', arg3)

    def lsS3(self, bucket : str =  "frct-hadu-bench-ec61-01"):
        """lists all files in a bucket recusively

        Args:
            bucket (str, optional): [name of bucket]. Defaults to "frct-hadu-bench-ec61-01".
        """
        os.system("aws s3api list-objects --bucket "+bucket
                  +" --output text --query \"Contents[].{Key: Key}\"")