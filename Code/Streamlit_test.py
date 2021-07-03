
import streamlit as st
import plotly
plotly.offline.init_notebook_mode()
import plotly.express as px
import pandas as pd
import cufflinks as cf
cf.set_config_file(theme='solar',sharing='public',offline=True) #List of Cufflinks Themes :  ['ggplot', 'pearl', 'solar', 'space', 'white', 'polar', 'henanigans']
import holoviews as hv
import hvplot
import hvplot.pandas

st.title("Australian Economy Analysis")

aud_exchange_df = pd.read_csv("../Data/RawData/AUDexchange.csv")
st.dataframe(aud_exchange_df.head(10))

del aud_exchange_df["Time"]
for column in aud_exchange_df.columns:
    aud_exchange_df[column] = aud_exchange_df[column]  / aud_exchange_df[column].abs().max()
      

plot1 = aud_exchange_df.iplot(kind='line',
                             yTitle='ExchangeRates',
                             asFigure=True)

st.write(plot1)

