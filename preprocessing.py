Our goal here is to prevent data leakage.

#  note: mw was removed from the analysis because 83.08% of its values were missing. also the amount of missing data changed a lot across different years so filling the missing values could give misleading results.
# Missing    Percent
# mw        442  83.082707
# area        1  0.187970




# remove mw due to the high percentage of missing values
X_train = X_train.drop(columns=["mw"])
X_test = X_test.drop(columns=["mw"])





print(X_train["area"].value_counts().head(10))




print(
    X_train.loc[
        X_train["area"].isna(),
        ["lat", "long", "dirname", "dist", "area"]
    ]
)


# OUTPUT:       lat   long dirname  dist area
# 2234  37.22  28.35   north   1.3  NaN




# remove the observation with missing area
missing_area_index = X_train[X_train["area"].isna()].index

X_train = X_train.drop(index=missing_area_index)
y_train = y_train.drop(index=missing_area_index)





print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

print("\nMissing values:")
print(X_train.isna().sum()[X_train.isna().sum() > 0])




# Point-biserial correlation


from scipy.stats import pointbiserialr
import pandas as pd

numeric_cols = [
    "lat", "long", "dist", "depth", "xm",
    "md", "richter", "ms", "mb",
    "day", "month", "year"
]

results = []

for var in numeric_cols:
    r, p = pointbiserialr(y_train, X_train[var])

    results.append({
        "Variable": var,
        "Correlation": r,
        "Abs_Correlation": abs(r),
        "P_value": p
    })

association_table = pd.DataFrame(results)

association_table = association_table.sort_values(
    by="Abs_Correlation",
    ascending=False
)

print(association_table)





#Variable  Correlation  Abs_Correlation       P_value
#4        xm     0.652218         0.652218  1.199482e-65
#7        ms     0.427131         0.427131  5.850814e-25
#6   richter     0.364785         0.364785  3.713824e-18
#8        mb     0.286728         0.286728  1.656099e-11
#3     depth     0.254292         0.254292  2.782396e-09
#11     year    -0.217277         0.217277  4.291735e-07
#5        md     0.060915         0.060915  1.610118e-01
#9       day    -0.031126         0.031126  4.741572e-01
#0       lat     0.016020         0.016020  7.126360e-01
#10    month     0.010735         0.010735  8.050698e-01
#2      dist    -0.004174         0.004174  9.235506e-01
#1      long     0.000798         0.000798  9.853556e-01
#>>> 



selected_numeric = [
    "xm",
    "ms",
    "richter",
    "mb",
    "depth"
]



correlation_matrix = X_train[selected_numeric].corr()


print(correlation_matrix.round(3))





# correlation matrix graph
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    square=True
)

plt.title("Correlation Matrix of Selected Numerical Predictors")
plt.tight_layout()

plt.savefig(
    "correlation_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

















X_train = X_train.drop(columns=["area"])
X_test = X_test.drop(columns=["area"])





