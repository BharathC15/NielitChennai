#library(tidyverse)
rawdf<-read.csv("ftp://192.168.1.15/bigdata/BigDataSet/COVID/2019_nCoV_data.csv")

head(rawdf)

rawdf%>%select(c("Country","Province.State","Confirmed","Deaths","Recovered"))

rawdf%>%select(c("Country","Province.State","Confirmed","Deaths","Recovered"))%>%group_by("Country","Province.State")
