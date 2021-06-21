import glob, os
os.chdir("./IMG")
f = open("../trainval.txt", "w")
for file in glob.glob("*.txt"):
    # Using readlines()
    file1 = open(file, 'r')
    data = file1.readlines()[0].split()
    cx = float(data[1]) * 320
    cy = float(data[2]) * 160
    width = float(data[3]) * 320
    height = float(data[4]) * 160
    xmin = cx - width / 2
    ymin = cy - height / 2
    xmax = cx + width / 2
    ymax = cy + height / 2
    f.write("./IMG/{0}.jpg {1},{2},{3},{4},0\n".format(file.split('.')[0], int(xmin), int(ymin), int(xmax), int(ymax) ))
f.close()