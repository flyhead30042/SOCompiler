from io import StringIO
import logging
from typing import AnyStr, List
import streamlit as st
from soc import RES_DIR
from soc.eli import Eli, MessagesBuilder
from soc.rag import Rag, Rag_GoogleSearch
from pandas import DataFrame 
import os
import pandas as pd
from soc.splitter import RFPTextSplitter


logger = logging.getLogger(__name__)

string_data = None
# Title of the app
st.title("RFP Split")

####################
##     Sidebar    ##
####################
with st.sidebar:
    upload_file = st.file_uploader('Upload a file')
    if upload_file:
        string_data = upload_file.getvalue().decode("utf-8",  errors='ignore').strip()
        # logging.debug(f"read data={string_data}")

####################
##  Main Window   ##
####################
with st.container():
    if string_data:
        splittor = RFPTextSplitter(string_data)
        l = splittor.split()
        df = pd.DataFrame(l, columns=["Series #", "Content"])
        st.write(df)
        
