library(ggplot2)
library(reshape)
library(dplyr)
library(rvest)
area_naive <- read.csv2("area_naive_4000.csv", header = TRUE, dec = ".", sep = ",", encoding = "UTF-8", check.names = FALSE)

graf1 <- ggplot(data = area_naive, aes(x = area_naive$r)) +
  geom_point(aes(y = area_naive$X3)) + 
  geom_smooth(aes(y = area_naive$X3, group = 1 ))
graf1

area <- melt(area_naive, id = "r")
colnames(area) <- c("r", "tocke", "povrsina")
area$tocke <- gsub("X", "", area$tocke) #%>% as.factor   #  as.character# %>% as.numeric()
#levels(area$tocke) <- area$tocke
graf2 <- ggplot(data = area, aes(x = r, y = povrsina, col = tocke), order = as.numeric(tocke))+
  geom_line()+
  guides(colour = guide_legend(reverse=T))+
  scale_colour_discrete(name="Number of\n  points\n") + 
  labs(x = "ratio between circles")+
  labs(y = "area")+
  labs(title = "Area of convex hull versus ratios for different number of points ")+
  labs(caption = "*area is diveded with R of bigger circle")
graf2

