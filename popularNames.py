import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Popular Name Trends')


url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

name = st.text_input('Enter a name for the graph', value='John')
name_df = df[df['name']==name]

st.header(f'{name} over time')


#Graph 
plot_df = name_df[name_df['sex']=='M']
fig = px.line(data_frame=plot_df, x='year', y='n', title=f'Usage of {name} over Time')
plotF = name_df[name_df['sex']=='F']
fig.add_scatter(x=plotF['year'], y=plotF['n'], mode='lines', name='Female')
st.plotly_chart(fig)

with st.sidebar:

    letter = st.text_input('Select a Letter for the Table', value='A')
    letterName = df[df['name'][0]==letter]
    
    tab1, tab2 = st.tabs(['Female','Male'])
    with tab1:
        
    year = st.slider('Choose a year', 1910, 2021)
    st.header(f'Top names by {letter} and {year}')
    year_df = letterName[letterName['year']==year]
    girls = year_df[year_df.sex=='F'].sort_values('n', ascending=False).head(5)['name']
    girls.index = [1,2,3,4,5]
    st.dataframe(girls)
    
    with tab2:
        year = st.slider('Choose a year', 1910, 2021)
        st.header(f'Top names by {letter} and {year}')
        year_df = letterName[letterName['year']==year]
        boys = year_df[year_df.sex=='M'].sort_values('n', ascending=False).head(5)['name']
        boys.index = [1,2,3,4,5]
        st.dataframe(boys)