# Probability Basics

# Generating a population of size 10,000
population <- sample.int(100,10000,replace = TRUE)
population[1:10]
length(population)

# Extract a sample of 100 from the population
samp <- sample(population,100)
samp[1:10]
length(samp)

# Population Mean
mean(population)

#Sample Mean
mean(samp)

#Population Median
median(population)

#Sample Median
median(samp)

# R doesnt have an inbuilt function for mode
Mode <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

# Population Mode
Mode(population)

# Sample Mode
Mode(samp)

# Population Range
max(population) - min(population)

# Sample Range
max(samp) - min(samp)

# Population Quantile
quantile(population,c(0.25,0.50,0.75))

# Sample Quantile
quantile(samp,c(0.25,0.50,0.75))

# Population InterQuantileRange
IQR(population)

# Sample InterQuantileRange
IQR(samp)

# Sample variance
var(samp)

# Function to Calculate Population Variance
PopVar <- function(x){
  n <- length(x)
  if (n > 1) {
    return (var(x)*(n-1)/n)
  } else {
    return (mean((x-mean(x))^2))
  }
}

#Population variance
PopVar(population)

# Population SD
sqrt(PopVar(population))

# Sample SD
sqrt(var(samp))

# xtabs
ucba <- data.frame(UCBAdmissions)
head(ucba)

xtabs(Freq ~ Gender + Admit ,data = ucba)

# Table Proportions
counts<-matrix(c(2,2,4,3,1,4,
                 2,0,1,5,3,3),nrow=4) 
counts 

prop.table(counts,1)

cross <- xtabs(Freq ~ Gender + Admit ,
               data = ucba[ucba$Dept=="A",])
prop.table(cross,1)

# Covariance
head(women)

cov(women$weight,women$height)

# Corelation coefficient

cor(airquality$Temp,airquality$Wind)

cor(iris[c(1:4)])

#Cut function
x<-rnorm(100)
c<-cut(x,breaks = 3)
summary(c)

x<-rnorm(100)
c<-cut(x,breaks = -5:5)
summary(c)