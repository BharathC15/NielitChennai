# Poisson Distribution

# Solution for (a)
ppois(0, lambda=3,lower.tail=FALSE)

#Solution for (b)
ppois(1, lambda=3,lower.tail=FALSE) -
  ppois(4, lambda=3,lower=FALSE) 

#Solution for (c)
# Lambda (Average) for 5 days = 3
# So lambda for 1 day = 3 / 5
dpois(1, lambda = (3/5))

X <- Pois(lambda = 1.4)
plot(X)