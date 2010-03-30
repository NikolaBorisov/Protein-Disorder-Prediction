#!/usr/bin/python
import sys

# test comment

thr1 = 0.066
thr2 = -0.052

def is_disordered2(val):
    if val <= thr1 and val >= thr2:
        return True
    else:
        return False

def is_disordered1(val):
    if val >= thr3:
        return True
    else:
        return False


#rename to Protein
class NMR:
    def __init__(self):
        self.data = {}
        self.size = 0

    def parse1(self, filename):
        f = open(filename, "r")
        str = f.read()
        lines = str.split('\n')
        for line in lines:
            d = line.split('\t')
            if len(d) == 11:
#                print len(d), d[0], d[9]
                num = int(d[0].strip())
                val = int(d[9].strip())
                self.add(num, is_disordered1(val))

#        print self.data

    def parse2(self, filename):
        f = open(filename, "r")
        str = f.read()
        lines = str.split('\n')
        for line in lines:
            d = line.split('\t')
            if len(d) == 2:
                num = int(d[0]) + mismatch_fix
                val = float(d[1])
#               print num, val, is_disordered2(val)
                self.add(num, is_disordered2(val))


    # adding number and ordered or disordered
    def add(self, num, is_disordered):
        if num in self.data:
            raise Exception("duplicate residue number")
        self.data[num] = is_disordered
        self.size = max(self.size, num)

    def get_size(self):
        return self.size

    def is_present(self, num):
        if num in self.data:
            return True
        else:
            return False

    def is_dis(self, num):
        if not self.is_present(num):
            raise Exception("no data for this number")
        return self.data[num]


# check num of arguments

def usage():
    print "Usage: ./main.py <file1> <file2> thr1 mismatch_fix"

if len(sys.argv) <> 5:
    usage()

thr3 = int(sys.argv[3])
mismatch_fix = int(sys.argv[4])

nmr1 = NMR()
nmr1.parse1(sys.argv[1])

nmr2 = NMR()
nmr2.parse2(sys.argv[2])

def compare(nmr1, nmr2):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    i = 1
    while i <= max(nmr1.get_size(), nmr2.get_size()):
        if nmr1.is_present(i) and nmr2.is_present(i):
            if nmr1.is_dis(i) and nmr2.is_dis(i):
                tp += 1
            elif nmr1.is_dis(i) and not nmr2.is_dis(i):
                fp += 1
            elif not nmr1.is_dis(i) and nmr2.is_dis(i):
                fn += 1
            elif not nmr1.is_dis(i) and not nmr2.is_dis(i):
                tn += 1
            else:
                print "SHIT"
        i += 1

    print "True Positive: ", tp
    print "True Negative: ", tn
    print "False Positive: ", fp
    print "Flase Negative: ", fn


compare(nmr1, nmr2)



