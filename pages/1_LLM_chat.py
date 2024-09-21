import logging
from typing import AnyStr, List
import streamlit as st
from soc.eli import Eli, MessagesBuilder
from soc.rag import Rag, Rag_GoogleSearch
from pandas import DataFrame 

logger = logging.getLogger(__name__)

# Title of the app
st.title("LLM Chat")

####################
##     Sidebar    ##
####################

with st.sidebar:

   # model selection and setup
   # Dropdown menu for model selection
   model_options = ["mistral", "llama3.1", "phi3"]
   selected_model = st.selectbox("Select a model:", model_options, index=0)

   # Slider for temperature
   temperature = st.slider("Select temperature:", min_value=0.0, max_value=1.0, value=0.3, step=0.01)

   # Slider for max tokens
   max_tokens = st.slider("Select max tokens:", min_value=1, max_value=4096, value=2048, step=1)

   llm = Eli(model=selected_model, max_new_tokens=max_tokens, temperature= temperature)

   
   # rag selection and setup
   # Multiselect for Google Search 
   rag_options = ["None", "Google Search"]
   rag_option = st.selectbox("Enable RAG", options=rag_options)
   
   # Slider for top k
   top_k = st.slider("Select top k:", min_value=1, max_value=5, value=2, step=1)

   rag = None
   if rag_option in "Google Search":
      rag = Rag_GoogleSearch(top_k)



####################
##  Main Window   ##
####################
with st.container():
   
# Text area for question input
   question = st.text_area("Enter your question:", "Ericsson CCES stands for what?")
   submit_btn = st.button("Submit")
   with st.expander("RAG Details"):
      rag_placeholder = st.empty()
   response_placeholder = st.empty()
   response_placeholder.text_area("Response:", "", height=200)
  
   
# Button to submit the question
   if submit_btn:
      
      rag_results= None
      if rag:
         l = rag.search(question)
         rag_results  = ", ".join(l)
         df = DataFrame(data= l, columns=["Source"]) 
         rag_placeholder.table(df)
         logging.info(f"rag result={rag_results}")
   
   
      messages = MessagesBuilder.format(rag_results=rag_results, question=question)
      logging.info(messages)
      result = llm.chat(messages)           

      logging.info(f"llm result={result}")
   
      # Update area
      response_placeholder.text_area("Response:", result, height=200)
     


