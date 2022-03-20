# 1.st step https://www.live2tech.com/merge-multiple-csv-files-combine-one-large-csv-file/
# this py deletes every header bar the first one

with open("benchmarkdata.csv", "r") as f:
    lines = f.readlines()
with open("nh.csv", "w") as f:
    headerline = True
    for line in lines:
        if (headerline):
            headerline=False
            f.write(line)
            continue
        if line.strip("\n") != "Operation,Time, Argument1, Argument2, Argument3":
            f.write(line)
