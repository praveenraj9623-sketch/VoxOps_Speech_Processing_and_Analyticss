import streamlit as st

TITLE = "VoxOps — Speech Processing & Analytics"
FILE_TYPES = ["wav", "mp3", "flac"]

st.set_page_config(page_title=TITLE, layout="wide")
st.title(TITLE)
st.info("Prototype in progress. Model processing is being implemented.")

uploaded = st.file_uploader(
    "Upload a sample file",
    type=FILE_TYPES,
)

if uploaded is not None:
    st.write({
        "filename": uploaded.name,
        "size_bytes": uploaded.size,
    })
    st.caption("Upload received. No model inference has run yet.")
