# A simple R program to display the n Fibonnaci terms
a<-0
b<-1
fib<-0
{
n<-readline(prompt="Enter the number of terms :")
n <- as.integer(n)
}
i=2
print("-------------")
print(a)
print(b)
while (i<n){
    fib<-a+b
    a<-b
    b<-fib
    i<-i+1
    print(fib)
} 