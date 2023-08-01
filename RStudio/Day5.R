# import

library(readr)
Heart_Disease <- read_csv("C:/Users/user/Desktop/Alaa Saif/RStudio/Heart_Disease_Prediction.csv")
View(Heart_Disease)


summary(Heart_Disease)
str(Heart_Disease)
# 270 observation & 14 variables

Heart_Disease[1,]
x1 = Heart_Disease[1,]
View(x1)
x2 = Heart_Disease[,1]
View(x2)

# Spilt Data set to create new data set
MyNewData = Heart_Disease[,c(1,2,4,13,14)]
View(MyNewData)

set.seed(123)
boxplot(MyNewData$Age,
        main="BoxPlot Graph for Age",
        xlab="Age",
        border="brown",
        col = "light pink",
        horizontal=TRUE
)

boxplot(MyNewData$BP,
        main="BoxPlot Graph for BP",
        xlab="BP",
        border="brown",
        col = "light blue",
        horizontal=TRUE
)

boxplot(MyNewData$Age ~ MyNewData$`Heart Disease`,
        main="BoxPlot Graph for BP",
        xlab="Age",
        border="brown",
        col = c("light blue","light pink"),
        horizontal=TRUE
)
par(mfrow = c(2,1))
fivenum(MyNewData$Age)

# Linear Regression

model2= lm(MyNewData$Age ~ MyNewData$BP)
summary(model2)

cor(MyNewData$Age, MyNewData$BP)

plot(MyNewData$Age ~ MyNewData$BP,
        main="correlation graph between Age & BP",
        xlab="BP",
        ylab="Age",
        border="brown",
        col = c("blue","pink")
)

# To drow fit line
abline(model2,col="black")

# spilt male from female:

MD = MyNewData[MyNewData$Sex == 1,]
FD = MyNewData[MyNewData$Sex == 0,]
View(MD)
View(FD)

cor(MD$BP,MD$Age)

plot(MD$BP ~ MD$Age,
     main="correlation graph for Male between Age & BP",
     xlab="Age",
     ylab="BP",
     border="brown",
     col = c("blue","pink")
)

cor(FD$BP,FD$Age)

plot(FD$BP ~ FD$Age,
     main="correlation graph for female between Age & BP",
     xlab="Age",
     ylab="BP",
     border="brown",
     col = c("blue","pink")
)

par(bg="light grey")

barplot(table(MyNewData$Sex),
        main = "Bar plot to show the freqency if male & female",
        border = "brown",
        col = c("light blue","light pink"),
        horizontal=TRUE
)
