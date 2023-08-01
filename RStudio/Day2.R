numb = c(8,10,12)
price = c(10.000,12.000,8.000)
weighted.mean(price,numb)


Fav = c(40,30,50)
nums = c(1000,3000,800)
weighted.mean(Fav,nums)


A = c(44,39,22,50,64)
z_scores = (A-mean(A))/sd(A)
z_scores


B = c(22,20,18,30,11)
z_scores = (B-mean(B))/sd(B)
z_scores

rnorm(20,3,4)
rnorm(20,5,2)*10

set.seed(123)
var1 = rnorm(100,50,2.5)
boxplot(var1,
        main="BoxPlot Graph",
        border="brown",
        col = "grey",
        horizontal=TRUE
)
fivenum(var1)
summary(var1)

var1[3]
var1[3] = var1[3]+40
boxplot(var1,
        main="BoxPlot Graph",
        border="brown",
        col = "grey",
        horizontal=TRUE,
        outline=FALSE
)

var1[50]
var1[50] = var1[3]-30
boxplot(var1,
        main="BoxPlot Graph",
        border="brown",
        col = "grey",
        horizontal=TRUE,
        outline=FALSE
)


