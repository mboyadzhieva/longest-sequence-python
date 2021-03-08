current = 0


def find_longest_sequence(n, m, rows, columns,  counter, matrix, visited):
    global current
    current = counter
    if visited[n][m]:
        return current
    else:
        visited[n][m] = True

    if m + 1 < columns:
        if matrix[n][m] == matrix[n][m + 1] and not visited[n][m + 1]:
            current += 1
            find_longest_sequence(n, m + 1, rows, columns, current, matrix, visited)

    if n + 1 < rows:
        if matrix[n][m] == matrix[n + 1][m] and not visited[n + 1][m]:
            current += 1
            find_longest_sequence(n + 1, m, rows, columns, current, matrix, visited)

    if m - 1 >= 0:
        if matrix[n][m] == matrix[n][m - 1] and not visited[n][m - 1]:
            current += 1
            find_longest_sequence(n, m - 1, rows, columns, current, matrix, visited)

    if n - 1 >= 0:
        if matrix[n][m] == matrix[n - 1][m] and not visited[n - 1][m]:
            current += 1
            find_longest_sequence(n - 1, m, rows, columns, current, matrix, visited)

    return current


def iterate_through_matrix(rows, columns, matrix, visited):
    longest_sequence = 0
    for i in range(0, rows):
        for j in range(0, columns):
            temp_longest_sequence = find_longest_sequence(i, j, rows, columns, 1, matrix, visited)
            if temp_longest_sequence > longest_sequence:
                longest_sequence = temp_longest_sequence
    print(longest_sequence)
