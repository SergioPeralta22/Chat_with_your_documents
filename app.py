import streamlit as st


def main():
    st.set_page_config(page_title="Chat with your documents", page_icon="📝")

    st.header("Chat with your documents")
    st.subheader("Upload your PDFs and start chatting with it!")

    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDFs here and click on 'Process'")
        st.button("Process")


if __name__ == "__main__":
    main()
