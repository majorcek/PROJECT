library(ggplot2)
library(reshape)
library(dplyr)
library(rvest)

length_naive0 <- read.csv2("../../data/length_naive_4000.csv", header = TRUE, dec = ".", sep = ",", encoding = "UTF-8", check.names = FALSE)
length_naive <- melt(length_naive0, id = "r")
colnames(length_naive) <- c("r", "tocke", "dolzina")

graf_length_naive <- ggplot(data = length_naive, aes(x = r, y = dolzina, col = tocke), order = as.numeric(tocke))+
  geom_line()+
  guides(colour = guide_legend(reverse=T))+
  scale_colour_discrete(name="Number of\n  points\n") + 
  labs(x = "ratio between circle radiuses")+
  labs(y = "length")+
  labs(title = "Length of convex hull versus ratios for different number \nof points (naive distribution)")+
  labs(caption = "*length is divided with R of bigger circle")

#########################################
#########################################
length_polar0 <- read.csv2("../../data/length_polar_4000.csv", header = TRUE, dec = ".", sep = ",", encoding = "UTF-8", check.names = FALSE)
length_polar <- melt(length_polar0, id = "r")
colnames(length_polar) <- c("r", "tocke", "dolzina")

graf_length_polar <- ggplot(data = length_polar, aes(x = r, y = dolzina, col = tocke), order = as.numeric(tocke))+
  geom_line()+
  guides(colour = guide_legend(reverse=T))+
  scale_colour_discrete(name="Number of\n  points\n") + 
  labs(x = "ratio between circle radiuses")+
  labs(y = "length")+
  labs(title = "Length of convex hull versus ratios for different number \nof points (polar distribution)")+
  labs(caption = "*length is divided with R of bigger circle")

#####################################
#####################################

length_naive$type <- "naive"
length_polar$type <- "polar"
length_primerjava <- rbind(length_naive, length_polar)

graf_primerjava_length <- ggplot(data = length_primerjava, aes(x = r, y = dolzina, col = tocke, lty = type))+
  geom_line()+
  guides(colour = guide_legend(reverse=T)) +
  labs(col = "Number of\n  points\n", lty = "") +
  labs(type = "") + 
  labs(x = "ratio between circle radiuses") +
  labs(y = "area") +
  labs(title = "Comparison between polar and naive distibuted points") +
  labs(caption = "*area is diveded with R of bigger circle")