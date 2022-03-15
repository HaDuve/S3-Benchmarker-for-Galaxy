# Benchmarking Script
# Author: Hannes Duve

# Modules:
import functionsPOSIX, functionsS3

# Other Imports:
import argparse
import utils
import timer

class Benchmarker:
    def __init__(self, args):
        self.args = args
        if(self.args.r): self.args.r = int(self.args.r)
        print('args: ', self.args)

        # Modules:
        if ("POSIX" in self.args.function):
            self.fnManager = functionsPOSIX.FunctionManager(self.args)
        elif ("S3" in self.args.function):
            self.fnManager = functionsS3.FunctionManager(self.args)

        # If no module fits, print error:
        else: print("No suitable module found!")


    def run(self):
        data =  []
        if self.args.r:         # repetitive measurement with r preparations
            for _ in range(0, self.args.r):
                data.append(self.benchmark())
        else:
            data.append(self.benchmark())

        if (self.args.warmup == "True"):
                # delete the warmup run from data
                warmup = data.pop(0)
                print(f"Removing warmup time: {warmup}s run from data")
                data.append(self.benchmark())

        utils.save_file_as_csv(data, self.args)


    def report_time(self):
        # timing
        t = timer.Timer(name = self.args.function)

        # assume we dont get arg3 without arg2 etc.
        if(self.args.arg3 is not None):
            t.start()
            result = getattr(self.fnManager, self.args.function)(self.args.arg1, self.args.arg2, self.args.arg3)
            time = t.stop()
        elif(self.args.arg2 is not None):
            t.start()
            result = getattr(self.fnManager, self.args.function)(self.args.arg1, self.args.arg2)
            time = t.stop()
        elif(self.args.arg1 is not None):
            t.start()
            result = getattr(self.fnManager, self.args.function)(self.args.arg1)
            time = t.stop()
        else: #all args==None
            t.start()
            result = getattr(self.fnManager, self.args.function)()
            time = t.stop()


        # output handling
        print('result: ', result)
        print('time: ', time)
        return time


    def benchmark(self):
        """Calls the timing function with argument handling

        Args:
            args (str): the arguments given via the CLI
        Returns:
            data (list): list of data
        """
        utils.prepareBenchmark(self.args)
        time_data = self.report_time()
        utils.afterBenchmark(self.args)
        return time_data


if __name__=='__main__':
    """Argument handling and Data Saving"""
    parser = argparse.ArgumentParser(description="A tool to benchmark the time used for different functions")
    parser.add_argument('function', type=str, help='The function to be tested.'
                        , choices=['testS3','debugS3','lsS3','checksumS3','uploadS3','deleteS3','readS3','seekS3','testPOSIX','debugPOSIX','checksumPOSIX',
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
    Bench = Benchmarker(args)
    Bench.run()

