# Normal Distribution

# dnorm
x=seq(-4,4,length=200)
y=dnorm(x,mean=0,sd=1)
plot(x,y,type="l",lwd=2,col="red")


# pnorm
x <- seq(-10,10,by = .2)
y <- pnorm(x, mean = 2.5, sd = 2)
plot(x,y,type="l",lwd=2,col="red")

# qnorm
x <- seq(0, 1, by = 0.02)
y <- qnorm(x, mean = 2, sd = 1)
plot(x,y)

# rnorm
y <- rnorm(50)
hist(y, main = "Normal Distribution")

library(distr)
X<-Norm(mean=100,sd=15)
plot(X)

# Standard Deviation
x=seq(-8,8,length=500)
y1=dnorm(x,mean=0,sd=1)
plot(x,y1,type="l",lwd=2,col="red")
y2=dnorm(x,mean=0,sd=2)
lines(x,y2,type="l",lwd=2,col="blue")
legend("topright",c("sigma=1","sigma=2"),
       col=c("red","blue"),lty = c(1,1))


# Area under the Probability Density Function
x=seq(70,130,length=200)
y=dnorm(x,mean=100,sd=10)
plot(x,y,type="l",lwd=2,col="red")
x=seq(70,90,length=100)
y=dnorm(x,mean=100,sd=10)
polygon(c(70,x,90),c(0,y,0),col="gray")

#Calculate the shaded area: 
pnorm(90,mean=100,sd=10)

# Test for Skewness and Kurtosis
points = c(452, 437, 542, 447, 411, 484,
           392, 317, 502, 526, 455, 454,
           628, 500, 457, 478, 511, 365,
           407, 440, 357, 298, 594, 395,
           617, 505, 541, 458, 381)
mean(points)
sd(points)
hist(points)

install.packages("e1071")
library(e1071)

skewness(points)

kurtosis(points)

# 3 Sigma Rule
mu <- 0
sdev <- 1

pnorm(mu+sdev,mean=mu,sd=sdev) - pnorm(mu-sdev,mean=mu,sd=sdev)
pnorm(mu+2*sdev,mean=mu,sd=sdev) - pnorm(mu-2*sdev,mean=mu,sd=sdev)
pnorm(mu+3*sdev,mean=mu,sd=sdev) - pnorm(mu-3*sdev,mean=mu,sd=sdev)