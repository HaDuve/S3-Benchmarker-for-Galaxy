import benchmarker
from argparse import Namespace

if __name__=='__main__':
    args =  Namespace(arg1='arg1',
                      arg2='arg2',
                      arg3='arg4',
                      cleanup=False,
                      function='debugPOSIX',
                      r=None,
                      warmup=False)
    b = benchmarker.Benchmarker(args)