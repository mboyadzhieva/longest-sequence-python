import sys
import argparse
import numpy
import pathlib


def main():
    arguments = get_arguments()
    for t in arguments.tests:
        run_test(t)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tests", type=pathlib.Path, nargs="+")
    args = parser.parse_args()
    return args


def run_test(test_name):
    file = open(test_name, 'r')
    lines = file.read().split("\n")
    rows = int(lines[0].split()[0])
    columns = int(lines[0].split()[1])
    matrix = []
    visited = numpy.full((rows, columns), False, dtype=bool)

    for line in lines[1:]:
        matrix.append(line.split(" "))

    iterate_through_matrix(rows, columns, matrix, visited)


def iterate_through_matrix(rows, columns, matrix, visited):
    longest_sequence = 0
    for i in range(0, rows):
        for j in range(0, columns):
            temp_longest_sequence = find_longest_sequence(rows, columns, i, j, 1, matrix, visited)
            if temp_longest_sequence > longest_sequence:
                longest_sequence = temp_longest_sequence
    print(longest_sequence)


current = 0


def find_longest_sequence(rows, columns, n, m, counter, matrix, visited):
    global current
    current = counter

    if visited[n][m]:
        return current
    else:
        visited[n][m] = True

    if m + 1 < columns:
        if matrix[n][m] == matrix[n][m + 1] and not visited[n][m + 1]:
            current += 1
            find_longest_sequence(rows, columns, n, m + 1, current, matrix, visited)

    if n + 1 < rows:
        if matrix[n][m] == matrix[n + 1][m] and not visited[n + 1][m]:
            current += 1
            find_longest_sequence(rows, columns, n + 1, m, current, matrix, visited)

    if m - 1 >= 0:
        if matrix[n][m] == matrix[n][m - 1] and not visited[n][m - 1]:
            current += 1
            find_longest_sequence(rows, columns, n, m - 1, current, matrix, visited)

    if n - 1 >= 0:
        if matrix[n][m] == matrix[n - 1][m] and not visited[n - 1][m]:
            current += 1
            find_longest_sequence(rows, columns, n - 1, m, current, matrix, visited)

    return current


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()
