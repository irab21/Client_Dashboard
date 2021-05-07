import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go

#titles
st.title('Client Report FY 2020-2021')
st.sidebar.title('Client 1')

st.markdown('### By My Company')
st.sidebar.markdown('### A Review of the past year ')

DATA_URL= dummy_data.xlsx


@st.cache(persist =True)
def load_data():
	data = pd.read_excel(DATA_URL)
	return data


data = load_data()



st.sidebar.markdown("### Numbeber Of Joinings, Declines, and Pending")
st.write('The visual depicts the number of Joinings, Declines and the still Pending offers in the FY 2020-21')
select= st.sidebar.selectbox('Visualization',['Pi Chart'], key=1)

#newdataframe
status_count= data['Status'].value_counts()
status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})


st.markdown('### Numbeber Of Joinings, Declines And Pending')

if select=='Pi Chart':
	fig=px.pie(status_count, values='Count',names='Status')
	st.plotly_chart(fig)


st.sidebar.markdown("### Selection TAT")



selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']]
selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Count':selection_tat_count.values})

#st.write(selection_tat_count)
st.markdown('### Selection TAT')
if st.sidebar.checkbox('Visual',True,key=1):
	fig=px.bar(selection_tat_count,x='Selection TAT',y='Count', color='Count', text='Count',title='Max, Average and Min TAT For Selection')
	fig.update_traces(texttemplate='%{text:.4s}', textposition='outside')
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

	st.plotly_chart(fig)

st.sidebar.markdown("### Offer TAT")

offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']]
offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'values':offer_tat_count.values})

st.markdown('### Offer TAT')
st.write('This is a visual of Maximum, minimum and Average Time taken by Airtel Paymnets Bank for converting a selection to offer.')
if st.sidebar.checkbox('Visual',True,key=2):
	fig1=px.bar(offer_tat_count,x='Offer TAT',y='values', color='values',text='values')
	fig1.update_traces(texttemplate='%{text:.4s}', textposition='outside')
	fig1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
	fig1.update_layout(barmode='group', xaxis_tickangle=-45)
	st.plotly_chart(fig1)
