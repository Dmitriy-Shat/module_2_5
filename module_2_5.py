def get_matrix(n, m, value):
  matrix = []
  for i in range(n):
      column = []
      matrix.append(column)
      for j in range(m):
          column.append(value)
  print(matrix)

get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4,2,13)