# S3 Benchmarker for Galaxy
 Investigating and benchmarking distributed filesystems for the European Galaxy server

 Benchmarks the performance of different functions and compares S3 timings with POSIX timings.
 
# How to use:
 python benchmarker.py functionname -i [optional_number_of_iterations] -r [optional_number_of_repetitions] --arg1 [optional_arg1] ... --arg3 [optional_arg3]
 
 
 Test Data:

Operation   | Iterations |          Time       |    AverageTime  
------------|------------|---------------------|-----------------
test        |           1|             0.802693|         0.802693
test        |           1|             0.789800|         0.789800
test        |           1|             0.770129|         0.770129
test        |           1|             0.776668|         0.776668
test        |           1|             0.785811|         0.785811
test        |           1|             0.782927|         0.782927
test        |           1|             0.766997|         0.766997
test        |           1|             0.776960|         0.776960
test        |           1|             0.780780|         0.780780
test        |           1|             0.781875|         0.781875
             
