# 2.1
numbers = list(range(21))
print(numbers)

# 2.2
def squareList(numbers):
    return [x**2 for x in numbers]
squares = squareList(numbers)
print(squares)

# 2.3
def first_fifteen_elements(squares):
    return squares[:15]
print(first_fifteen_elements(squares))
# SyntaxError: invalid syntax in line 10. Since I only wrote return [:15], I didn't specify that I was trying to splice the squares list.

# 2.4
def every_fifth_element(squares):
    return squares[4::5]
print(every_fifth_element(squares))

# 2.5
def fancy_function(squares):
    return squares[-3::-3]
print(fancy_function(squares))
# When I first ran this section, it only printed [400] because I sliced the list as [:-3:-3] which only kept the last 3 elements instead of excluding them.

# 3.1
matrix = []
def create_2d_list():
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix
matrix = create_2d_list()
print(matrix)
#  I had a syntax error when I tried to run 'for i in range 5:' because the 5 should have been in parantheses.
# Another error I got was having it return <function create_2d_list at 0x1030ad940> instead of the matrix. This was because I forgot to call create_2d_list when declaring the matrix variable.  

# 3.2
def modified_2d_list(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = '?'
    return matrix
modified = modified_2d_list(matrix)
print(modified)
# My code printed 'None' because I forgot to include a return statement. I fixed this by adding the line 'return matrix'

# 3.3 
def sum_non_question_elements(modified):
    sum = 0
    for i in range(5):
        for j in range(5):
            if modified[i][j] != '?':
                sum += matrix[i][j]
    return sum 
print(sum_non_question_elements(modified))