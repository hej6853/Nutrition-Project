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

def ALT(df):
    y = df['SGPT (ALT) (U/L)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())
#ALT(df)

def GGTP(df):
    y = df['Gamma Glutamyltransferase (GGTP) (U/L)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())
#GGTP(df)

def GLUCOSE(df):
    y = df['Glucose (MG/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#GLUCOSE(df)

def FRUCTOSAMIN(df):
    y = df['Fructosamin (MMOL/L)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#FRUCTOSAMIN(df)

def HBA1C(df):
    y = df['HB A1C (%)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#HBA1C(df)

def BUN(df):
    y = df['Blood Urea Nitrogen (BUN) (MG/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#BUN(df)

def CREATININE(df):
    y = df['Creatinine (MG/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#CREATININE(df)

def ALKALINE_PHOSPHATASE(df):
    y = df['Alkaline Phosphatase (U/L)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#ALKALINE_PHOSPHATASE(df)

def BILIRUBIN_TOTAL(df):
    y = df['Bilirubin Total (MG/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#BILIRUBIN_TOTAL(df)

def PROTEIN(df):
    y = df['Total Protein (G/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#PROTEIN(df)

def ALBUMIN(df):
    y = df['Albumin (G/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#ALBUMIN(df)

def GLOBULIN(df):
    y = df['Globulin (G/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#GLOBULIN(df)

def TRIGLYCERIDES(df):
    y = df['Triglycerides (MG/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#TRIGLYCERIDES(df)

def CHOLESTEROL(df):
    y = df['Cholesterol (MG/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#CHOLESTEROL(df)

def LDL(df):
    y = df['LDL (MG/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#LDL(df)

def VLDL(df):
    y = df['VLDL (MG/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#VLDL(df)

def HDL(df):
    y = df['HDL (MG/DL)']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#HDL(df)

def CHOLESTEROL_RATIO(df):
    y = df['Cholesterol Ratio ']

    for header in df.iloc[:,1:22]:
        x = sm.add_constant(df[f'{header}'])
        mod = sm.OLS(y, x).fit()
        LRresult = (mod.summary2().tables[1])
        pvalue = list(LRresult['P>|t|'])

        if pvalue[1] <= 0.3:
            print(mod.summary())            
#CHOLESTEROL_RATIO(df)