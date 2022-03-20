with open("nhf.csv", "r") as f:
    lines = f.readlines()
# get a list of all Operations
operations = []
for line in lines:
    op_end_index = line.find(",")
    if (line[:op_end_index] not in operations):
        operations.append(line[:op_end_index])
operations.remove('Operation')
operations.remove('')
print('operations: ', operations)

#split into operating systems
# POSIX S3
for system in ["POSIX", "S3"]:
    with open("Systems/"+system+".csv", "w") as f:
        headerline = True
        for line in lines:
            if (headerline):
                headerline=False
                f.write(line)
                continue
            if (system in line):
                f.write(line)

# split files into operations
# list of operations
# 'checksumPOSIX', 'checksumS3', 'deletePOSIX', 'readPOSIX', 'seekPOSIX', 'uploadPOSIX', 'uploadS3'
for operation in operations:
    with open("Operations/"+operation+".csv", "w") as f:
        headerline = True
        for line in lines:
            if (headerline):
                headerline=False
                f.write(line)
                continue
            if (operation in line):
                f.write(line)

# split files into operations + file type
# list of files:
# HDF5 JPG MP4 NetCDF FASTA FASTQ gzip
for filetype in ["HDF5", "JPG", "MP4", "NetCDF", "FASTA", "FASTQ", "gzip"]:
    for operation in operations:
        with open("OperationsFiletypes/"+operation+filetype+".csv", "w") as f:
            headerline = True
            for line in lines:
                if (headerline):
                    headerline=False
                    f.write(line)
                    continue
                if (operation in line):
                    if (filetype in line):
                        f.write(line)

# split files into system + file type
for system in ["POSIX", "S3"]:
    for filetype in ["HDF5", "JPG", "MP4", "NetCDF", "FASTA", "FASTQ", "gzip"]:
        with open("SystemsFiletype/"+system+filetype+".csv", "w") as f:
            headerline = True
            for line in lines:
                if (headerline):
                    headerline=False
                    f.write(line)
                    continue
                if (system in line):
                    if (filetype in line):
                        f.write(line)

# split files into system + file size
# ["small","medium","big"]
for system in ["POSIX", "S3"]:
    for filesize in ["small","medium","big"]:
        with open("SystemsFilesize/"+system+filesize+".csv", "w") as f:
            headerline = True
            for line in lines:
                if (headerline):
                    headerline=False
                    f.write(line)
                    continue
                if (system in line):
                    if (filesize in line):
                        f.write(line)