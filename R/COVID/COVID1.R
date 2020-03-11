rawdf<-read.csv("ftp://192.168.1.15/bigdata/BigDataSet/COVID/2019_nCoV_data.csv")
head(rawdf)
df<-rawdf[c(4,6,7,8)]
head(df)
dfm<-melt(data=df,id.vars = c(1),measure.vars = c(2,3,4))
head(dfm)
final<-cast(dfm,formula = Country~variable,sum)
head(final)
row.names(final)<-final$Country
final$Country<-NA
final1 <- subset(final, select = c(2,3,4))
head(final1)
