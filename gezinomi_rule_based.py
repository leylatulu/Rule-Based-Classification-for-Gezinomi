import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df_ = pd.read_excel('gezinomi.xlsx')
df = df_.copy() 

def general_information(df):
    print("_____ INFO _____")
    print(df.info(), end='\n\n')
    print("_____ DESCRIPTION _____")
    print(df.describe().T, end='\n\n')
    print("_____ SHAPE _____")
    print(df.shape,end ='\n\n')
    print("_____ MISSING _____")
    print(df.isnull().sum().sort_values(ascending=False), end='\n\n')
    print("_____ QUANTILE _____")
    print(df.quantile([0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99, 1]).T, end='\n\n')
    print("_____ UNIQUE _____")
    print(df.nunique(), end='\n\n')
    print("_____ HEAD _____")
    print(df.head(), end='\n\n')
    print("_____ TAIL _____")
    print(df.tail(), end='\n\n')
    print("_____ SAMPLE _____")
    print(df.sample(5), end='\n\n')

general_information(df)

df.SaleCityName.unique()
df.SaleCityName.value_counts()


df.ConceptName.unique()
df.ConceptName.value_counts()

df.groupby('SaleCityName')['Price'].sum()
df.groupby('ConceptName')['Price'].count()
df.groupby('SaleCityName')['Price'].mean()
df.groupby('ConceptName')['Price'].mean()
df.groupby(['SaleCityName', 'ConceptName'])['Price'].mean()

df["EB_Score"] = pd.cut(df.SaleCheckInDayDiff, bins=[-1, 7, 30, 90, df.SaleCheckInDayDiff.max()], labels = ["Last Minuters", "Potential Planners", "Planners", "Early bookers"])


new_df = df.groupby(['SaleCityName', 'ConceptName', 'EB_Score']).agg({'Price': ['mean', 'count']})
new_df

agg_df = df.groupby(['SaleCityName', 'ConceptName', 'Seasons']).agg({'Price': ['mean']}).sort_values(by=[('Price', 'mean')], ascending=False)
agg_df.head()

agg_df.index
agg_df.reset_index(inplace = True)

agg_df["sales_level_based"] = (agg_df.SaleCityName + "_" + agg_df.ConceptName + "_" + agg_df.Seasons).apply(lambda x: x.upper())
agg_df.head()

agg_df.columns = agg_df.columns.droplevel(1)

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})



customer1 = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df.sales_level_based == customer1]

customer2 = "GIRNE_YARIM PANSIYON_LOW"
agg_df[agg_df.sales_level_based == customer2]