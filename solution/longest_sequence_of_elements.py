import argparse
import numpy

parser = argparse.ArgumentParser()
parser.add_argument("--t1", required=True)
parser.add_argument("--t2", required=False)
parser.add_argument("--t3", required=False)
parser.add_argument("--t4", required=False)
args = parser.parse_args()

current = 0
rows = 0
columns = 0
matrix = []
visited = []


def find_longest_sequence(n, m, counter):
    global current
    current = counter

    if visited[n][m]:
        return current
    else:
        visited[n][m] = True

    if m + 1 < columns:
        if matrix[n][m] == matrix[n][m + 1] and not visited[n][m + 1]:
            current += 1
            find_longest_sequence(n, m + 1, current)

    if n + 1 < rows:
        if matrix[n][m] == matrix[n + 1][m] and not visited[n + 1][m]:
            current += 1
            find_longest_sequence(n + 1, m, current)

    if m - 1 >= 0:
        if matrix[n][m] == matrix[n][m - 1] and not visited[n][m - 1]:
            current += 1
            find_longest_sequence(n, m - 1, current)

    if n - 1 >= 0:
        if matrix[n][m] == matrix[n - 1][m] and not visited[n - 1][m]:
            current += 1
            find_longest_sequence(n - 1, m, current)

    return current


def iterate_through_matrix():
    longest_sequence = 0
    for i in range(0, rows):
        for j in range(0, columns):
            temp_longest_sequence = find_longest_sequence(i, j, 1)
            if temp_longest_sequence > longest_sequence:
                longest_sequence = temp_longest_sequence
    print(longest_sequence)


def do_test(test_name):
    global rows
    global columns
    global matrix
    global visited

    file = open(test_name, 'r')
    lines = file.read().split("\n")
    rows = int(lines[0].split()[0])
    columns = int(lines[0].split()[1])
    matrix = []
    visited = numpy.full((rows, columns), False, dtype=bool)

    for line in lines[1:]:
        matrix.append(line.split(" "))

    iterate_through_matrix()


def main():
    if args.t1:
        do_test(args.t1)
    if args.t2:
        do_test(args.t2)
    if args.t3:
        do_test(args.t3)
    if args.t4:
        do_test(args.t4)


if __name__ == "__main__":
    main()
