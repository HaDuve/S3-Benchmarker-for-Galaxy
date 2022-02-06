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
    result_path = work['result_path']
    warmup = work['warmup']
    
    #default namespace
    args =  Namespace(arg1=None,
                      arg2=None,
                      arg3=None,
                      cleanup=False,
                      function='debug',
                      r=None,
                      saveas='data',
                      default_region=default_region,
                      s3_url=s3_url,
                      s3_access_key=s3_access_key,
                      s3_secret_key=s3_secret_key,
                      workflow=workflow,
                      result_path=result_path,
                      warmup=warmup)
    _ = benchmarker.Benchmarker(args)