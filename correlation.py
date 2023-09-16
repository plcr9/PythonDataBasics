import pandas as pd
x = pd.Series(range(10, 20))
y = pd.Series([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
x.corr(y)                     # Pearson's r
0.7586402890911867
y.corr(x)
0.7586402890911869
x.corr(y, method='spearman')  # Spearman's rho
0.9757575757575757
x.corr(y, method='kendall')   # Kendall's tau
0.911111111111111
