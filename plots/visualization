
#  - PCA Class Separation Graph -
library(ggplot2)

pca_plot <- data.frame(
  PC1 = train_pca[, "PC1"],
  PC2 = train_pca[, "PC2"],
  mg = train$mg
)

ggplot(pca_plot, aes(x = PC1, y = PC2, color = mg)) +
  geom_point(alpha = 0.7, size = 2) +
  labs(
    title = "PCA: Class Separation",
    x = "Principal Component 1",
    y = "Principal Component 2",
    color = "mg"
  ) +
  theme_minimal()




