import streamlit as st


from streamlit_option_menu import option_menu


st.set_page_config(page_title="nCesta",page_icon=":tada",layout="wide")


with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["","Page 2","Page 3","Page 4","Page 5"],
        icons=['house',"filter", 'graph-up', 'upload',"laptop"],
        menu_icon="cast",
        default_index=1,
    )

if selected == "":
    st.title('Home Page')

if selected =="Page 2":
    st.title('Page 2')


if selected =="Page 3":
    st.title('Page 3')

if selected =="Page 4":
    st.title('Page 4')


if selected =="Page 5":
    st.title('Page 5')
