import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
myworkspace="C:/DATA/Lehre/GeodataAnalysisAndModelling2020/covid19"
#inputdata=myworkspace+"/"+"time_series_19-covid-Confirmed.csv"
inputdata=myworkspace+"/"+"full_data.csv"
df=pd.read_csv(inputdata, sep=",")#, dtype={"date":str, "location":int, "new_cases":int, "total_cases":int, "total_deaths":int})
df.dtypes
df["date"].astype('str')
df.astype({'date': 'str'}).dtypes
popIT=60480000.0
popCH=8570000.0
popFR=70000000.0
popDE=82790000.0
popAU=8822000.0

#extract the country dataframes
df_IT=df[df.location=="Italy"]
df_CH=df[df.location=="Switzerland"]
df_FR=df[df.location=="France"]
df_DE=df[df.location=="Germany"]
df_AU=df[df.location=="Austria"]

#IT add day counting from case no. 100
df_IT["countIT"]=0
daycounter=0
for index, row in df_IT.iterrows():
    if row["total_cases"]>=100:
        daycounter+=1
        df_IT.set_value(index, "countIT",daycounter)

#CH add day counting from case no. 100
df_CH["countCH"]=0
daycounter=0
for index, row in df_CH.iterrows():
    if row["total_cases"]>=100:
        daycounter+=1
        df_CH.set_value(index, "countCH",daycounter)

#FR add day counting from case no. 100
df_FR["countFR"]=0
daycounter=0
for index, row in df_FR.iterrows():
    if row["total_cases"]>=100:
        daycounter+=1
        df_FR.set_value(index, "countFR",daycounter)

#DE add day counting from case no. 100
df_DE["countDE"]=0
daycounter=0
for index, row in df_DE.iterrows():
    if row["total_cases"]>=100:
        daycounter+=1
        df_DE.set_value(index, "countDE",daycounter)

#AU add day counting from case no. 100
df_AU["countAU"]=0
daycounter=0
for index, row in df_AU.iterrows():
    if row["total_cases"]>=100:
        daycounter+=1
        df_AU.set_value(index, "countAU",daycounter)


#plot the data
plt.plot(df_IT.countIT, df_IT.total_cases/popIT*1000000.0, label="IT", color="blue")
plt.plot(df_CH.countCH, df_CH.total_cases/popCH*1000000.0, label="CH", color="red")
plt.plot(df_FR.countFR, df_FR.total_cases/popFR*1000000.0, label="FR", color="green")
plt.plot(df_DE.countDE, df_DE.total_cases/popDE*1000000.0, label="DE", color="yellow")
plt.plot(df_AU.countAU, df_AU.total_cases/popAU*1000000.0, label="AU", color="black")
plt.legend(loc="best", frameon=False)
#plt.yscale("log")
plt.ylabel("no. of cases per 1 mio. inhabitants")
plt.xlabel("days after 100th case")
plt.show()

