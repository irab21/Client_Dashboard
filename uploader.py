import streamlit as st

temp_file = st.file_uploader("Enter file here!")
if temp_file: 
	temp_file_contents = temp_file.read()

if st.button("Save as working file"):
    with open("ON_DISK_FILE.extension","wb") as file_handle:
        file_handle.write(temp_file_contents)
