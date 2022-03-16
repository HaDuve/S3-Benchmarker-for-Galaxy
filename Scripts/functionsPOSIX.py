# Time-testable functions to be called by benchmarker.py - timeit
# Author: Hannes Duve
import os
from hashlib import md5
import gzip
import h5py

class FunctionManager:
    def __init__(self, args):
        self.args = args

    def uploadPOSIX(self, sourceDir : str = "~/testdata", targetDir : str = "~/mnt/testdata"):
        """copies the folder or file to another POSIX volume via cp

        Args:
            sourceDir (str, optional): [Source Directory]. Defaults to "/testdata".
            targetDir (str, optional): [Target Directory]. Defaults to "/mnt/testdata".
        """
        os.system("cp -Rf "+sourceDir+" "+targetDir)

    def deletePOSIX(self, filename : str = "test.txt"):
        """delete the directory or file from POSIX"""
        os.system("rm -rf " + filename)

    def readPOSIX(self, filename : str = "test.txt"):
        """Read from POSIX file

        Args:
            filename (str, optional): [Name of the file]. Defaults to "test.txt".
        """
        if(self.args.arg1.endswith('.hdf5')):
            f1 = h5py.File(filename,'r+')
        elif(self.args.arg1.endswith('.gz')):
            with open(filename, 'rb') as file:
                gzip_fd = gzip.GzipFile(fileobj=file)
                for line in gzip_fd:
                    tmp = line
        else:
            with open(filename, "r") as file:
                for line in file:
                    tmp = line
        return tmp

    def seekPOSIX(self, filename : str = "test.txt", pos : str = "0"):
        """Seek from POSIX file
        """
        pos = int(pos)
        with open(filename, "r") as file:
            file.seek(pos)
            return file.tell()

    # Checksum
    def checksumPOSIX(self, fileName : str = "test.txt"):
        """Create Checksum from POSIX file
        """
        hash = md5()
        with open(fileName, "rb") as f:
            for chunk in iter(lambda: f.read(128 * hash.block_size), b""):
                hash.update(chunk)
        digest = hash.hexdigest()
        return digest

    # Test and Debug Functions
    def testPOSIX(self, max : str = 1000000):
        """Random test function, puts a list of 1 mio ints together"""
        max = int(max)
        l = []
        for i in range(max):
            l.append(i)

    def debugPOSIX(self, arg1:str = "default 1", arg2:str= "default 2", arg3:str= "default 3"):
        print('debugPOSIX called')
        print(r'arg1: ', arg1)
        print(r'arg2: ', arg2)
        print(r'arg3: ', arg3)