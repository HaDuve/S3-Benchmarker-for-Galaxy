# Benchmarking Script 
# Author: Hannes Duve
import argparse
import utils
import functions
import timer

class Benchmarker:
    def __init__(self, args):
        self.args = args
        self.run()        
        
    def run(self):
        if self.args.r:         # repetitive measurement with r preparations
            data =  []
            utils.blockPrint()  # quiet mode
            for i in range(0,self.args.r):
                data.append(benchmark(self.args))
            utils.enablePrint()

        else:                   # single measurement (can still be repeated via -i with just 1 preparation)
            data = benchmark(self.args)
            
        print('args: ', self.args)
        utils.save_file_as_csv(data, self.args)    
    

def report_time(fn, arg1, arg2, arg3):
    # timing
    t = timer.Timer(name = fn)
    t.start()
    # assume we dont get arg3 without arg2 etc.
    if(arg3 is not None):
        result = getattr(functions, fn)(arg1, arg2, arg3)
    elif(arg2 is not None):
        result = getattr(functions, fn)(arg1, arg2)
    elif(arg1 is not None):
        result = getattr(functions, fn)(arg1)
    else: #all args==None
        result = getattr(functions, fn)()
    time = t.stop()
    
    # output handling
    print('result: ', result)
    return time

def benchmark(args): 
    """Calls the timing function with argument handling

    Args:
        args (str): the arguments given via the CLI
    Returns:
        data (list): list of data
    """
    utils.prepareBenchmark(args)
    data = report_time(args.function, args.arg1, args.arg2, args.arg3)
    utils.afterBenchmark(args)
    return data


if __name__=='__main__':
    """Argument handling and Data Saving"""
    parser = argparse.ArgumentParser(description="A tool to benchmark the time used for different functions")
    parser.add_argument('function', type=str, help='The function to be tested.'
                        , choices=['test','debug','debugPOSIX','lsS3','checksumS3','uploadS3','deleteS3','readS3','seekS3','checksumPOSIX',
                                   'uploadPOSIX','deletePOSIX','readPOSIX','seekPOSIX']
                        )
    # optionals
    parser.add_argument('-r', type=int, help='Repeat the measurement for r times to get a table of data (with preparation)')
    parser.add_argument('--warmup', default=False, help='If True, does a warmup before measurement')
    parser.add_argument('--cleanup', default=False, help='If True, does a cleanup after measurement')
    parser.add_argument('--arg1', help='Optional arguments to be passed to the tested function')
    parser.add_argument('--arg2', help='Optional arguments to be passed to the tested function')
    parser.add_argument('--arg3', help='Optional arguments to be passed to the tested function')
    parser.add_argument('--saveas', default='data', help='Optional argument of naming the .csv file, defaults to data')

    args = parser.parse_args()
    _ = Benchmarker(args)
    
