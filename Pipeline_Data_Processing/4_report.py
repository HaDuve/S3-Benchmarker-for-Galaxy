import os
from decimal import Decimal
import statistics

ROUNDTODIGIT = 5
FOLDERS = ["Systems","Operations","SystemsFilesize","SystemsFiletype","OperationsFiletypes"]
LATEXFORMAT = True
SEPERATORSTRING = "----------------------------------------------------------------\n"

with open("RESULTS.csv", "w") as f_out:
    if(LATEXFORMAT):
        f_out.write("NAME \t& max \t& min \t&avg \t&median \t&stddev\n")
        f_out.write(SEPERATORSTRING)
    for folder in FOLDERS:
        for file in os.listdir(os.path.join(os.getcwd(),folder)):
            with open(os.path.join(os.getcwd(),folder,file), "r") as f:
                lines = f.readlines()
                header = True
                decimals = []
                print(file)
                for line in lines:
                    if header:
                        header = False
                        continue
                    # find first comma and take the next 8 characters as a float into a list
                    op_end_index = line.find(",")
                    benchcase = line[op_end_index + 1:op_end_index+9]
                    decimals.append(round(Decimal(benchcase),ROUNDTODIGIT))

                max_value = max(decimals)
                min_value = min(decimals)

                mean_value = 0 if len(decimals) == 0 else sum(decimals)/len(decimals)
                mean_value = round(mean_value, ROUNDTODIGIT)

                median_value = statistics.median(decimals)
                median_value = round(median_value, ROUNDTODIGIT)

                stddev_value = statistics.stdev(decimals)
                stddev_value = round(stddev_value, ROUNDTODIGIT)

                outputstring = (file+":"                  +"\t"
                                +" max_value: "+ str(max_value)         +"\t"
                                +" min_value: "+ str(min_value)         +"\t"
                                +" avg_value: "+ str(mean_value)        +"\t"
                                +" median_value: "+ str(median_value)   +"\t"
                                +" stddev_value: "+ str(stddev_value)   +"\t"
                                + "\n")

                if(LATEXFORMAT):
                    outputstring = (file+"\t"
                                +"&"+ str(max_value)+"\t"
                                +"&"+ str(min_value)+"\t"
                                +"&"+ str(mean_value)+"\t"
                                +"&"+ str(median_value)+"\t"
                                +"&"+ str(stddev_value)+"\t"
                                + "\\\\ \n")

                f_out.write(outputstring)

        f_out.write(SEPERATORSTRING)

