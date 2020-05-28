# Chi Squared Test of Independance

library(MASS)
tbl <- table(survey$Smoke,survey$Exer)
tbl

chisq.test(tbl)

ctbl <- cbind(tbl[,"Freq"], 
              tbl[,"None"] + tbl[,"Some"])
ctbl
chisq.test(ctbl) 


M <- as.table(rbind(c(200, 150, 50), 
                    c(250, 300, 50)))
dimnames(M) <- list(gender = c("F", "M"), 
                    party = c("Democrat",
                              "Independent",
                              "Republican"))
(Xsq <- chisq.test(M))  # Prints test summary

Xsq$observed   # observed counts (same as M)
Xsq$expected   # expected counts under the null
Xsq$residuals  # Pearson residuals
Xsq$stdres     # standardized residuals

install.packages("ade4")
library(ade4)
data(housetasks)
head(housetasks)

chisq <- chisq.test(housetasks)
chisq

chisq$observed
chisq$expected

round(chisq$residuals, 3)

contrib <- 100*chisq$residual^2/chisq$statistic
round(contrib,3)

tulip <- c(81, 50, 27)
res <- chisq.test(tulip, p = c(1/3, 1/3, 1/3))
res

tulip <- c(81, 50, 27)
res <- chisq.test(tulip, p = c(1/2, 1/3, 1/6))
res

x <- rnorm(50)
y <- runif(30)
# Do x and y come from the same distribution?
ks.test(x, y)

x <- rnorm(30)
y <- rnorm(100)
# Do x and y come from the same distribution?
ks.test(x, y)

ks.test(x+2,"pgamma",3,2)
ks.test(x+2,"pgamma",3,2,exact = FALSE)
ks.test(x+2,"pgamma",3,2,alternative = "gr")


#One sample
z<-rnorm(100)
ks.test(z,y="pnorm") # Hypothesize a normal Dist
ks.test(z,y="pchisq",df=2) # Hypothesize a chisqare Dist
ks.test(z,y="pgamma",shape=3,scale=2,
        exact=FALSE,alternative="greater")

#Two Sample
x<-rnorm(90)
y<-rnorm(8,mean=2.0,sd=1)
ks.test(x,y)
ks.test(x,y,exact=FALSE,alternative="less")

