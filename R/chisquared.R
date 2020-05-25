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

head(housetask)
