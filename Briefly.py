import streamlit as st

def main(): 
    st.set_page_config(page_icon=":scroll:", page_title="Briefly")
    st.header("Chat With Your Documents :scroll:")
    st.chat_input("Ask Question !")    

    with st.sidebar: 
        st.subheader(":package: Upload Your Documents ")
        st.file_uploader("Click Proceess to Upload files")
        st.button("Proceess")

if __name__ == '__main__': 
    main()
