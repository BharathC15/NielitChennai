#Visualization
str(airquality)

library(help = "graphics")

x11()

plot(airquality$Ozone)

x11()

plot(airquality$Ozone, airquality$Wind)

plot(airquality)

plot(airquality$Ozone, type= "b")

plot(airquality$Ozone, type= "h")

plot(airquality$Ozone,
  xlab = 'ozone Concentration', 
  ylab = 'No of Instances', 
  main = 'Ozone levels in NY city', 
  col = 'red')

barplot(airquality$Ozone, 
        main = 'Ozone Concenteration in air',
        xlab = 'ozone levels', 
        col= 'green',
        horiz = TRUE)

hist(airquality$Solar.R)

hist(airquality$Solar.R, 
     main = 'Solar Radiation values in air',
     xlab= 'Solar rad.', 
     col='red')

boxplot(airquality$Solar.R)

boxplot(airquality[,0:4], 
        main='Multiple Box plots')

boxplot(airquality, 
        main='Multiple Box plots')


par(mfrow=c(3,3), mar=c(2,5,2,1), 
    las=1, bty="n")
plot(airquality$Ozone)
plot(airquality$Ozone, airquality$Wind)
plot(airquality$Ozone, type= "c")
plot(airquality$Ozone, type= "s")
plot(airquality$Ozone, type= "h")
barplot(airquality$Ozone, 
        main = 'Ozone Concenteration in air',
        xlab ='ozone levels', 
        col='green',horiz = TRUE)
hist(airquality$Solar.R)
boxplot(airquality$Solar.R)
boxplot(airquality[,0:4], 
        main='Multiple Box plots')

#ggplot2

install.packages("ggplot2")
library(ggplot2)

install.packages("gapminder")
library(gapminder)
head(gapminder)

ggplot(gapminder,aes(x = gdpPercap,y = lifeExp))+geom_point()

# Another Method

p <- ggplot(gapminder,aes(x = gdpPercap,y = lifeExp))
p + geom_point()+ scale_x_log10()


#Another method
ggplot(gapminder,aes(x = log(gdpPercap),
                     y = lifeExp))+geom_point()


ggplot(gapminder,aes(x = gdpPercap,
                     y = lifeExp,
                     color = continent))+geom_point()

ggplot(gapminder,aes(x = log(gdpPercap),
                     y = lifeExp))+
  geom_point(alpha = (1/3), size = 3)

ggplot(gapminder,aes(x = log(gdpPercap),
                     y = lifeExp))+
  geom_point()+ geom_smooth()

ggplot(gapminder,aes(x = log(gdpPercap),
                     y = lifeExp))+
  geom_point()+ geom_smooth(method = "lm")

ggplot(gapminder,aes(x = log(gdpPercap),
                     y = lifeExp,
                     color = continent))+
  geom_point(alpha = (1/3))+ geom_smooth()


  ggplot(gapminder,aes(x = log(gdpPercap),
                       y = lifeExp,
                       color = continent))+
  facet_wrap((~ continent))+
  geom_point(alpha = (1/3))+ geom_smooth()
  
  