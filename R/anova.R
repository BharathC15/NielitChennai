#ANOVA Test

library(dplyr)
my_data <- PlantGrowth

sample_n(my_data, 10)

levels(my_data$group)

my_data$group<-ordered(my_data$group,                         levels = c("ctrl", "trt1", "trt2"))

group_by(my_data, group) %>% 
  summarise( count = n(), 
             mean = mean(weight, na.rm = TRUE),
             sd = sd(weight, na.rm = TRUE) )

# Compute the analysis of variance
res.aov <- aov(weight ~ group, data = my_data)
# Summary of the analysis
summary(res.aov)

TukeyHSD(res.aov)
