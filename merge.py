#!/usr/bin/python
import sys


def ph_from_filename(file_name):
    #find the start and end index of the string containing the pH
    st = file_name.rindex('_') + 1
    end = file_name.index('.', st)

    # getting just the part we need
    tmpstr = file_name[st:end]
    tmpstrs = tmpstr.split('pt')
    # pull the numbers out and merge them back in a string
    ph_str = tmpstrs[0][2:] + "." + tmpstrs[1]
    #ph = float(ph_str)
    return ph_str

def readfile(file_name):
    lines = open(file_name).readlines()
    separated = []
    for line in lines:
        ar = line.split()
        if (len(ar) <> 3 or ar[0] == 'Assignment'):
            continue
        separated.append(ar)
    return separated

def add_to(d, acid, ph, w):
    if (not (acid in d)):
        d[acid] = {}
    d[acid][ph] = w

def print_to_file(d, phs):
    #f = open(out_file_name, 'w')
    #f.write("bla")

    # Header
    phs.sort()
    print "%15s" % ("Assignmens"), 
    for ph in phs:
        print "%8s" % (ph),
    print ""

    # Data
    acids = d.keys()
    acids.sort()
    #print acids

    for acid in acids:
        print "%15s" % (acid),
        for ph in phs:
            
            if (ph in d[acid]):
                w = d[acid][ph]
                print "%8.3f" % (float(w)),
            else:
                print "%8s" % ("-"),

        print ""





file_names = sys.argv[1:]

d1 = {}
d2 = {}
phs = []

for file_name in file_names:
    data = readfile(file_name)
    ph = ph_from_filename(file_name)
    phs.append(ph)
    for d_line in data:
        add_to(d1, d_line[0], ph, d_line[1])
        add_to(d2, d_line[0], ph, d_line[2])

print_to_file(d1, phs)
print_to_file(d2, phs)

