# Time-testable functions to be called by benchmarker.py - timeit
# Author: Hannes Duve
import os
import utils

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
    else:
        inp = input("Really delete the Bucket: %s ?" % bucket)
        if(inp == "Y" or inp == "y" or inp == "yes" or inp == "Yes"):
            os.system("rclone purge s3ws:"+directory)

def deletePOSIX(filename : str = "test.txt"):
    """delete the directory or file from POSIX"""
    os.system("rm -rf " + filename)



# Read
def readS3(object_name : str = "test", s3_bucket_name : str = "frct-hadu-bench-ec61-01"):
    """TODO: Read from S3 Bucket object
    """
    pass


def readPOSIX(filename : str = "test.txt"):
    """Read from POSIX file

    Args:
        filename (str, optional): [Name of the file]. Defaults to "test.txt".
    """
    with open(filename, "r") as file:
        file.read()



# Seek
def seekS3():
    """TODO: Seek from S3 Bucket object
    """
    pass
    
def seekPOSIX(filename : str = "test.txt", pos : str = "0"):
    """Seek from POSIX file
    """
    pos = int(pos)
    with open(filename, "r") as file:
        file.seek(pos)



# Checksum
def checksumS3(filepath : str = "test.txt"):
    """TODO: Create Checksum from S3 Bucket object
    """
    pass

def checksumPOSIX(filename : str = "test.txt"):
    """TODO: Create Checksum from POSIX file
    """
    import hashlib
    md5_hash = hashlib.md5()
    with open(filename, "r") as file:
        content = file.read()
        md5_hash.update(content)    
        digest = md5_hash.hexdigest()
    print(digest)



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