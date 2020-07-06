# Factor
# 1. Display the levels in the following vector
# v = c(1, 2, 3, 3, 4, NA, 3, 2, 4, 5, NA, 5)
# 2. Display the number of times each element has occured in the above vector

# 1. Print the levels in the vector
v <- c(1, 2, 3, 3, 4, NA, 3, 2, 4, 5, NA, 5)
print(factor(v))

# 2. Display the count of each elements
print(table(factor(v)))