# Basic of Datasets
rm(list=ls())

#Vector
apple <- c('red','green',"yellow")
print(apple)
print(class(apple))

v <- c("A"=1,"B"=2,"C"=3) 
print(v)
v["D"]=5
print(v)
names(v) <- c("l","m","n","o")
print(v)

l<-c(1:5)
print(l)
ll=l[c(TRUE,FALSE,TRUE,FALSE,TRUE)]
print(ll)
lm=l[l %% 2 == 0]
print(lm)
ln=l[-(1:3)] 
print(ln)

#Matrices
M = matrix( c('a','a','b','c'),nrow=2,ncol=2,byrow=TRUE)
print(M)
print(class(M))

M <- matrix(c(3:14),nrow=4,byrow=TRUE)
print(M)
N <- matrix(c(3:14),nrow=4,byrow=FALSE)
print(N)

rownames = c("row1", "row2", "row3", "row4")
colnames = c("col1", "col2", "col3")
P <- matrix(c(3:14),nrow = 4, byrow = TRUE,
            dimnames = list(rownames, colnames))
print(P)
print(P[1,3])
print(P[4,2])
print(P[2,])
print(P[,3])

matrix1<-matrix(c(3,9,-1,4,2,6),nrow=2)
print(matrix1)
matrix2<-matrix(c(5,2,0,9,3,4),nrow=2)
print(matrix2)
result<-matrix1+matrix2
print(result)

matrix1<-matrix(c(3,9,-1,4,2,6),nrow=2)
print(matrix1)
matrix2<-matrix(c(5,2,0,9,3,4),nrow=2)
print(matrix2)
result<-matrix1-matrix2
print(result)

matrix1<-matrix(c(3,9,-1,4,2,6),nrow=2)
print(matrix1)
matrix2<-matrix(c(5,2,0,9,3,4),nrow=2)
print(matrix2)
result<-matrix1*matrix2
print(result)

matrix1<-matrix(c(3,9,-1,4,2,6),nrow=2)
print(matrix1)
matrix2<-matrix(c(5,2,0,9,3,4),nrow=2)
print(matrix2)
result<-matrix1/matrix2
print(result)


#Arrays
a <- array(c('green','yellow'),dim = c(3,3,2))
print(a)
print(class(a))

vector1 <- c(5,9,3)
vector2 <- c(10,11,12,13,14,15)
column.names <- c("COL1","COL2","COL3")
row.names <- c("ROW1","ROW2","ROW3")
matrix.names <- c("Matrix1","Matrix2")
result <- array(c(vector1,vector2),
                dim = c(3,3,2),
                dimnames = list(row.names,
                                column.names,
                                matrix.names))
print(result)
print(result[3,,2])
print(result[1,3,1])

vector3 <- c(9,1,0)
vector4 <- c(6,0,11,3,14,1,2,6,9)
array2 <- array(c(vector1,vector2),
                dim = c(3,3,2))
matrix1 <- result[,,2]
matrix2 <- array2[,,2]
result <- matrix1+matrix2
print(result)

vector1 <- c(5,9,3)
vector2 <- c(10,11,12,13,14,15)
new.array <- array(c(vector1,vector2),
                   dim = c(3,3,2))
print(new.array)
result <- apply(new.array, c(1), sum)
print(result)



#Factors
apple_colors<-c('green','green','red','red','green') 
factor_apple<-factor(apple_colors) 
print(factor_apple) 
print(nlevels(factor_apple)) 

ff <- factor(LETTERS[1:4], 
            levels = rev(LETTERS[1:4]))
print(ff)
print(nlevels(ff))
print(summary(ff))

#List
list1 <- list(c(2,5,3),21.3,sin)
print(list1)

list_data <- list(c("Jan","Feb","Mar"),
                  matrix(c(3,9,5,1,-2,8), nrow = 2),
                  list("green",12.3))
names(list_data) <- c("1st Quarter", "A_Matrix",
                      "A Inner list")
print(list_data)

print(list_data$A_Matrix)
print(list_data$A_Matrix[1,2])
print(list_data[1])

list1 <- list(1,2,3)
list2 <- list("Sun","Mon","Tue")
merged.list <- c(list1,list2)
print(merged.list)


# Create the data frame.
BMI <- 	data.frame(
  gender = c("Male", "Male","Female"), 
  height = c(152, 171.5, 165), 
  weight = c(81,93, 78),
  Age = c(42,38,26)
)
print(BMI)

empdata<-data.frame(emp_id=c(1:5),
                    emp_name=c("KNC","RDS","SKJ",
                               "ME","NRR"),
                    salary=c(623.3,515.2,611.0,
                             729.0,843.25),
                    start_date=as.Date(c("2012-01-01", 
                                         "2013-09-23", 
                                         "2014-11-15", 
                                         "2014-05-11", 
                                         "2015-03-27")),   
                    stringsAsFactors = FALSE)
print(empdata)
str(empdata)
summary(empdata)

result<-data.frame(empdata$emp_name,empdata$salary)
print(result)
result <- empdata[1:2,]
print(result)
result <- empdata[c(3,5),]
print(result)
result <- empdata[,c(3,4)]
print(result)
result <- empdata[c(3,5),c(2,4)]
print(result)

df <- data.frame(a = 1:4, b = letters[1:4]) 
df2 <- data.frame(a = 5:7, b = letters[5:7]) 
print(rbind(df, df2)) 
df3 <- data.frame(c = 5:8, d = letters[5:8]) 
cbind(df, df3)

library(MASS)
merged.Pima <-merge(x = Pima.te,
                    y = Pima.tr,
                    by.x = c("bp", "bmi"), 
                    by.y=c("bp", "bmi"))
print(merged.Pima)

install.packages("reshape")
library(reshape)
library(MASS)
print(ships)
molten.ships <- melt(ships, 
                     id = c("type","year"))
print(molten.ships)
recasted.ship <- cast(molten.ships, 
                      type+year~variable,
                      sum)
print(recasted.ship)
