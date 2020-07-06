#List:
#1. Create a List containing a vector,a string, a number, a vector, a matrix and a list
#2. Remove the second element from the list
#3. Count the number of objects in the list
#4. Add a new element name="abc" to the list

# 1. Create a list
df <- list(c(1,2,3),"Hello",123,c("how","are","you"),matrix(1:9,byrow=TRUE),list("testing","this","software"))
print(df)

# 2. Remove the second element
df[[2]] <- NULL
print(df)

# 3. Count the number of objects in the list
paste("The number of objects are ",length(df))

# 4. Add a new element name="abc"
df["name"]="abc"
print(df)