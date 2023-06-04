import pandas
import streamlit as st
import pandas as pd
import zipfile


menu_items={
        "Get help": "https://yourwebsite.com/help",
        "Report a bug": None,  # This will hide the 'Report a bug' item.
        "About": "https://yourwebsite.com/about",
    }

st.set_page_config(page_title= "COMPANY WEBSITE",layout="wide", menu_items={
        "Get help": "https://yourwebsite.com/help",
        "Report a bug": None,  # This will hide the 'Report a bug' item.
        "About": "https://yourwebsite.com/about",
    })

st.header("RegenesisAI")
st.write(""" RegenensisAI is a pioneering biotech company focused on revolutionizing the field of regenerative medicine 
    through the application of artificial intelligence (AI). With a mission to develop personalized regenerative therapies and medicines, RegenensisAI harnesses the power of AI and
     machine learning algorithms to transform the way we approach age-related degenerative diseases and injuries.

    This innovative company combines cutting-edge technology with the expertise of a multidisciplinary team of scientists
     and researchers. RegenensisAI's AI-driven approach enables the identification of novel therapeutic targets, the design 
     of new drugs and therapies, and the accurate prediction of treatment outcomes with unprecedented precision. By optimizing 
     the research and development process, RegenensisAI reduces time and costs associated with traditional methods, 
     expediting the delivery of safe, effective, and affordable regenerative solutions.
    
    RegenensisAI emphasizes collaboration and partnerships, actively seeking to leverage the expertise of other biotech 
    companies and research institutions. By fostering collaborative efforts, RegenensisAI accelerates the development of new 
    therapies and treatments, bringing hope to millions of individuals suffering from age-related degenerative diseases and injuries.
    
    With a commitment to patient-centric care, RegenensisAI prioritizes the development of non-invasive treatments that minimize patient 
    discomfort and recovery time. By focusing on improving patient compliance and treatment efficacy, RegenensisAI aims to enhance overall patient outcomes and quality of life.""")

st.subheader("The Team...")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

with col1:
    ## iterate over only the FIRST four rows...
    for index, row in df[:4].iterrows():
        ## Add members first and last name...
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        ## add member's role in the company///
        st.write(row["role"])
        ## add members photo....
        st.image("images/" + row["image"])

# Add content to the second column....

with col2:
    ## iterate of rows 4 to 7...
    for index, row in df[4:8].iterrows():
        ## Add members first and last names...
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        ## Add members role in the company...
        st.write(row["role"])
        ## Add a members photo...
        st.image("images/" + row["image"])

with col3:
    ## iterate over rows 4 to 7...
    for index, row in df[8:].iterrows():
        ## Add members first and last names...
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        ## Add members role in the company...
        st.write(row["role"])
        ## Add the photo....
        st.image("images/" + row["image"])



























