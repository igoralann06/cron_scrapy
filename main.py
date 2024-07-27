import streamlit as st
import pandas as pd
import os

list_of_lists = []
list_of_lists.append(["rebuy"])
list_of_lists.append(["kleinanzeigen"])
list_of_lists.append(["vinted"])
df = pd.DataFrame(list_of_lists, columns=['Script'])

def refresh():
    st.rerun()

if st.button('Refresh'):
    refresh()

st.table(df)

if os.path.isfile("kleinanzeigen.csv"):
  with open('kleinanzeigen.csv') as f:
     st.download_button('kleinanzeigen CSV', f, file_name='kleinanzeigen.csv')

file_list=os.listdir("vinted")
for vinted_csv in file_list:
    with open("vinted/" + vinted_csv) as f:
        st.download_button(vinted_csv, f, file_name=vinted_csv)
