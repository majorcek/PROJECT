library(ggplot2)
library(reshape)
library(dplyr)
library(rvest)

area_naive0 <- read.csv2("../../data/area_naive_4000.csv", header = TRUE, dec = ".", sep = ",", encoding = "UTF-8", check.names = FALSE)
area_naive <- melt(area_naive0, id = "r")
colnames(area_naive) <- c("r", "tocke", "povrsina")

graf_area_naive <- ggplot(data = area_naive, aes(x = r, y = povrsina, col = tocke), order = as.numeric(tocke))+
  geom_line()+
  guides(colour = guide_legend(reverse=T))+
  scale_colour_discrete(name="Number of\n  points\n") + 
  labs(x = "ratio between circle radiuses")+
  labs(y = "area")+
  labs(title = "Area of convex hull versus ratios for different number \nof points (naive distributed)")+
  labs(caption = "*area is diveded with R^2 of bigger circle")

##################################################
##################################################
area_polar0 <- read.csv2("../../data/area_polar_4000.csv", header = TRUE, dec = ".", sep = ",", encoding = "UTF-8", check.names = FALSE)
area_polar <- melt(area_polar0, id = "r")
colnames(area_polar) <- c("r", "tocke", "povrsina")

graf_area_polar <- ggplot(data = area_polar, aes(x = r, y = povrsina, col = tocke), order = as.numeric(tocke))+
  geom_line()+
  guides(colour = guide_legend(reverse=T))+
  scale_colour_discrete(name="Number of\n  points\n") + 
  labs(x = "ratio between circle radiuses")+
  labs(y = "area")+
  labs(title = "Area of convex hull versus ratios for different number \nof points (polar distributed)")+
  labs(caption = "*area is diveded with R^2 of bigger circle")

#####################################################
#####################################################
area_naive$type <- "naive"
area_polar$type <- "polar"
area_primerjava <- rbind(area_naive, area_polar)

graf_area_primerjava <- ggplot(data = area_primerjava, aes(x = r, y = povrsina, col = tocke, lty = type))+
  geom_line()+
  guides(colour = guide_legend(reverse=T)) +
  labs(col = "Number of\n  points\n", lty = "") +
  labs(type = "") + 
  labs(x = "ratio between circle radiuses") +
  labs(y = "area") +
  labs(title = "Comparison between polar and naive distibuted points") +
  labs(caption = "*area is diveded with R^2 of bigger circle")

graf_area_primerjava

