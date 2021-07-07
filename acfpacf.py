import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

header = "Sodium..mg."

series = pd.read_csv('paleo.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

# Create figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Make ACF plot
plot_acf(series[{header}], lags=10, zero=False, ax=ax1)

# Make PACF plot
plot_pacf(series[{header}], lags=10, zero=False, ax=ax2)

plt.show()
