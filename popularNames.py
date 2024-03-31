import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Popular Name Trends')


url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

name = st.text_input('Enter a name for the graph', value='John')
name_df = df[df['name']==name]

st.header(f'{name} over time')

tab3, tab4 = st.tabs(['Graph','Chart'])

with tab3:
#Graph 
    plot_df = name_df[name_df['sex']=='M']
    fig = px.line(title=f'Usage of {name} over Time')
    fig.add_scatter(x=plot_df['year'], y=plot_df['n'], mode='lines', name='Male', line_color = 'blue')
    plotF = name_df[name_df['sex']=='F']
    fig.add_scatter(x=plotF['year'], y=plotF['n'], mode='lines', name='Female', line_color = 'pink')
    st.plotly_chart(fig)

with tab4:
    nameDF = name_df.sort_values('n', ascending=False).head(5)
    nameDF = nameDF.drop(columns = 'name')
    nameDF['year'] = nameDF['year'].astype(str)
    nameDF.index = [1,2,3,4,5]
    st.dataframe(nameDF)

with st.sidebar:

    letter = st.text_input('Select a Letter for the Table', value='A')
    letter = letter.upper()
    letterName = df[df['name'].str.startswith(letter, na=False)]
    
    year = st.slider('Choose a year', 1910, 2021)
    
    tab1, tab2 = st.tabs(['Female','Male'])
    with tab1:
        
        st.header(f'Top female names starting with {letter} and in {year}')
        year_df = letterName[letterName['year']==year]
        girls = year_df[year_df.sex=='F'].sort_values('n', ascending=False).head(5)['name']
        girls.index = [1,2,3,4,5]
        st.dataframe(girls)
    
    with tab2:
        st.header(f'Top male names starting wtih {letter} and in {year}')
        year_df = letterName[letterName['year']==year]
        boys = year_df[year_df.sex=='M'].sort_values('n', ascending=False).head(5)['name']
        boys.index = [1,2,3,4,5]
        st.dataframe(boys)