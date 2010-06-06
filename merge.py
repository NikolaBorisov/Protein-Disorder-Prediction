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

def is_binary_from_filename(file_name):
    if (file_name.find("hnco") <> -1 or file_name.find("hncoca") <> -1):
        return True
    else:
        return False

# Given string "A107H" -> ["A", "107", "H"]
def split_res_num(res_num):
    i = 0
    while (i < len(res_num) and (not res_num[i].isdigit()) ):
        i += 1

    j = len(res_num) - 1
    while (j >= 0 and (not res_num[j].isdigit())):
        j -= 1

    return [res_num[:i], res_num[i:j+1], res_num[j+1:]]



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

def res_cmp(x, y):
    xs = split_res_num(x);
    ys = split_res_num(y);
    if (cmp(xs[0], ys[0]) == 0):
        return cmp(int(xs[1]), int(ys[1]))
    else:
        return cmp(xs[0], ys[0])

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
    acids.sort(res_cmp)
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
    is_binary = is_binary_from_filename(file_name)
    if (is_binary):
        print "%s is Binary" % file_name
    phs.append(ph)
    for d_line in data:
        if (is_binary):
            # from A107N-B108H  ->  res_nums[0] = A107N;   res_nums[1] = B108H
            res_nums = d_line[0].split("-")
        else:
            # from A107N-H  ->  res_num1 = A107N;  res_num2 = A107H
            dash_index = d_line[0].find("-")
            res_num1 = d_line[0][0:dash_index]
                       # A107                        + H
            res_num2 = d_line[0][0:(dash_index - 1)] + d_line[0][dash_index + 1:]
            res_nums = [res_num1, res_num2]
#        print "%s" % res_nums[0]
#        print split_res_num(res_nums[0])
        add_to(d1, res_nums[0], ph, d_line[1])
        add_to(d2, res_nums[1], ph, d_line[2])

print_to_file(d1, phs)
print_to_file(d2, phs)

