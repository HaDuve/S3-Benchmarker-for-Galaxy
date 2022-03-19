# Utility functions for benchmarker.py
# Author: Hannes Duve
import sys, os
import time

def save_file_as_csv(data, args):
    """saving the results as a comma-separated list of data points

    Args:
        data (str): .csv filestring

        args (namespace):
    """
    if not data:
        print("No data error!")
        return
    # put data into .csv
    headerstring = "Operation,Time, Argument1, Argument2, Argument3\n"
    datastring = ""
    if not args.r: datastring = f"{args.function},{data:f},{args.arg1},{args.arg2},{args.arg3}"
    else:                       # modified repetitions
        for i in range(args.r):
                datastring += f"{args.function},{data[i]:f},{args.arg1},{args.arg2},{args.arg3}\n"

    filestring = headerstring + datastring

    print('filestring: \n'+ filestring)
    if not os.path.exists("data"):
        os.mkdir("data")
    with open("data/"+args.saveas+".csv", "w") as file1:
        # Writing data to a file
        file1.write(filestring)

def blockPrint():
    """Disable print output to console"""
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    """Restore print output"""
    sys.stdout = sys.__stdout__

def purge(directory = "/testdata"):
    """S3 purging the directory before upload,

    Args:
        directory (str): careful with empty directory = "" because it will delete the bucket!

    """
    os.system("rclone purge s3ws:frct-hadu-bench-ec61-01" + directory)

def delete(filename = "/testdata"):
    """S3 purging the directory before upload,

    Args:
        directory (str): careful with empty directory = "" because it will delete the bucket!

    """
    os.system("rclone delete s3ws:frct-hadu-bench-ec61-01" + filename)

def prepareBenchmark(args):
    """preparing the benchmark depending on args

    Args:

        "POSIX" in args.function  - checks if platform == linux

        'uploadS3'                - deleting target directory before upload

        'uploadPOSIX'             - creating target directory before copy
    """
    checkPOSIX(args.function)

    if(args.function == 'uploadS3'):
        print('LOG::  purging target file before uploading')
        if (args.arg2 is None):
            purge("/testdata/raw")
        else: #delete(args.arg2)
            pass

    if(args.function == 'uploadPOSIX'):
        # create directory before copy
        index = args.arg2.rfind("/")
        pathname = args.arg2[0:index]
        os.system("mkdir -p "+ pathname)
        print('LOG::  creating target ' +pathname+' directory before uploading')

    if(args.function == 'deletePOSIX'):
        # copy the file before deleting to recover after bench
        print("LOG::  copy the file before deleting to recover after bench")
        os.system("cp "+args.arg1+" "+args.arg1+"copy")
    if(args.function == 'deleteS3'):
        # copy the file before deleting to recover after bench
        print("LOG::  copy the file before deleting to recover after bench S3")
        os.system("rclone copy s3ws:frct-hadu-bench-ec61-01"+args.arg1+" s3ws:frct-hadu-bench-ec61-01/Copies"+args.arg1)


def afterBenchmark(args):
    """cleaning up after the benchmark depending on args"""
    # These functions will only be applied if cleanup mode is activated
    if(args.cleanup == "True"):
        if(args.function == 'uploadS3'):
            print(f'LOG::  purging {args.arg2} from s3 after uploading')
            purge(args.arg2)
        if(args.function == 'uploadPOSIX'):
            print(f'LOG::  removing "rm -rf" {args.arg2} after copying')
            os.system("rm -rf " + args.arg2)

    # These functions will be applied after every benchmark run
    if(args.function == 'deletePOSIX'):
        # recover file
        print("LOG::  recovering file after delete-benchmark")
        os.system("mv "+args.arg1+"copy " + args.arg1)
    if(args.function == 'deleteS3'):
        # recover file
        print("LOG::   copy back file after delete-benchmark S3")
        os.system("rclone copy s3ws:frct-hadu-bench-ec61-01/Copies"+args.arg1+" s3ws:frct-hadu-bench-ec61-01"+args.arg1)

def checkPOSIX(string = "POSIX"):
    if("POSIX" in string):
        platform1 = "linux"
        platform2 = "linux2"
        if(not (checkPlatform(platform1) or checkPlatform(platform2))):
            raise Exception("POSIX functions can only be tested on Linux platforms")

def checkPlatform(ComparePlatform):
    """[compares platforms and returns true if match, false otherwise]

    Args:
        ComparePlatform ([str]): [platform to be checked]

    Returns:
        [bool]: [true if sys.platform == Compared Platform]
    """
    from sys import platform
    return ComparePlatform == platform


