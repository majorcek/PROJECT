library(plotly)
library(rvest)
library(dplyr)
library(scatterplot3d)
probabaility_naive_3D <- read.csv2("data/probability_naive_3D.csv", header = TRUE, dec = ".", sep = ",", encoding = "UTF-8", check.names = FALSE)
proba3D <- probabaility_naive_3D[,-1]


Z_naive <- as.matrix(proba3D)
Y <- seq(3,50,1)
X <- seq(0,1,0.01)
col.pal <- colorRampPalette(c("green", "orange"))
colors <- col.pal(101)
z.facet.center <- (Z_naive[-1, -1] + Z_naive[-1, -ncol(Z_naive)] + Z_naive[-nrow(Z_naive), -1] + Z_naive[-nrow(Z_naive), -ncol(Z_naive)])
z.facet.range <- cut(z.facet.center, 101)

graf_3D_naive <- persp(x = X, z = Z_naive, 
      theta = 130, phi = 30, 
      xlab = "ratio between radiuses", ylab = "number of points", zlab = "probability", 
      main = "Circle inside convex hull",
      sub = "probability that smaller circle is inside convex hull",
      col = colors[z.facet.range],
      shade = 0.01,
      expand = 0.25,
      ticktype = "simple"
      )


###############################################
###############################################

probabaility_polar_3D <- read.csv2("data/probability_polar_3D.csv", header = TRUE, dec = ".", sep = ",", encoding = "UTF-8", check.names = FALSE)
proba3D_polar <- probabaility_polar_3D[,-1]


Z_polar<- as.matrix(proba3D_polar)
Y <- seq(3,50,1)
X <- seq(0,1,0.01)
col.pal <- colorRampPalette(c("green", "orange"))
colors <- col.pal(101)
z.facet.center.polar <- (Z_polar[-1, -1] + Z_polar[-1, -ncol(Z_polar)] + Z_polar[-nrow(Z_polar), -1] + Z_polar[-nrow(Z_polar), -ncol(Z_polar)])
z.facet.range.polar <- cut(z.facet.center.polar, 101)

graf_3D_polar <- persp(x = X, z = Z_polar, 
                       theta = 130, phi = 30, 
                       xlab = "ratio between radiuses", ylab = "number of points", zlab = "probability", 
                       main = "Circle inside convex hull",
                       sub = "probability that smaller circle is inside convex hull",
                       col = colors[z.facet.range.polar],
                       shade = 0.01,
                       expand = 0.25,
                       ticktype = "simple"
)
