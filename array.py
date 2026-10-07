import numpy as np

#creating 1D array
arr1 = np.array([10, 20, 30, 40, 50])

# creating 2D array
arr2 = np.array([[1, 2, 3],[4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:")
print(arr2)

#Accesing 1st element of 1D array
print("First element of 1D array:", arr1[0])

#Acessing the last element of 1D array
print("Last element of 1D array:", arr1[-1])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)

print('2nd element on 1st row: ', arr[0, 1])

#Array Slicing
#1D array slicing
print("Sliced 1D array:", arr1[1:5])

#2D array slicing
print("Sliced 2D array:")
print(arr[1, 1:3])
print(arr[1, 1:4])
print("Sum of all elements in 1D array:", np.sum(arr1))
print("Sum of all elements in 2D array:", np.sum(arr))
