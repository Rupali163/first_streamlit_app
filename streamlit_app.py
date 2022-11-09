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
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
