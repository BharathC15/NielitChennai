# Student T Test

sample <- c(1,2,3,4,5) #Samples
pop_mean <- 3.5 #Population Mean
sample_mean <- mean(sample) # Sample Mean
sample_std <- sd(sample) #Sample Standard Deviation
n <- length(sample) #No of Sample
dof <- n-1 #Degree of Freedom
cl <- 0.95 #Confidence level
significant <- 1-cl # Significant Level

cat("Sample values are",sample)
cat("Population mean",pop_mean)
cat("Sample mean",sample_mean)
cat("Sample Standard Deviation",sample_std)
cat("No of samples",n)
cat("Degree fo freedom",dof)
cat("Confidence Interval",cl)
cat("Significant level",significant)

tstatistics = (sample_mean - pop_mean) /
  (sample_std/sqrt(n))
cat("T Statistics is",tstatistics)

tcritical_l<- qt(p=significant/2,df=dof)
tcritical_u<--tcritical_l
cat("Critical Values are",tcritical_l,tcritical_u)

if(tstatistics<tcritical_l | tstatistics>tcritical_u){
  print("Reject the Null hypothesis")
  } else {
  print("Fails to reject the Null hypothesis")
  }

pvalue <- 2*pt(q=tstatistics,df=dof)
cat("p-value is ",pvalue)

if(pvalue<0.05){
  print("Reject the Null hypothesis")
} else {
  print("Fails to reject the Null hypothesis")
}

SE<-sample_std/sqrt(n)
cat("Standard Error",SE)

cat("Confidence Interval",sample_mean+SE*c(tcritical_l,tcritical_u))

x<-seq(-5,5,length=100)
tplot<-dt(x,dof)
plot(x,tplot,type = "l")
x<-seq(-5,tcritical_l,length=100)
y<-dt(x,dof)
polygon(c(-5,x,tcritical_l),c(0,y,0),col="gray")
x<-seq(tcritical_u,5,length=100)
y<-dt(x,dof)
polygon(c(tcritical_u,x,5),c(0,y,0),col="gray")
abline(v=tstatistics)




# 2 Sample t test
sample1 <- rnorm(n = 20,mean = 4.7,sd = 1)
sample2 <- rnorm(n = 20,mean = 5.3,sd = 1)
cat("Mean of sample1",mean(sample1))
cat("Mean of sample2",mean(sample2))
t.test(x = sample1,y = sample2)