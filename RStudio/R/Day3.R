
# Create a table in the data frame:

my_df <- data.frame(
  ID = c(1,2,3),
  Name = c('Ali', 'Saif', 'Khalid'),
  Percent = c(95,88,90),
  stringsAsFactors = FALSE
)

print(my_df)

#####################

my_df2 <- data.frame(
  ID = c(1,2,3),
  status = c('Grd', 'Enr','Grd'),
  year = c(3,5,2),
  stringsAsFactors = FALSE
)

print(my_df2)

# Merging Data Frames:

Total <- merge(my_df,my_df2, by="ID")
print(Total)

#####################

mydata = data.frame(Titanic)
View(mydata)
head(mydata)

# Selecting Observation:

attach(mydata) # To Call the Variable from mydata by [$]

newdata <- mydata[which(mydata$Class == 'Crew' & mydata$Survived == 'Yes'),]
View(newdata)

####################

# The Subset() Function:

newdata <- subset(mydata,mydata$Class == 'Crew' & mydata$Survived == 'Yes',
                  select = c(Class,Survived))
View(newdata)

######################

# I choose [mtcars] data set to convert it into data frame:

MyTestData = data.frame(mtcars)
View(MyTestData) # Open a spreadsheet-like viewer to visualize the data frame. 
head(MyTestData) # Display the first few rows of the "MyTestData" data frame.

# Selecting Observation:

# logical condition:

# Select rows where mpg is greater than 20:

selected_rows1 <- MyTestData[MyTestData$mpg > 20, ]
View(selected_rows1)

# multiple conditions:

# Select rows where mpg is greater than 20 and hp is less than 100:

selected_rows2 <- MyTestData[MyTestData$mpg > 20 & MyTestData$hp < 100, ]
View(selected_rows2)

# The Subset() Function:

# Subset the "MyTestData" data frame to select specific columns:

subset_data <- subset(MyTestData, select = c(mpg, cyl, disp))
View(subset_data)

# Print the first few rows of the subsetted data frame:

head(subset_data)


# Random Samples:

# Load the dplyr package for data manipulation:

library(dplyr)

# Generate a random sample of 5 observations using sample_n():

random_sample <- sample_n(MyTestData, 5)
View(random_sample)

# Print the random sample:

random_sample

# using SQL statement to Manipulate data frame:

# Load the sqldf package:

library(sqldf)

# Manipulate the data frame using SQL statements:

manipulated_data <- sqldf("
  SELECT mpg, cyl, hp
  FROM MyTestData
  WHERE mpg > 20
  ORDER BY hp DESC
  LIMIT 10
")

View(manipulated_data)

# Print the manipulated data frame:

manipulated_data

########################

# if condition:

score <- 79.5

if (score >= 90) {
  grade <- "A"
} else if (score >= 80) {
  grade <- "B"
} else if (score >= 70) {
  grade <- "C"
} else if (score >= 60) {
  grade <- "D"
} else {
  grade <- "F"
}

print(grade)

########################

s = as.integer(readline(prompt = "Enter start number: "))
e = as.integer(readline(prompt = "Enter end number: "))

i = s
sum = 0
while(i<=e){
  sum = sum + i
  i = i + 1
}

print(paste("sum is: ", sum))

#####################

mat <- matrix(1:25, nrow = 5)
mat

for (i in mat) {
  print(i)
  
}
for (row in 1:nrow(mat)) {
  for (col in 1:ncol(mat)) {
    print(paste('The element at row: ', row, 'and col: ',col, 'is: ', mat[row,col]))
    
  }
  
}

################

# write a function to find the mean and sd of a numeric variable:

calculate_mean_sd <- function(data) {
  mean_val <- mean(data)
    sd_val <- sd(data)
    
    return(list(mean = mean_val, sd = sd_val))
}

data <- c(1, 2, 3, 4, 5)
result <- calculate_mean_sd(data)
print(result$mean)  
print(result$sd)

