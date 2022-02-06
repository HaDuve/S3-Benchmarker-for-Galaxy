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
    s3_access_key = s3_con['s3_access_key']
    s3_secret_key = s3_con['s3_secret_key']
    
    work = config['Workflow']
    workflow = work['workflow']
    workflowargs = work['workflowargs']
    warmup = work['warmup']
    
    # workflow
    workflowlist = list(workflow.split(","))
    workflowargslist = list(workflowargs.split(","))
    i = 1
    while (workflowlist):        
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
        
        filename = "data"+next_function+str(i)
        
        #default namespace + config values
        args =  Namespace(arg1=arg1,
                        arg2=arg2,
                        arg3=arg3,
                        cleanup=False,
                        function=next_function,
                        r=None,
                        saveas=filename,
                        default_region=default_region,
                        s3_url=s3_url,
                        s3_access_key=s3_access_key,
                        s3_secret_key=s3_secret_key,
                        warmup=warmup)
        
        #TODO: workflow handling    
        workflow=workflow
        _ = benchmarker.Benchmarker(args)
        print('saved as: ', filename)
        i+=1