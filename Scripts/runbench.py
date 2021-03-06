import benchmarker
import configparser
from argparse import Namespace

if __name__=='__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    #parsing config
    s3_con = config['S3 Connection']
    default_region = s3_con['default_region']
    s3_url = s3_con['s3_url']

    work = config['Workflow']
    workflow = work['workflow']
    workflowargs = work['workflowargs']
    repetitions = work['repetitions']
    warmup = work['warmup']
    cleanup = work['cleanup']

    log = config['Log']
    runs = log['runs']

    # workflow
    workflowlist = list(workflow.split(","))
    workflowargslist = list(workflowargs.split(","))
    numRuns = int(runs)
    while (workflowlist):
        numRuns+=1
        next_function = workflowlist.pop(0)
        next_arglist = workflowargslist.pop(0)
        next_arglist = list(next_arglist.split(" "))
        if (next_arglist):
            if len(next_arglist) == 1:
                if (next_arglist[0] == ""):
                    arg1 = arg2 = arg3 = None
                else:
                    arg1 = next_arglist[0]
                    arg2 = None
                    arg3 = None
            if len(next_arglist) == 2:
                arg1 = next_arglist[0]
                arg2 = next_arglist[1]
                arg3 = None
            if len(next_arglist) == 3:
                arg1 = next_arglist[0]
                arg2 = next_arglist[1]
                arg3 = next_arglist[2]

        filename = f"time_{str(numRuns)}_{next_function}"

        #default namespace + config values
        args =  Namespace(arg1=arg1,
                        arg2=arg2,
                        arg3=arg3,
                        cleanup=cleanup,
                        function=next_function,
                        r=repetitions,
                        saveas=filename,
                        default_region=default_region,
                        s3_url=s3_url,
                        warmup=warmup)
        Bench = benchmarker.Benchmarker(args)
        Bench.run()
        print('saved as: ', f"\"{filename}.csv\"")
        config['Log']['runs'] = str(numRuns)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
