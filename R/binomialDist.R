# Binomial Distribution

dbinom(1,20,0.01)

# Diabetes Example

# No person with diabetes
dbinom (0, size = 50, prob = 0.09)

# Excatly one person with diabetes
dbinom (1, size = 50, prob = 0.09)

# At least two persons with diabetes : 1-P(x<=1)
1 - pbinom (1, size = 50, prob = 0.09)

# Alternate method
pbinom(1, size = 50, prob = 0.09,lower.tail = FALSE)

qbinom (0.99, size = 20, prob = 0.01)

# Find 8 random values from a sample of 150 
#with probability of 0.4.

rbinom(8,150,.4)

# Plot the Binomial Distribution

x <- seq (0, 50, by=1)

# Create Binomial Distribution
y <- dbinom (x, 50, 0.5)

# Plot the graph
plot(x,y)

install.packages("distr")
library(distr)
X<-Binom(size=20,prob=.01)
plot(X)

X <- Binom(prob=0.5,size=1)
# B is a binomial distribution with prob=0.5 and size=1.
r(X)(1) # # one random number generated from this distribution, e.g. 1
d(X)(1) # Density of this distribution is  0.5 for x=1.
p(X)(0.4) # Probability that x<0.4 is 0.5.
q(X)(.1) # x=0 is the smallest value x such that p(B)(x)>=0.1.



