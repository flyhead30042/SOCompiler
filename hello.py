from soc.eli import Eli, MessagesBuilder
from soc.rag import Rag_GoogleSearch
import logging


logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # messages = MessagesBuilder.format(
    #         rag= "Cloud Core Exposure Server (CCES) is a API exposure platform supporting NEF, SCEF and EES.", 
    #         question= "CCES stands for what?")

    question= "Ericsson CCES stands for what?"
    model = "mistral"
    rag = Rag_GoogleSearch()
    results = rag.search(question, 5)
    # messages = MessagesBuilder.format(question)  
    # messages = MessagesBuilder.format(question= question, 
                                    #   system_message = "Follow the instructions carefully and give short and direct answers.")      
    messages = MessagesBuilder.format(question= question, 
                                      system_message = "Follow the instructions carefully and give short and direct answers.", 
                                      rag_results= ", ".join(results))  

    
    llm = Eli(model)
    logger.info(f"llm chat response: {llm.chat(messages)}" )