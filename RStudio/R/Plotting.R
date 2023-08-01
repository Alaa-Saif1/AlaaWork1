# plotting a histogram graph using random data


#Load the ggplot2 library:

library(ggplot2)


#Set a seed for reproducibility:

set.seed(123)

#Generate random data:

data <- data.frame(x = rnorm(1000, mean = 50, sd = 10))

#Create histogram plot:

ggplot(data, aes(x)) +
  geom_histogram(fill = "steelblue", color = "white", bins = 30) +
  labs(x = "Value", 
       y = "Frequency", 
       title = "Random Data Histogram") +
  coord_cartesian(xlim = c(10, 80))

##########################

# Coloring The graph by the variable

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


############################

# Histogram for two normal distributions

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


###################

# density histogram with kernel density estimate overlay

set.seed(123)

# Generate random data from a uniform distribution:

data <- data.frame(x = runif(1000, min = 0, max = 1))

# Create density histogram with kernel density estimate overlay:

ggplot(data, aes(x)) +
  geom_histogram(aes(y = ..density..), fill = "steelblue", color = "white", bins = 30)
  + geom_density(alpha = 0.3, color = "darkorange") +
  labs(x = "Value", y = "Density",
       title = "Density Histogram with Kernel Density Estimate") +
   theme_minimal()

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

################

# Load and intall the Libraries:

install.packages("gganimate")

library(ggplot2)
library(gganimate)


# Load the data set:

data(mtcars)

# Create the animated scatter plot:

p <- ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  labs(x = "Weight", y = "Miles per Gallon") +
  ggtitle("Animated Scatter Plot")

animation <- p + transition_states(factor(cyl), transition_length = 2, state_length = 1) +
  enter_fade() +
  exit_fade()

animate(animation, nframes = 10, fps = 5)
