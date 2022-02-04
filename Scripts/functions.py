# Time-testable functions to be called by benchmarker.py - timeit
# Author: Hannes Duve
import os
import boto3
from botocore.utils import fix_s3_host
from hashlib import md5

# Upload / Copy
def uploadS3(sourceDir : str = "~/testdata", targetDir : str = "/testdata/raw"):
    """uploads the folder or file to the specific "s3ws:frct-hadu-bench-ec61-01" S3 Bucket via rclone

    Args:
        sourceDir (str, optional): [Source Directory]. Defaults to "/testdata".
        targetDir (str, optional): [Target Directory]. Defaults to "/testdata/raw".
    """
    os.system("rclone copy -P --transfers=4 "+sourceDir+" s3ws:frct-hadu-bench-ec61-01"+targetDir)

def uploadPOSIX(sourceDir : str = "~/testdata", targetDir : str = "~/mnt/testdata"):
    """copies the folder or file to another POSIX volume via cp

    Args:
        sourceDir (str, optional): [Source Directory]. Defaults to "/testdata".
        targetDir (str, optional): [Target Directory]. Defaults to "/mnt/testdata".
    """
    os.system("cp -R "+sourceDir+" "+targetDir)



# Delete / Purge / Remove
def deleteS3(directory : str = "/testdata", bucket : str = "frct-hadu-bench-ec61-01"):
    """delete the S3 Bucket, directory TODO: or object

    Args:
        directory (str, optional): Defaults to "/testdata".

    """
    if(directory != ""):
        os.system("rclone purge s3ws:"+directory)

def deletePOSIX(filename : str = "test.txt"):
    """delete the directory or file from POSIX"""
    os.system("rm -rf " + filename)



# Read
def readS3(bucket: str = 'frct-hadu-bench-ec61-01', key: str = 'testdata/raw/test.txt'):
    """reads a file directly from s3 using boto3 connection

    Args:
        bucket (str, optional): [name of the bucket]. Defaults to 'frct-hadu-bench-ec61-01'.
        key (str, optional): [path / name of the file]. Defaults to 'testdata/raw/test.txt'.
    """
    def_region= "fr-repl"
    endp_url = "https://s3.bwsfs.uni-freiburg.de/"
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=def_region,endpoint_url=endp_url)
    s3.meta.client.meta.events.unregister('before-sign.s3', fix_s3_host)

    obj = s3.Object(bucket, key)
    body = (obj.get()['Body'].read().decode('utf-8'))
    print(body)


def readPOSIX(filename : str = "test.txt"):
    """Read from POSIX file

    Args:
        filename (str, optional): [Name of the file]. Defaults to "test.txt".
    """
    with open(filename, "r") as file:
        file.read()



# Seek
def seekS3(bucket: str = 'frct-hadu-bench-ec61-01', key: str = 'testdata/raw/test.txt', num : str = '0'):
    """download from S3 and then seek the file

    Args:
        pathName (str, optional): [pathName]. Defaults to "s3ws:frct-hadu-bench-ec61-01/testdata/".
        fileName (str, optional): [fileName]. Defaults to "test.txt".
        num (str, optional): [seek pointer integer]. Has to be a string of an integer. Defaults to 0.
    """
    def_region= "fr-repl"
    endp_url = "https://s3.bwsfs.uni-freiburg.de/"
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=def_region,endpoint_url=endp_url)
    s3.meta.client.meta.events.unregister('before-sign.s3', fix_s3_host)

    obj = s3.Object(bucket, key)
    point = obj.get(Range='bytes='+num+'-')['Body']
    print(point.read())

def seekPOSIX(filename : str = "test.txt", pos : str = "0"):
    """Seek from POSIX file
    """
    pos = int(pos)
    with open(filename, "r") as file:
        file.seek(pos)



# Checksum
def checksumS3(bucket: str = 'frct-hadu-bench-ec61-01', key: str = 'testdata/raw/test.txt'):
    """Download from S3 and then checksum

    Args:
        pathName (str, optional): [description]. Defaults to "s3ws:frct-hadu-bench-ec61-01/testdata/".
        fileName (str, optional): [description]. Defaults to "test.txt".
    """
    def_region= "fr-repl"
    endp_url = "https://s3.bwsfs.uni-freiburg.de/"
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=def_region,endpoint_url=endp_url)
    s3.meta.client.meta.events.unregister('before-sign.s3', fix_s3_host)

    hash = md5()
    obj = s3.Object(bucket, key)
    hash.update(obj.get()['Body'].read())
    print("hash :", hash.hexdigest())

def checksumPOSIX(fileName : str = "test.txt"):
    """Create Checksum from POSIX file
    """
    hash = md5()
    with open(fileName, "rb") as f:
        for chunk in iter(lambda: f.read(128 * hash.block_size), b""):
            hash.update(chunk)
    print("hash :", hash.hexdigest())




# Test and Debug Functions
def test(max : str = 1000000):
    """Random test function, puts a list of 1 mio ints together"""
    max = int(max)
    l = []
    for i in range(max):
        l.append(i)

def debug(arg1:str = "default 1", arg2:str= "default 2", arg3:str= "default 3"):
    print('debug called')
    print(r'arg1: ', arg1)
    print(r'arg2: ', arg2)
    print(r'arg3: ', arg3)

def debugPOSIX(arg1:str = "default 1", arg2:str= "default 2", arg3:str= "default 3"):
    print('debugPOSIX called')
    print(r'arg1: ', arg1)
    print(r'arg2: ', arg3)
    print(r'arg3: ', arg3)

def lsS3(bucket : str =  "frct-hadu-bench-ec61-01"):
    """lists all files in a bucket recusively

    Args:
        bucket (str, optional): [name of bucket]. Defaults to "frct-hadu-bench-ec61-01".
    """
    os.system("aws s3api list-objects --bucket "+bucket+" --output text --query \"Contents[].{Key: Key}\"")