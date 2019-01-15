import numpy as np

#Numpy Operation
line_vec = [1,2,3,4,5,6,7]
line_10 = np.array(line_vec)
print(line_10)

result = line_10 * 2
print(result)

result_1 = line_10 + 4
print(result_1)

result_2 = line_10 - 2
print(result_2)

result_3 = line_10 /2 
print(result_3)


#Sin operation

result_4 = np.sin(line_10)
print(result_4)


#Sum operation
result_5 = np.sum(line_10)
print(result_5)


#Mean operation
result_6 = np.mean(line_10)
print(result_6)


#complex 2 diamentional operations
result_7 = np.array([[1,2],[2,4]])
result_8 = np.array([[23,34],[34,28]])

green = result_7 + result_8
print(green)


#performing the dot prdouct(matrix multiplication)

result_op = result_7.dot(result_8)
print(result_op)
