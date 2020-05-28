# Linear Regression

# Value of Heights
x<-c(151,174,138,186,128,136,179,163,152,131)

# Value of Weights
y<-c(63,81,56,91,47,57,76,72,62,48)

# Apply the lm() function
relation <- lm (y ~ x)
print(relation)
summary(relation)

# Find the weight of a person with height 170
a <- data.frame(x=170)
result<-predict(relation,a)
print(result)

# Plot the chart
plot(y,x,col="blue",
     main="Height & Weight Regression",
     abline(lm(x~y)),
     cex=1.3,pch=16,
     xlab="Weight in Kg",
     ylab="Height in cm")

# Faithful Solution
head(faithful)

eruption.lm = lm(eruptions ~ waiting, data=faithful) 
coeffs = coefficients(eruption.lm)
coeffs
summary(eruption.lm)

waiting = 80           # the waiting time 
duration = coeffs[1] + coeffs[2]*waiting
duration 

scatter.smooth(x=cars$speed, 
               y=cars$dist, 
               main="Dist ~ Speed")

# Divide graph area in 2 rows
par(mfrow=c(2,1))  

# Density plot for 'speed'
plot(density(cars$speed),
     main="Density Plot: Speed", 
     ylab="Frequency")  
polygon(density(cars$speed), col="red")

# Density plot for 'dist'
plot(density(cars$dist), 
     main="Density Plot: Distance", 
     ylab="Frequency")  
polygon(density(cars$dist), col="red")

cor(cars$speed, cars$dist)

linearMod <- lm(dist ~ speed, data=cars)  
print(linearMod)
summary(linearMod)

AIC(linearMod)
BIC(linearMod)

# Model Validations

# Create Training and Test data -
# setting seed to reproduce results of random sampling
set.seed(100)  
# row indices for training data
trainingRowIndex <- sample(1:nrow(cars), 0.8*nrow(cars))  

# model training data
trainingData <- cars[trainingRowIndex, ]  
# test data
testData  <- cars[-trainingRowIndex, ]   

# Build the model on training data -
lmMod <- lm(dist ~ speed, data=trainingData)  
# predict distance
distPred <- predict(lmMod, testData)  

summary (lmMod)  # model summary

AIC (lmMod)
BIC (lmMod)

# Make actuals_predicted Dataframe
actuals_preds<-data.frame(cbind(actuals=testData$dist,
                                predicteds=distPred))
head(actuals_preds)
correlation_accuracy<-cor(actuals_preds)
correlation_accuracy

min_max_accuracy <- mean(apply(actuals_preds, 1, min) /
                           apply(actuals_preds, 1, max))  
min_max_accuracy
mape<-mean(abs((actuals_preds$predicteds-actuals_preds$actuals))/
             actuals_preds$actuals)  
mape

