# Benchmarking Script 
# Author: Hannes Duve
import argparse
import utils
import functions

def report_time(fn, arg1 = None, arg2 = None, arg3 = None, iter=1):
    """Reports the time used to execute function "fn"

    Args:
    
        fn (function): Name of the function used as a string
        iter (int, optional): Number of executions. Defaults to 1
    Returns:
        [time, average]: List of datapoints, timed operations and their average over a (optionally modified) number of iterations
    """
    import timeit
    
    
    if(iter==None): iter = 1
    
    #debug
    print('fn: ', fn)
    
    
    argstr = ""
    if(args.arg1): argstr = str(args.arg1)
    if(args.arg1 and args.arg2): argstr = str(args.arg1) + ',' + str(args.arg2)
    if(args.arg1 and args.arg2 and args.arg3): argstr = str(args.arg1) + ',' + str(args.arg2) + ',' + str(args.arg3)
    
    # timing
    time = timeit.timeit(fn + "("+argstr+")", setup="from functions import " + fn + "; gc.enable()", number=iter)

    
    # output handling    
    print(fn + ": " + str(round(time,3)) + " sec for " + str(iter) + " iterations")
    average = time/iter
    averagestr = str(round(time/iter,9))
    print('average: ' + averagestr + " sec")
    return [time, average]


def benchmark(args): 
    """Calls the timing function with argument handling

    Args:
        args (str): the arguments given via the CLI
    Returns:
        data (list): list of data
    """
    utils.prepareBenchmark(args)
    
    data = report_time(args.function, args.arg1, args.arg2, args.arg3,args.i)
    
    utils.afterBenchmark(args)
    
    return data


if __name__=='__main__':
    """Argument handling and Data Saving"""
    parser = argparse.ArgumentParser(description="A tool to benchmark the time used for different functions")    
    parser.add_argument('function', type=str, help='The function to be tested.'
                        , choices=['test','checksumS3','uploadS3','deleteS3','readS3','seekS3','checksumPOSIX',
                                   'uploadPOSIX','deletePOSIX','readPOSIX','seekPOSIX']
                        )    
    # optionals    
    parser.add_argument('-i', type=int, help='an integer for the number i of repetitions of the function-execution (without preparation)')
    parser.add_argument('-r', type=int, help='repeat the measurement for r times to get a table of data (with preparation)')
    parser.add_argument('--cleanup', default=False)
    parser.add_argument('--arg1', help='optional arguments to be passed to the tested function')
    parser.add_argument('--arg2', help='optional arguments to be passed to the tested function')
    parser.add_argument('--arg3', help='optional arguments to be passed to the tested function')

    args = parser.parse_args()
    print('args: ', args)
    
    if args.r:          # repetitive measurement with preparation        
        data =  []        
        utils.blockPrint()    # quiet mode      
        for i in range(0,args.r):
            data.append(benchmark(args))        
        utils.enablePrint()
            
    else:               # single measurement
        data = benchmark(args)
        
    
    # print('data: ', data)
    utils.save_file_as_csv(data, args)
    
