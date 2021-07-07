import pandas as pd
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import warnings

warnings.simplefilter('ignore', category=UserWarning)

dataset = "Paleo"

series = pd.read_csv(f'{dataset}.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

for header in series.iloc[:,11:17]:        
    index_no = series.columns.get_loc(f'{header}')
    arima_model = ARIMA(series[f'{header}'], order=(1,0,1)).fit()
    pred = arima_model.predict(dynamic=False)
    rmse = mean_squared_error(series[f'{header}'], pred, squared=False)

    print(arima_model.summary())
    print(f"RMSE = {rmse}")

    pyplot.plot(series[f'{header}'])
    pyplot.plot(pred, color='red')       
    pyplot.title(f'{series.columns[index_no]} intake over time ({dataset})')
    pyplot.xlabel('Date')
    pyplot.ylabel(f'{series.columns[index_no]}')
    pyplot.show()