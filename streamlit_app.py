import streamlit
streamlit.title('New line is added')
streamlit.title('Updating streamlite data through this app!!')
streamlit.header('Breakfast menu ....')
streamlit.text('avcado')
streamlit.text('kala, splinach')
streamlit.text('almond milk')
streamlit.text('toasted Bread')

import pandas  as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
