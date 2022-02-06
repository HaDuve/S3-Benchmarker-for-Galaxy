import benchmarker
import utils

if __name__=='__main__':
    fnstring = "test"
    argstring = ""
    b = benchmarker.Benchmarker(fnstring, argstring)
    
    # utils.checkPOSIX()
    # os.system("python benchmarker.py " + fnstring + argstring)