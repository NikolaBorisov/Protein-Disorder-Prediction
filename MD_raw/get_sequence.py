#!/usr/bin/python
import sys

def readfile(filename):
        """
          Just read-in the [filename] and return a list of strings
        """
        star_data=open(filename).readlines()
        raw_data=[] 
        separated=[]
        for p in star_data[0:]: 
                raw_data.append(p[:-1])
        for p in range (len(raw_data)):
                separated.append(raw_data[p].split())
        return separated
        
def usage():
        """
            How to execute the script
        """
        print "Usage: ./get-assignments-pH3.py <asyn_pH3_bmrb_16342.shifts> <type: 1 - hsqc, 2 - hncoca, 4 - hnco>"
        

data = readfile(sys.argv[1])
sequence = {}
for line in data:
  if line:
    resnum = line[0]
    resname = line[1]
    sequence = resname.strip()
    sys.stdout.write(sequence)
print ""
print resnum


            
