# Page Complexity Alorithm

STILL A WORK IN PROGRESS

## Complexity Score

```
α*F1 + β*F2 + γ*G + λ*(α² + β²) + ε
```

## Variables

-   F1 and F2 represent the main factors derived from Factor Analysis, which are unobserved variables that are inferred from the observed variables (various webpage attributes).

-   G represents the group assignment of a web page, derived from K-Means Cluster Analysis. This variable classifies web pages into distinct groups based on similarities in their characteristics.

-   α, β, and γ are the coefficients that the model learns during training. These coefficients represent the importance or weight of each factor (F1 and F2) and group (G) in determining the complexity score.

-   λ is the regularization parameter. It's a constant that we set to prevent overfitting by penalizing high-valued coefficients (α and β).

-   (α² + β²) is the regularization term. This form of regularization is known as L2 regularization or Ridge regularization.

-   ε is the error term. It captures the unexplained variance in the complexity score.
