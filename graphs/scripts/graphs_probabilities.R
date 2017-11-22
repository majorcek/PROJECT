library(ggplot2)
library(reshape)
library(dplyr)
library(rvest)

probabaility_naive0 <- read.csv2("../../data/probability_naive_4000.csv", header = TRUE, dec = ".", sep = ",", encoding = "UTF-8", check.names = FALSE)
probabaility_naive <- melt(probabaility_naive0, id = "r")
colnames(probabaility_naive) <- c("r", "tocke", "probability")

graf_probabaility_naive <- ggplot(data = probabaility_naive, aes(x = r, y = probability, col = tocke), order = as.numeric(tocke))+
  geom_line()+
  guides(colour = guide_legend(reverse=T))+
  scale_colour_discrete(name="Number of\n  points\n") + 
  labs(x = "ratio between circle radiuses")+
  labs(y = "probability")+
  labs(title = "Length of convex hull versus ratios for different number \nof points (naive distribution)")+
  labs(caption = "*length is divided with R of bigger circle")

##################################################
##################################################

probabaility_polar0 <- read.csv2("../../data/probability_polar_4000.csv", header = TRUE, dec = ".", sep = ",", encoding = "UTF-8", check.names = FALSE)
probabaility_polar <- melt(probabaility_polar0, id = "r")
colnames(probabaility_polar) <- c("r", "tocke", "probability")

graf_probability_polar <- ggplot(data = probabaility_polar, aes(x = r, y = probability, col = tocke), order = as.numeric(tocke))+
  geom_line()+
  guides(colour = guide_legend(reverse=T))+
  scale_colour_discrete(name="Number of\n  points\n") + 
  labs(x = "ratio between circle radiuses")+
  labs(y = "probability")+
  labs(title = "Length of convex hull versus ratios for different number \nof points (polar distribution)")+
  labs(caption = "*length is divided with R of bigger circle")

##############################################
##############################################

probabaility_naive$type <- "naive"
probabaility_polar$type <- "polar"
probability_primerjava <- rbind(probabaility_naive, probabaility_polar)

graf_probability_primerjava <- ggplot(data = probability_primerjava, aes(x = r, y = probability, col = tocke, lty = type))+
  geom_line()+
  guides(colour = guide_legend(reverse=T)) +
  labs(col = "Number of\n  points\n", lty = "") +
  labs(type = "") + 
  labs(x = "ratio between circle radiuses") +
  labs(y = "probability") +
  labs(title = "Comparison between polar and naive distibuted points (probability)")# +
  #labs(caption = "*area is diveded with R of bigger circle")
