#!/usr/bin/python
import sys

# sudo easy_install xlwt

import xlwt
from tempfile import TemporaryFile
from xlwt import Workbook

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
                num = int(d[0].strip())
                val = int(d[9].strip())
                self.add(num, is_disordered1(val))

    def parse2(self, filename):
        f = open(filename, "r")
        str = f.read()
        lines = str.split('\n')
        for line in lines:
            d = line.split('\t')
            if len(d) == 2:
                num = int(d[0]) + mismatch_fix
                val = float(d[1])
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


def compare(nmr1, nmr2):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    i = 1
    begin_dis_seq1 = -1
    begin_dis_seq2 = -1
    
    seq_string1 = ""
    seq_string2 = ""
    
    while i <= max(nmr1.get_size(), nmr2.get_size()):
        if nmr1.is_present(i):
            if begin_dis_seq1 == -1 and nmr1.is_dis(i):
                begin_dis_seq1 = i
        
            if begin_dis_seq1 <> -1 and not nmr1.is_dis(i):
                seq_string1 += "MD Disorder interval: " + str(begin_dis_seq1) + " - " + str(i-1) + "\n"
                begin_dis_seq1 = -1
                
        if nmr2.is_present(i):
            if begin_dis_seq2 == -1 and nmr2.is_dis(i):
                begin_dis_seq2 = i
        
            if begin_dis_seq2 <> -1 and not nmr2.is_dis(i):
                seq_string2 += "ncSPC Disorder interval: " + str(begin_dis_seq2) + " - " + str(i-1) + "\n"
                begin_dis_seq2 = -1

    
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
    
    if begin_dis_seq1 <> -1: 
        seq_string1 += "MD Disorder interval: " + str(begin_dis_seq1) + " - " + str(nmr1.get_size()) + "\n"
    if begin_dis_seq2 <> -1:
        seq_string2 += "ncSPC Disorder interval: " + str(begin_dis_seq2) + " - " + str(nmr2.get_size()) + "\n"
    
    data_row = sheet1.row(thr3+1)
    data_row.write(0, thr3)
    
    len_of_dis = tp+fn 
    print "Length of Disorder: ", len_of_dis 
    data_row.write(1, len_of_dis)
    
    hits = tp+tn
    print "Hits: ", hits
    data_row.write(2, hits)
    
    print "True Positive: ", tp
    data_row.write(3, tp)
    print "True Negative: ", tn
    data_row.write(4, tn)
    print "False Positive: ", fp
    data_row.write(5, fp)
    print "Flase Negative: ", fn
    data_row.write(6, fn)
    
    if tp+fp<>0:
         accuracy = float(tp)/float(tp+fp)
    else:
        accuracy = "N/A"
    print "Accuracy: ", accuracy
    data_row.write(7, accuracy)
           
    if tp+fn<>0:
        coverage = float(tp)/float(tp+fn)
    else:
        coverage = "N/A"
    print "Coverage = TP rate: ", coverage
    data_row.write(8, coverage)
    
    if fp+tn<>0:    
        fp_rate = float(fp)/float(fp+tn)
    else:
        fp_rate = "N/A"
    print "FP Rate: ", fp_rate
    data_row.write(9, fp_rate)
    
   
    if tn+fn<>0: 
        accuracy_ordered = float(tn)/float(tn+fn)
    else:
        accuracy_ordered = "N/A"
    print "Accuracy Ordered: ", accuracy_ordered
    data_row.write(10, accuracy_ordered)
        
    if tp+fp<>0:
        coverage_ordered = float(tn)/float(tn+fp)
    else:
        coverage_ordered = "N/A"
    print "Coverage Ordered: ", coverage_ordered
    data_row.write(11, coverage_ordered)
    
    print seq_string1, seq_string2
    
    data_row.write(12, seq_string1)
    data_row.write(13, seq_string2)
    
    
if len(sys.argv) <> 5:
    usage()

#thr3 = int(sys.argv[3])
mismatch_fix = int(sys.argv[3])

# some hacky code to get the protein number from the file name
f = sys.argv[1]
ar = f.split("/")
protein_num = ar[len(ar)-1].split(".")[0]

book = Workbook()
sheet1 = book.add_sheet(protein_num)
header_row = sheet1.row(0)
header_row.write(0, "\\")
header_row.write(1, "Length of Disorder")
header_row.write(2, "Hits")
header_row.write(3, "True Positives")
header_row.write(4, "True Negative")
header_row.write(5, "False Positives")
header_row.write(6, "False Negatives")
header_row.write(7, "Accuracy")
header_row.write(8, "Coverage/TP Rate")
header_row.write(9, "FP Rate")
header_row.write(10, "Accuracy Ordered")
header_row.write(11, "Coverage Ordered")



nmr2 = NMR()
nmr2.parse2(sys.argv[2])


for th in range(10):
    thr3 = th
    print "################################# ", thr3 

    nmr1 = NMR()
    nmr1.parse1(sys.argv[1])
    
    compare(nmr1, nmr2)
    

book.save(protein_num + ".xls")
book.save(TemporaryFile())



