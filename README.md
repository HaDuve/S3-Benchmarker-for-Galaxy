# S3 Benchmarker for Galaxy
 Investigating and benchmarking distributed filesystems for the European Galaxy server

 Benchmarks the performance of different functions and compares S3 timings with POSIX timings.

## How to use:

### Configurated way:
 1. Setup config.ini  :

        [S3 Connection]
        default_region = fr-repl                       # standard region
        s3_url = https://s3.bwsfs.uni-freiburg.de/     # standard bwsfs url

        [Workflow]
        workflow = debug,uploadS3,test                 # comma separated functions from FunctionManager class
        workflowargs = 3 2 1,,10                       # comma separated arguments for functions (space-separated for multiple args)
        repetitions = 10                               # how often each function should be tested
        warmup = True                                  # omit first run?
        cleanup = True                                 # delete certain files after each run?

        [Log]
        runs = 0                                       # logging for .csv files, ignore it

 3. Run runbench.py

### Manual way:
 python benchmarker.py functionname -i [optional_number_of_iterations] -r [optional_number_of_repetitions] --arg1 [optional_arg1] ... --arg3 [optional_arg3]

## Returns a data file
#### data_uploadS3_run1.csv:

Operation       |Time                 |
----------------|---------------------|
uploadS3        |             0.802693|
uploadS3        |             0.789800|
uploadS3        |             0.770129|
uploadS3        |             0.776668|
uploadS3        |             0.785811|
uploadS3        |             0.782927|
uploadS3        |             0.766997|
uploadS3        |             0.776960|
uploadS3        |             0.780780|
uploadS3        |             0.781875|
