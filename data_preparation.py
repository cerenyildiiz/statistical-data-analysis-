# reticulate::py_require("pandas") for R-to-Python integration , please  run in the R console
# reticulate::source_python("earthquake.py")

import pandas as pd

# import mugla.txt data
mugla = pd.read_csv(
    "mugla.txt",
    sep=r"\s+",
    header=0,
    index_col=0
)

mugla.head()


print(mugla.head()) 



# total NA  values from all variables
print("\nMissing values:")
print(mugla.isna().sum())




# splitting of data into train and test data

from sklearn.model_selection import train_test_split

train_data, test_data = train_test_split(
    mugla,
    test_size=0.20,
    random_state=123,
    stratify=mugla["mg"]     # stratified split
)

print("Train dataset:", train_data.shape)









X_train = train_data.drop(columns=["mg"])
y_train = train_data["mg"]

X_test = test_data.drop(columns=["mg"])
y_test = test_data["mg"]
print("Test dataset:", test_data.shape)






# check class proportions
print("Train class proportions:")
print(y_train.value_counts(normalize=True))

print("\nTest class proportions:")
print(y_test.value_counts(normalize=True))









