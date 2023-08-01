# convert the data frame into excel file:

library(readr)

marksheet <- read_csv("marksheet.csv")
View(marksheet)

mymatrix = matrix(1:9, nrow=3, ncol=3)
mydf = data.frame(mymatrix)

library(rio)

export(mydf,"t1.xlsx")

############# Practice #################

# create a matrix of 5 student scores in three subjects
# create student scores by using functions, make sure the numbers you get
# are integer without decimal points.

# Create a matrix of student scores:

student_scores <- rbind(
  c(80, 90, 75),
  c(85, 92, 78),
  c(70, 80, 88),
  c(92, 87, 95),
  c(78, 83, 90)
)

# Assign column names & row names:

colnames(student_scores) <- c("Math", "Physics", "Biology")
rownames(student_scores) <- c("Ali", "Bader", "Saif", "Sultan", "Ahmed")


# Calculate total grade for each student:

total_grades <- rowSums(student_scores)

# Calculate percentage for each student:

percentages <- round(total_grades / 300 * 100, 2)

# Add total grade and percentage as new columns to the matrix:

student_scores <- cbind(student_scores, Total = total_grades, 
                        Percentage = percentages)

# Print the matrix:

print(student_scores)

# Save the result in an excel file:

# I use rio library format:

export(student_scores, "student_scores.xlsx")

#########################

student_scores2 = edit(student_scores)
print(student_scores2)

#######################

# Load the ggplot2 library:

library(ggplot2)


# Set a seed for reproducibility:

set.seed(123)

# Generate random data:

data <- data.frame(x = rnorm(1000, mean = 50, sd = 10))

# Create histogram plot:

ggplot(data, aes(x)) +
  geom_histogram(fill = "steelblue", color = "white", bins = 30) +
  labs(x = "Value", 
       y = "Frequency", 
       title = "Random Data Histogram") +
  coord_cartesian(xlim = c(10, 80))

##################################

set.seed(123)

# Generate random data:

n <- 1000
data <- data.frame(
  category = factor(sample(LETTERS[1:5], n, replace = TRUE)),
  value = rnorm(n)
)

# Create the histogram:

ggplot(data, aes(x = value, fill = category)) +
  geom_histogram(binwidth = 0.5, color = "black", alpha = 0.7) +
  labs(x = "Value", y = "Frequency", fill = "Category") +
  scale_fill_discrete(name = "Category") +
  theme_minimal()


##################################

set.seed(123)

# Generate random data from two normal distributions:

data <- data.frame(
  x = c(rnorm(1000, mean = 50, sd = 10), 
        rnorm(1000, mean = 70, sd = 15)),
  group = rep(c("Group 1", "Group 2"), each = 1000)
)

# Create grouped histogram:

ggplot(data, aes(x, fill = group)) +
  geom_histogram(color = "white", bins = 30, alpha = 0.7, position = "identity") +
  labs(x = "Value", y = "Frequency", title = "Grouped Histogram") +
  scale_fill_manual(values = c("steelblue", "darkorange")) +
  theme_minimal()

#################################

set.seed(123)

# Generate random data from a uniform distribution:

data <- data.frame(x = runif(1000, min = 0, max = 1))

# Create density histogram with kernel density estimate overlay:

ggplot(data, aes(x)) +
  geom_histogram(aes(y = ..density..), fill = "steelblue", color = "white", bins = 30) +
  geom_density(alpha = 0.3, color = "darkorange") +
  labs(x = "Value", y = "Density", title = "Density Histogram with Kernel Density Estimate") +
  theme_minimal()

########################################

# using mtcars data set to use boxplot


# Load the mtcars data set:

data(mtcars)

# Create a boxplot with individual data points:

boxplot(mpg ~ cyl, data = mtcars, outline = TRUE,
        ylab = "Miles per Gallon", xlab = "Number of Cylinders")

########################################

# using mtcars data set to use boxplot

# Load the Libraries:

library(ggplot2)
library(viridis) # improve graph readability for readers
library(hrbrthemes) # provides typography-centric theme

# Load the mtcars data set:

data(mtcars)

# Create a boxplot with individual data points:

ggplot(mtcars, aes(x = factor(cyl), y = mpg)) +
  geom_boxplot() +
  scale_fill_viridis(discrete = TRUE, alpha=0.6) +
  geom_jitter(width = 0.2, height = 0, color = "blue", alpha = 0.5) +
  theme_ipsum() +
  labs(x = "Cylinders", y = "Miles per Gallon") +
  ggtitle("A boxplot with jitter")