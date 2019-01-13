# -*- coding: utf-8 -*-

'''
		IMPLEMENTED DATE : 06/01/2019

		SCOPE OF IMPLEMENTATION : For learning about Numby Arrays

		DEVELOPER NAME : M.BALAVIGNESH
'''

import numpy as np

# defining the 1-diementional array
# defining the matrix

vec_arr = [1,2,45,34]
line_1 = np.array(vec_arr)
print(line_1)


#Printing the matrix Array
met = [[1,2,3],[22,33,44]]
line_2 = np.array(met)
print(line_2)

#Zeros,Ones,eye

# printing the zeros matrix with tuple input

line_3 = np.zeros((3,4))
print(line_3)

#Printing the ones matrix with tuple input
line_4 = np.ones((2,4))
print(line_4)

#printing the diagnoal eyecan matrix array and distance is same intervel
line_5 = np.eye(4)
print(line_5)

#Random generation

line_6 = np.random.rand(5)
print(line_6)


#Random integer genartion
line_7 = np.random.randint(2,200,(5,5))
print(line_7)

#random integer genartion with negative and positive combination
line_8 = np.random.randn(2,10)
print(line_8)

# Numpy linspace creating the array based on the in between intervel values for given tuple input

line_9 = np.linspace(1,10)
print(line_9)

line_10 = np.linspace(1,10)
print(line_10)



myarr = [1,2,3,4,5,6,7,8]

nparr = np.array(myarr)

print(myarr)

#simple matrix creation



myarrlist = [[1,2,3],[2,3,4],[3,4,5]]
nparrlist = arr.array(myarrlist)
print(nparrlist)

#custom array creation using arange method


mycustom_arr = np.arange(0,15)
print(mycustom_arr)

setp_2_arr_range = np.arange(0,15,2)
print()
print("step 2 base array")
print(setp_2_arr_range)

#Custom array with zeros method

myarr = np.zeros(4)

print(myarr)

print()

my_matrix_3x3 = np.zeros((3,3))

print(my_matrix_3x3)


print()

my_one_custom = np.ones(6)
print(my_one_custom)

print()

my_one_matrix = np.ones((6,6))
print(my_one_matrix)


#for seeing the diemensions

print("diemension : " ,np.ndim(my_one_matrix))


#checking the array datatype

print("data type of an array : ",my_one_matrix.dtype)


#declaring the array type defaultly

my_dim = np.array((6,6),dtype = 'int64')

print(my_dim.dtype)

import numpy as np

line_ = np.linspace(0,1,20)
print(line_)
line_2 = np.linspace(0,1,20)
print(line_2)


arr,spacing = np.linspace(1,6,20,retstep=True)
print("spacing",spacing)

#Diagnol array creation

import numpy as np

line = np.eye(4)
print(line)


#Diagnoal changing using change the k- value (domain of diagnol changing)

line_2 = np.eye(6,k=-1)
print(line_2)


line_3 = np.eye(10,k=2)
print(line_3)

#Ranom array generation it prints the vlaue between 0 to 1 


import numpy as nf


line_1 = nf.random.rand(2)
print(line_1)

line_2 = nf.random.rand(2,4)
print(line_2)


#printing the random array from this start from negative to positive

line_3 = nf.random.randn(2,6)
print(line_3)

#Creating the random integer array values

line_4 = nf.random.randint(1,10)
print(line_4)


line_5 = nf.random.randint(1,100,(4,4))
print(line_5)

#seed value for dont repeat the same array 
nf.random.seed(43)
line_6 =nf.random.randint(1,100,20)
print(line_6)


