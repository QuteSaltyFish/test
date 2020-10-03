import numpy as np
import os
if __name__ == "__main__":
    filebase = "origin_rules"
    filelists = os.listdir(filebase)
    for filename in filelists:
        filename2 = os.path.join(filebase,filename)
        outfile = os.path.join('result',filename.split('.')[0]+'.list')
        f =  open(filename2, 'r')
        o = open(outfile, 'w')
        for line in f.readlines():
            if line.startswith('#'):
                o.write(line)
                continue
            o.write('IP-CIDR,'+line.strip()+',no-resolve\n')
        f.close()
        o.close()