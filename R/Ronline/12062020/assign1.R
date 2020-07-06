# Array
# 1. Create an array A containing 5 elements of even numbers starting from 10
# 2. Create an array B containing squares of A
# 3. Create an array C which is the sum of array A and array B
# 4. Create an array D which contains first 2 elements of array A, second 2 elements of array B and last element of array C

# 1. Create an array A containing 5 element of even numbers starting from 10
A<-array(c(seq(10, 18, 2)))
print(A)

# 2. Create an array B Containing Squares of A
B<-A^2
print(B)

#3. Create an array C which is the sum of array A and array B
C<-A+B
print(C)

# 4. Create an array D which contains first 2 elements of array A, second 2 elements of array B and last element of array C
D<-array(c(A[c(1,2)],B[c(3,4)],C[5]))
print(D)

# DataFrame
# 1. create a DataFrame ABC containing the array A, B, C, D
# 2. Display only the (2,3) row and (2,3) column of ABCD DataFrame

# 1. Create a DataFrame ABC containing the array A,B,C,D
ABCD<-data.frame(A,B,C,D)
print(ABCD)

# 2. Display only the (2,3) row and (2,3) column
print(ABCD[c(2,3),c(2,3)])