# S3 Benchmarker for Galaxy
 Investigating and benchmarking distributed filesystems for the European Galaxy server

 Benchmarks the performance of different functions and compares S3 timings with POSIX timings.
 
## How to use:

### Easy way:
 1. Setup Config
 2. Run runbench.py

### Hard way:
 python benchmarker.py functionname -i [optional_number_of_iterations] -r [optional_number_of_repetitions] --arg1 [optional_arg1] ... --arg3 [optional_arg3]
 
 
 Test Data:
 
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
