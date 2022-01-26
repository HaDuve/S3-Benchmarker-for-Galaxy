# Utility functions for benchmarker.py
# Author: Hannes Duve
import sys, os, boto3

def save_file_as_csv(data, args):
    if not data:
        raise "No data error!"
    # put data into .csv
    headerstring = "Operation,Iterations,Time,AverageTime\n"
    datastring = ""
    if not args.r:              # no repetitions
        if (not args.i):        # default iterations
            datastring = f"{args.function},{1},{data[0]:f},{data[1]:f}"
        else:                   # modified iterations
            datastring = f"{args.function},{args.i},{data[0]:f},{data[1]:f}"
    else:                       # modified repetitions
        for i in range(args.r):
            if (not args.i):    # default iterations
                datastring += f"{args.function},{1},{data[i][0]:f},{data[i][1]:f}\n"
            else:               # modified iterations
                datastring += f"{args.function},{args.i},{data[i][0]:f},{data[i][1]:f}\n"
    
    filestring = headerstring + datastring
    
    print('filestring: \n'+ filestring)
    with open("data/data.csv", "w") as file1:
        # Writing data to a file
        file1.write(filestring)
    
def blockPrint():
    """Disable print output"""
    sys.stdout = open(os.devnull, 'w')
    
def enablePrint():
    """Restore print output"""
    sys.stdout = sys.__stdout__
 
def connectBoto(bucketName):
    """
    Accessing the S3 buckets using boto3 client
    
    Returns:
        Bucket
    """
    s3_client = boto3.client('s3')
    s3_bucket_name = bucketName
    s3 = boto3.resource('s3',
                        aws_access_key_id= '9IFHS2U0MX1C28Y15XM8',
                        aws_secret_access_key='qCRZduGNr1Zsw8hky91ZEKXzkTCT/4lzPuv++pr8')
    return s3


def purge(directory = "/testdata"):
    """purging the directory before upload, 
    
    Args:
        directory (str): careful with empty directory = "" because it will delete the bucket!
    
    """
    os.system("rclone purge s3ws:frct-hadu-bench-ec61-01" + directory)

def prepareBenchmark(args):
    """preparing the benchmark depending on args"""
    if(args.function == 'upload'):
        print('purging directory before uploading')
        purge("/testdata")
        
def afterBenchmark(args):
    """cleaning up after the benchmark depending on args"""
    if(args.cleanup == True):
        if(args.function == 'upload'):
            print('purging directory after uploading')
            purge("/testdata")
