import streamlit as st
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with your documents", page_icon="📝")

    st.header("Chat with your documents")
    st.subheader("Upload your PDFs and start chatting with it!")

    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing your documents..."):
            # get pdf text

            # get pdf embeddings

            # create vector store


if __name__ == "__main__":
    main()
