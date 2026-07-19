
# Import the earthquake dataset from a .txt file 
# Read a txt file, named "mugla.txt"

# This code will read the dataset as if it contains only one variable

mugla <- read.delim("mugla.txt")


# To import the data without errors, you need to apply the following code 
mugla <- read.delim("mugla.txt", header = TRUE, sep = "", row.names = 1)



# Total NA  values from all variables
colSums(is.na(mugla)) #554,mw: moment magnitude of the earthquake
