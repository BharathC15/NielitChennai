print("Nielit Chennai")

var_x <- "Hello"
cat("The class of var_x is ",class(var_x),"\n")
var_x <- 34.5
cat("Now the class of var_x is ",class(var_x),"\n")
var_x <- 27L
cat("Next the class of var_x becomes ",class(var_x),"\n")

# Conditional Statement
x<-10
if ( x > 0){
  print("x is a +ve Number")
}

x<--10
if ( x > 0){
  print("x is a +ve Number")
} else {
  print("x is a -ve Number")
}

x<-0
if ( x > 0){
  print("x is a +ve Number")
} else if (x < 0) {
  print("x is a -ve Number")
} else {
  print("x is equal to zero")
}
as.character()
# Get input from user
a<-as.integer(readline(prompt="Enter a number: "))
cat("The entered number is :",a)

#For loop
x <- c(2,5,3,9,8,11,6)
count <- 0
for (val in x) {
  if(val %% 2 == 0){
    count = count+1
  }
}
print(count)

# while
i <- 1
while (i < 6) {
  print(i)
  i = i+1
}

#Break Statement
x<-1:5
for (val in x){
  if (val == 3){
    break
  }
  print(val)
}

#Next Statement
x<-1:5
for (val in x){
  if (val == 3){
    next
  }
  print(val)
}

#Repeat Loop
x <- 1
repeat {
  print(x)
  x = x+1
  if (x == 6){
    break
  }
} 

#String handling
a <- 'Start and end with single quote'
b <- "Start and end with double quotes"
c <- "single quote ' in between double quotes"
d <- 'Double quotes " in between single quote'
cat(a,"\n",b,"\n",c,"\n",d)

print(paste(a,b,c,d,sep = "\n", collapse = " "))

a <- "Hello"
b <- 'How'
c <- "are you? "
print(paste(a,b,c))
print(paste(a,b,c, sep = "-"))
print(paste(a,b,c,collape="-"))

result <- format("Hello", width = 8, justify = "c")
print(result)

x<-"nieLit"
print(toupper(x))
print(tolower(x))
#Sub String
print(substr(x,2,4))

#Numeric Handling
print(format(23.123456789, digits = 9))
print(format(c(6, 13.14521), scientific = TRUE))

# Builtin Functions
print(seq(32,44)) 
print(mean(25:82)) 
print(sum(41:68))

#user defined function

myfunc<-function(a=10){
  print(a+1)
}

myfunc2 <- function(a, b) {
  print(a^2)
  print(a)
  print(b)
}

# Vectorized Function
maybe_square <- function(x){
  ifelse (x %% 2 == 0, x ** 2, x) 
} 

maybe_square2 <- function(x){
  if (x %% 2 == 0){
    x ** 2
    } 
  else {
    x 
    } 
} 
maybe_square2 <- Vectorize(maybe_square2) 