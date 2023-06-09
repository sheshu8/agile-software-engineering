grid=[
  [5,3,2,1,4,6,7,8,5],
  [1,4,6,7,8,9,2,5,3],
  [7,8,9,5,3,1,4,6,2],
  [2,3,4,5,6,7,8,9,1],
  [9,1,8,7,6,5,4,3,2],
  [8,3,4,5,6,9,1,2,3],
  [1,1,1,1,1,1,2,2,2],
  [6,7,8,1,2,3,4,5,6],
  [9,8,1,3,4,5,6,1,2],
]
def check_row(grid,row_no,element):
  for column in range(9):
    print(grid[row_no][column])
    if grid[row_no][column]==element:
      return True
  return False
print(check_row(grid,0,5))


def check_column(grid,column,element):
  for row in range(9):
    print(grid[column][row])
    if grid[column][row]==element:
      return True
  return False
print(check_column(grid,0,5))


def check_diagonal(grid,i,element):
  for i in range(9):
      print(grid[i][i])
      if grid[i][i]==element:
        return True
  return False
print_diagonal(grid)
