# Nutrition-Project
![image](https://user-images.githubusercontent.com/79428102/124829551-9f0ec600-df2d-11eb-804a-94e0d3abbfe3.png)

The food and nutrition project helps our project client Jim (anonymous) learn to make healthy food choices, improve energy and alertness, reduce disease and illness risks, and gain knowledge of nutrients through the data-driven analysis.

## Motivation
The food and nutrition project helps our project client Jim (alias) learn to make healthy food choices, improve energy and alertness, reduce disease and illness risks, and gain knowledge of nutrients through the data-driven analysis. 

## Dataset
We received 6,400 hundred rows of nutritional data going back to 2014 that told us how many meals he ate in a day plus the nutritional content for each meal, including calories, fat content, carbohydrates, protein, cholesterol, sodium, potassium, Vitamins A and C, Calcium, and Iron. We also received some weight data. Jim also provided us with the results of eight blood tests done between 2009 and 2019, though we only used the five tests from 2014 to 2019 in order to compare bloodwork with the other variables gathered like the nutritional data. Jim also has a very active lifestyle and has tracked the type and length of exercise he has done since 2014. He primarily does High intensity interval training, Brazilian Jiu Jitsu, and weight training combined with cardio. Finally, we also have about a years worth of sleep data going back to early 2020. There are periods of time that we don’t have data for which we had to keep in mind when doing our analysis. For most of 2016, Jim did not track his meals. It can be challenge when analyzing this data and not knowing whether, for example, Jim didn’t exercise for several months or if he simply wasn’t recording exercise for that period of time. As we continue to undergo this analysis, communication with Jim will be important to make sure we have the information that we need. 

## Built With
● Python
● VBA
● Excel 
● Tableau

## Key Skills Learned
● ARIMA, Auto regression
● Advanced statistic (time-series data forcasting)
● Correlation matrix 
● ETL (Dataframe Transform)
● Python regression analysis 

### ARIMA CODE
```
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
```

### Regression Analysis
```
import pandas as pd
import statsmodels.api as sm
import warnings

warnings.simplefilter('ignore', category=UserWarning)

df = pd.read_excel("RegressionData.xlsx")

def CHECKALL(df):
    for ys in df.iloc[:,23:41]:
        y = df[f'{ys}']
        for header in df.iloc[:,1:22]:
            x = sm.add_constant(df[f'{header}'])
            mod = sm.OLS(y, x).fit()
            LRresult = (mod.summary2().tables[1])
            pvalue = list(LRresult['P>|t|'])

            if pvalue[1] <= 0.05:
                print(mod.summary())
CHECKALL(df)

def AST(df):
    y = df['SGOT (AST) (U/L)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())
#AST(df)
```

## Conclusion
![image](https://user-images.githubusercontent.com/79428102/124829657-b8b00d80-df2d-11eb-88ed-a741225d6e56.png)

Our models indicate that trans fat and saturated fat have a positive relationship with LDL, meaning that decreasing trans and saturated fat intake may decrease LDL levels. With LDL levels indicating borderline high on the client’s recent bloodwork, our client may want to keep monitoring their change. In addition,  our client can investigate the proposed correlation matrix to see what ingredients have negative and positive relationships one another affiliated with his diet habit. Finally, we recommend that our client continue to monitor cholesterol levels to make sure they stay in the healthy range.

## License
© hej6853
