import pandas as pd
import pmdarima as pmd

dataset = "Paleo"
series = pd.read_csv(f'{dataset}.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

def arimamodel(series):
    for header in series.iloc[:,0:17]:        
        seriesarray = series[f'{header}']
        autoarima_model = pmd.auto_arima(seriesarray, 
                                start_p=1, 
                                start_q=1, 
                                max_p=3, 
                                max_q=3, 
                                test="adf", 
                                trace=True, 
                                stepwise=True, 
                                seasonal=True, 
                                random_state=20, 
                                n_fits=50)
        print(autoarima_model.summary())

arimamodel(series)
