import argparse
from longest_sequence import iterate_through_matrix
import numpy

parser = argparse.ArgumentParser()
parser.add_argument("--t1", required=True)
parser.add_argument("--t2", required=False)
parser.add_argument("--t3", required=False)
parser.add_argument("--t4", required=False)
args = parser.parse_args()


def do_test(test_name):
    file = open(test_name, 'r')
    lines = file.read().split("\n")
    rows = int(lines[0].split()[0])
    columns = int(lines[0].split()[1])
    matrix = []
    visited = numpy.full((rows, columns), False, dtype=bool)
    for line in lines[1:]:
        matrix.append(line.split(" "))
    iterate_through_matrix(rows, columns, matrix, visited)


if args.t1:
    do_test(args.t1)
if args.t2:
    do_test(args.t2)
if args.t3:
    do_test(args.t3)
if args.t4:
    do_test(args.t4)
