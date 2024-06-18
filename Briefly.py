import streamlit as st

def main(): 
    st.set_page_config(page_icon=":scroll:", page_title="Briefly")
    st.header("Chat With Your Documents :scroll:")
    st.chat_input("Ask Question !")    

if __name__ == '__main__': 
    main()
