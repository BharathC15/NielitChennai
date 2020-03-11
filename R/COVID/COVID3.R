rawdf<-read.csv("ftp://192.168.1.15/bigdata/BigDataSet/COVID/2019_nCoV_data.csv")
head(rawdf)
df<-rawdf[c(4,6,7,8)]
dfm<-melt(data=df,id.vars = c(1),measure.vars = c(2,3,4))
final<-data.frame(cast(dfm,formula = Country~variable,sum))
row.names(final)<-final$Country
final1 <- subset(final, select = c(2,3,4))
table(final$Country,final$Deaths)
bha<-final1[order(desc(final1$Confirmed)),]
bha<-bha[1:12,]
barplot(t(bha),beside = TRUE,col = c("Red","Blue","Green"),legend=TRUE,log = "y",offset = 0.0001)