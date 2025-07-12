'''Imagine you are helping a student with their mathematics homework which involves a lot of problems based on matrix addition. You decide to write a program to automate the task of adding two matrices, which would make the homework a breeze!

Write a program to add two matrices. The program should:

Prompt the user to enter the dimensions of the matrices (assume both matrices have the same dimensions).

Accept the elements of the two matrices from the user.

Display the two matrices.

Add the two matrices.

Print the resultant matrix.

Kindly check the sample test case for input and output format.

Input Format

2 2
1 2
3 4
5 6
7 8

Constraints

NA

Output Format

First Matrix:
1 2
3 4
Second Matrix:
5 6
7 8
Sum of the two matrices is:
6 8
10 12

Sample Input 0

2 2
1 2
3 4
5 6
7 8
Sample Output 0

First Matrix:
1 2 
3 4 
Second Matrix:
5 6 
7 8 
Sum of the two matrices is:
6 8 
10 12
Sample Input 1

1 1
6
8
Sample Output 1

First Matrix:
6
Second Matrix:
8
Sum of the two matrices is:
14
'''
m,n=map(int,input().split())


mat1=[]
mat2=[]
for i in range(m):
    row=list(map(int,input().split()))
    mat1.append(row)
print("First Matrix:")
for row in mat1:
    print(' '.join(map(str,row)))

for i in range(m):
    row=list(map(int,input().split()))
    mat2.append(row)
print("Second Matrix:")
for row in mat2:
    print(' '.join(map(str,row)))

mat3=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(mat1[i][j]+mat2[i][j])
    mat3.append(row)
print("Sum of the two matrices is:")
for row in mat3:
    print(' '.join(map(str,row)))

        




        
