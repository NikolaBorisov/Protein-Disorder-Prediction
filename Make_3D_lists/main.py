#!/usr/bin/python
import sys


def is_binary_from_filename(file_name):
    if (file_name.find("hnco") <> -1 or file_name.find("hncoca") <> -1):
        return True
    else:
        return False

def split_label(label):
    return label.split("-")

# Given string "A107H" -> ["A", "107", "H"]
def split_res_num(res_num):
    i = 0
    while (i < len(res_num) and (not res_num[i].isdigit()) ):
        i += 1

    j = len(res_num) - 1
    while (j >= 0 and (not res_num[j].isdigit())):
        j -= 1

    return [res_num[:i], res_num[i:j+1], res_num[j+1:]]

def get_num_from_first_label(label):
    labels = split_label(label)
    ar = split_res_num(labels[0])
    return ar[1]


def readfile(file_name):
    lines = open(file_name).readlines()
    separated = []
    for line in lines:
        ar = line.split()
        if (len(ar) == 0 or ar[0] == 'Assignment'):
            continue
        separated.append(ar)
    return separated

def output_line(l13, l2):
    ls13 = split_label(l13[0])
    x = split_res_num(ls13[0])
    out_label1 = ls13[0]
    out_label2 = split_label(l2[0])[0]
    out_label3 = x[0] + x[1] + split_label(l13[0])[1]

    print out_label1 + "-" + out_label2 + "-" + out_label3 , "\t", l13[1], "\t",l2[1], "\t", l13[2]


data13 = readfile(sys.argv[1])
data2 = readfile(sys.argv[2])

#print split_res_num(data13[0][0])

for l13 in data13:
    for l2 in data2:
        n13 = int(get_num_from_first_label(l13[0]))
        n2 = int(get_num_from_first_label(l2[0]))
        if (n13 == n2):
            output_line(l13, l2)
        if (n13 == (n2 - 1) ):
            output_line(l13, l2)

        
