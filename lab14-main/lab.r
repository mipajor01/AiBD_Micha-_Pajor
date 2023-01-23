library(magrittr)
#Michał Pajor

lista <- 1:10
# print(list)
lista %<>% log2() %>%
    sin() %>%
    sum() %>%
    sqrt() %>%
print(lista)

data(iris)
print(head(iris))
aggr <- iris %>%
    aggregate(. ~ Species, ., mean)
print(aggr)

# install.packages("ggplot2")
library(ggplot2)
# install.packages("GGally")
library(GGally)

wykres <- ggplot(iris, aes(x = Sepal.Width)) +
    geom_histogram(aes(fill=Species, color = Species), bins=20) +
    geom_vline(data=aggr, aes(xintercept=Sepal.Width, color=Species), linetype="dashed") +
    labs(x='x_axis', y='y_axis', title='title')
ggsave("/home/wykres.jpg", plot = wykres)

wykres <- ggpairs(data = iris, aes(color = Species))
ggsave("/home/wykres2.jpg", plot = wykres)

# install.packages("cluster")
library(cluster)
x <- iris[,1:4]

y <- iris[,5]

sum_sqr <- c()

for (i in 1:10){
    kmeans_result <- kmeans(x, i)
    sum_sqr <- append(sum_sqr, kmeans_result$tot.withinss)
}

wykres <- ggplot(data.frame(iteration = 1:length(sum_sqr), value = sum_sqr), aes(x = iteration, y = sum_sqr)) +
    geom_line() 
    ggsave("/home/wykres3.jpg", plot = wykres) 
    
kmeans_result <- kmeans(x, 3)
wykres <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color = kmeans_result$cluster)) + geom_point()
ggsave("/home/wykres4.jpg", plot = wykres)

wykres <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color = Species)) + geom_point() 
ggsave("/home/wykres5.jpg", plot = wykres)
