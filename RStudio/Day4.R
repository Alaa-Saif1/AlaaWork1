sample_A = c(1,4,4,4,5,5,5,8)
sample_B = c(1,2,3,4,5,6,7,8)

sd(sample_A)
sd(sample_B)

CI_A = t.test(sample_A)$conf.int
CI_B = t.test(sample_B)$conf.int

set.seed(123)
boxplot(sample_A,
        main="BoxPlot Graph1",
        border="brown",
        col = "orange",
        horizontal=TRUE
)

boxplot(sample_B,
        main="BoxPlot Graph1",
        border="brown",
        col = "green",
        horizontal=TRUE
)

hist(sample_A, col = "yellow")
hist(sample_B, col = "grey")
par(mfrow = c(2,2))
