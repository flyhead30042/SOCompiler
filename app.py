from soc.eli import Eli, MessagesBuilder
from soc.rag import Rag_GoogleSearch
import logging
import os.path
from io import BytesIO
import streamlit as st


logger = logging.getLogger(__name__)

st.set_page_config(
 page_title="App",
 page_icon=":world_map:️",
 layout="wide",
 initial_sidebar_state="expanded"
)

#################
## Main Window ##
#################
st.write("# Welcome to SoComplier! 👋")
with st.container():
    st.write(f"This is main windows")


#############
## Sidebar ##
#############
with st.sidebar:
 st.write(f"This is side bar")