# Advanced R
rm(list=ls())

# Pipes
library(magrittr)
x <- pi/4
#Normal Method: 
print(log(sin(x)))
#Piping Method: 
print(x %>% sin %>% log)

print(head(iris))


clock<-data.frame(date=as.Date("2001-01-01",
                               format="%Y-%m-%d")+0:729)

clockLast <- aggregate(x = clock["date"],
                       by = list(month = substr(clock$date,1,7)),
                       FUN = max)
print(clockLast)

library(MASS)
head(mtcars)
table(mtcars$gear,mtcars$carb)
table(mtcars$gear,mtcars$carb,mtcars$cyl)

# Import DataFrame from web
data_url<- "http://tinyurl.com/zq2u8vx"
boston_housing <- read.table(data_url) 
str(boston_housing)

library(mlbench) 
data(BostonHousing) 
str(BostonHousing)

col_classes <- rep("numeric", length(BostonHousing)) 
col_classes[which("chas" == names(BostonHousing))] <- "factor" 
boston_housing <- read.table(data_url, 
                             col.names = names(BostonHousing),
                             colClasses = col_classes)
str(boston_housing)

library(dplyr)
iris %>% tbl_df
iris %>% select(Sepal.Length:Petal.Length) %>% head(3)
iris %>% tbl_df %>%   select(Sepal.Width, Petal.Length) %>% head(3)

iris %>% tbl_df %>% select(contains("etal")) %>% head (3)
iris %>% tbl_df %>% select(matches(".t.")) %>% head (3)
iris %>% tbl_df %>% select(-starts_with("petal")) %>% head (3)

iris %>% tbl_df %>% select(Sepal.Length:Petal.Length) %>% head (3)
iris %>% tbl_df %>% select(ends_with("Width")) %>% head (3)
iris %>% tbl_df %>% select(starts_with("petal")) %>% head (3)

#Mutate
iris %>% tbl_df %>% 
  mutate(Petal.Width.Length=Petal.Width+Petal.Length) %>%
  select(Species,Petal.Width.Length) %>% 
  head (3)
                       
#Transmute
iris %>% tbl_df %>% 
  transmute(Petal.Width.Length=Petal.Width+Petal.Length) %>% 
  head (3)
                              
# Arrange
iris %>% arrange(Sepal.Length) %>% head (3)
arrange(mtcars,cyl,disp)
arrange(mtcars,desc(disp))

#Filter
iris%>%filter(Sepal.Length>5  & Species=="virginica")

#by
mean(iris$Petal.Length[iris$Species=="setosa"])
mean(iris$Petal.Length[iris$Species=="versicolor"])
mean(iris$Petal.Length[iris$Species=="virginica"])

by(iris$Petal.Length,iris$Species,mean)

by(iris$Petal.Length,iris$Species,summary)
