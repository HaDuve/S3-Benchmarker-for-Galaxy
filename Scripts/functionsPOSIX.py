# Time-testable functions to be called by benchmarker.py - timeit
# Author: Hannes Duve
import os
from hashlib import md5

class FunctionManager:
    def __init__(self, args):
        self.args = args

    def uploadPOSIX(self, sourceDir : str = "~/testdata", targetDir : str = "~/mnt/testdata"):
        """copies the folder or file to another POSIX volume via cp

        Args:
            sourceDir (str, optional): [Source Directory]. Defaults to "/testdata".
            targetDir (str, optional): [Target Directory]. Defaults to "/mnt/testdata".
        """
        os.system("pv -R "+sourceDir+" "+targetDir)

    def deletePOSIX(self, filename : str = "test.txt"):
        """delete the directory or file from POSIX"""
        os.system("rm -rf " + filename)

    def readPOSIX(self, filename : str = "test.txt"):
        """Read from POSIX file

        Args:
            filename (str, optional): [Name of the file]. Defaults to "test.txt".
        """
        #TODO: rewrite this to os.path to open directories
        with open(filename, "r") as file:
            body = file.read()
            return body

    def seekPOSIX(self, filename : str = "test.txt", pos : str = "0"):
        """Seek from POSIX file
        """
        pos = int(pos)
        #TODO: rewrite this to os.path to open directories
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