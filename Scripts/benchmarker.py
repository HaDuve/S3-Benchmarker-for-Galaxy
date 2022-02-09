# Benchmarking Script
# Author: Hannes Duve
import argparse
import utils
import functions
import timer

class Benchmarker:
    def __init__(self, args):
        self.args = args
        self.args.r = int(self.args.r)
        self.fnManager = functions.FunctionManager(self.args)

    def run(self):
        if self.args.r:         # repetitive measurement with r preparations
            data =  []
            utils.blockPrint()  # quiet mode
            for _ in range(0, self.args.r):
                data.append(self.benchmark())
            utils.enablePrint()
            if (self.args.warmup == "True"):
                print("cold round deleted from list!")
                data.pop(0)

        else:                   # single measurement (can still be repeated via -i with just 1 preparation)
            data = self.benchmark()

        print('args: ', self.args)
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
        return time

    def benchmark(self):
        """Calls the timing function with argument handling

        Args:
            args (str): the arguments given via the CLI
        Returns:
            data (list): list of data
        """
        utils.prepareBenchmark(self.args)
        data = self.report_time()
        utils.afterBenchmark(self.args)
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
    Bench = Benchmarker(args)
    Bench.run()

