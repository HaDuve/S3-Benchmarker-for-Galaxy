# Time-testable functions to be called by benchmarker.py - timeit
# Author: Hannes Duve
import os
import utils

# Upload / Copy
def uploadS3(sourceDir = "~/testdata", targetDir = "/testdata/raw"):
    """uploads the folder or file to the specific "s3ws:frct-hadu-bench-ec61-01" S3 Bucket via rclone

    Args:
        sourceDir (str, optional): [Source Directory]. Defaults to "/testdata".
        targetDir (str, optional): [Target Directory]. Defaults to "/testdata/raw".
    """
    os.system("rclone copy -P --transfers=4 "+sourceDir+" s3ws:frct-hadu-bench-ec61-01"+targetDir)
    
def uploadPOSIX(sourceDir = "~/testdata", targetDir = "~/mnt/testdata"):
    """copies the folder or file to another POSIX volume via cp

    Args:
        sourceDir (str, optional): [Source Directory]. Defaults to "/testdata".
        targetDir (str, optional): [Target Directory]. Defaults to "/mnt/testdata".
    """
    os.system("cp -R "+sourceDir+" "+targetDir)



# Delete / Purge / Remove
def deleteS3(directory = "/testdata", bucket="frct-hadu-bench-ec61-01"):
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

def deletePOSIX(filename:str="test.txt"):
    """delete the directory or file from POSIX"""
    os.system("rm -rf" + filename)
    pass



# Read
def readS3(s3_bucket_name = "frct-hadu-bench-ec61-01", prefixFilter = ""):
    """TODO: Read from S3 Bucket object
    """
    s3 = utils.connectBoto(s3_bucket_name)
    my_bucket=s3.Bucket(s3_bucket_name)
    bucket_list = []
    prefix = prefixFilter
    # To search with prefix and suffix:
    # for file in my_bucket.objects.filter(prefix):
    #     file_name=file.key
    #     if file_name.find(".csv")!=-1:
    #         bucket_list.append(file.key)
    for file in my_bucket.objects.all():
        bucket_list.append(file.key)
    print("length of Bucketlist: ", len(bucket_list))
    print(bucket_list[0:10])

def readPOSIX():
    """TODO: Read from POSIX file
    """
    pass



# Seek
def seekS3():
    """TODO: Seek from S3 Bucket object
    """
    # Python program to demonstrate
    # seek() method
    
    
    # Opening "GfG.txt" text file
    f = open("test.txt", "r")
    
    # Second parameter is by default 0
    # sets Reference point to twentieth
    # index position from the beginning
    f.seek(20)
    
    # prints current position
    print(f.tell())
    
    print(f.readline())
    f.close()
    
def seekPOSIX():
    """TODO: Seek from POSIX file
    """
    pass



# Checksum
def checksumS3(filepath="test.txt"):
    """TODO: Create Checksum from S3 Bucket object
    """
    import hashlib
    md5_hash = hashlib.md5()
    a_file = open(filepath,"rb")
    content = a_file.read()
    md5_hash.update(content)
    
    digest = md5_hash.hexdigest()
    print(digest)
    a_file.close()
    pass

def checksumPOSIX():
    """TODO: Create Checksum from POSIX file
    """
    pass



# Test and Debug Functions
def test(max = 1000000):
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