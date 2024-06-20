import streamlit as st 

def main(): 
    st.set_page_config(page_icon=":scroll:",page_title="Briefly")
    st.header("Chat With Your Documents :scroll:")
    input = st.text_input("Enter Question !")

    with st.sidebar: 
        st.subheader("Upload Your Documents")
        st.file_uploader("upload your files here", accept_multiple_files=True)
        st.button(":package: Process")

if __name__ == "__main__": 
    main()