# Nutrition-Project
![image](https://user-images.githubusercontent.com/79428102/124829551-9f0ec600-df2d-11eb-804a-94e0d3abbfe3.png)

The food and nutrition project helps our project client Jim (anonymous) learn to make healthy food choices, improve energy and alertness, reduce disease and illness risks, and gain knowledge of nutrients through the data-driven analysis.

## Motivation
The food and nutrition project helps our project client Jim (alias) learn to make healthy food choices, improve energy and alertness, reduce disease and illness risks, and gain knowledge of nutrients through the data-driven analysis. 

## Dataset
We received 6,400 hundred rows of nutritional data going back to 2014 that told us how many meals he ate in a day plus the nutritional content for each meal, including calories, fat content, carbohydrates, protein, cholesterol, sodium, potassium, Vitamins A and C, Calcium, and Iron. We also received some weight data. Jim also provided us with the results of eight blood tests done between 2009 and 2019, though we only used the five tests from 2014 to 2019 in order to compare bloodwork with the other variables gathered like the nutritional data. Jim also has a very active lifestyle and has tracked the type and length of exercise he has done since 2014. He primarily does High intensity interval training, Brazilian Jiu Jitsu, and weight training combined with cardio. Finally, we also have about a years worth of sleep data going back to early 2020. There are periods of time that we don’t have data for which we had to keep in mind when doing our analysis. For most of 2016, Jim did not track his meals. It can be challenge when analyzing this data and not knowing whether, for example, Jim didn’t exercise for several months or if he simply wasn’t recording exercise for that period of time. As we continue to undergo this analysis, communication with Jim will be important to make sure we have the information that we need. 

## Data Preprocessing
![image](https://user-images.githubusercontent.com/79428102/128901036-5cb95742-7aa1-4068-ad8e-09895b2dc52b.png)
First step in going about this project was to get the data and examine what we needed to do in moving forward. For example, there were time periods where we were missing data or had minimal food entries so we had to come with a plan on how we were going to clean the data. Data cleaning was an important step that we worked on before going into exploratory analysis to see what kind of insights we may be able to pull from our data. The primary datasets that we worked with revolved around exercise, bloodwork, and nutrition. Since we knew that our client had played around with going on different diets, we wanted to figure out when these changes were so that we could compare these time periods and the health outcomes. From our exploratory analysis, we found that our client was on the Paleo diet in 2014, starting on Keto later in 2017. Now, Chesta is going to talk about these two different diets. 

![image](https://user-images.githubusercontent.com/79428102/128901183-5fbabe24-d004-4d8d-b713-77c2929995f5.png)
During the data pre-processing, we felt the necessity of having a relative value for each category, that is, a fat, carbohydrates, and protein percentage compared to the total amount of calories. Because it wouldn’t make sense to compare 100 grams of protein against 3000 calories versus 200 grams of protein against  2000 calories. In this case, we used fat in grams times 9 divided by total calories, carbs and protein in grams times 4 divided by total calories!

# Data Exploration
![image](https://user-images.githubusercontent.com/79428102/128901596-632f53bc-685a-40f5-bdc4-f253563c5872.png)

# Analysis
![image](https://user-images.githubusercontent.com/79428102/128901952-12e39368-2eb2-4b86-a1be-493c76982ea9.png)
The LDL level as known as a bad cholesterol, it reached border high levels after the Keto Diet. The fats linked to LDL cholesterol levels are related to certain type of fat called saturated fats and trans fats. Saturated fats in products that usually come from animals, such as meat, milk, cheese, and butter. Also, when trans-fat enters the body, it pushes unsaturated fat and takes its place, causing abdominal problems, lowering HDL and raising LDL, causing various vascular diseases.

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
