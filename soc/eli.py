import logging
import sys
from typing import AnyStr, Union, List
import warnings

from soc import ELI_API_KEY, ELI_API_URL
warnings.filterwarnings("ignore")
import requests
from soc.rag import Rag_GoogleSearch

logger = logging.getLogger(__name__)

class Eli():
    def __init__(self, model:str="mistral", max_new_tokens:int=128, temperature:float=0.3) -> None:
        self.model = model
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        
    def chat(self, messages) -> str:
        try:
            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": self.temperature,
                "max_new_tokens": self.max_new_tokens,
                "stream": True,  # Set to false if you do not want streamed response
            }  
            logger.debug(f"payload:{payload}")    
            headers = {
                "Authorization": f"Bearer {ELI_API_KEY}",
                "Content-Type": "application/json",
            }
            logger.debug(f"headers:{headers}")
      
            
            response = requests.post(
                f"{ELI_API_URL}/api/v1/llm/chat_stream",
                json=payload,
                headers=headers,
                timeout=(300, 300),
                verify=False,
            )
            output = []
            for part in response.iter_content():
                part = part.decode("utf8")
                output.append(part)
                # print(part, end="", flush=True)  # <- print stream content to console
            # print()
            output_str = "".join(output)
            logger.debug(f"output:{output_str}")
            return output_str
        except Exception as ex:
            return f"An error occurred: {ex}"

class MessagesBuilder():
    # @staticmethod
    # def format(question:AnyStr, system_message:str = None, rag_results: AnyStr = None) -> List:
    #     if system_message is None:
    #         system_message = "Follow the instructions carefully and give short and direct answers."

    #     if rag_results:
    #         prompt = f""" Answer questions based on the following information: {rag_results}.
    #         Question: {question}
    #         """.strip()
    #     else:
    #         prompt = f"Question: {question}".strip()
            
    #     return [
    #         {"role": "system", "content": system_message},
    #         {"role": "user", "content": prompt},
    #     ]
    @staticmethod        
    def format(question:AnyStr, system_message:AnyStr| None = None, rag_results: AnyStr | None = None) -> List:
        messages=[]
        if system_message:
            messages.append({"role": "system", "content": system_message})
        # else:
        #     system_message = "Follow the instructions carefully and give short and direct answers."
        
        if rag_results:
             prompt = f""" Answer questions based on the following information: {rag_results}.
             Question: {question}""".strip()
        else:
             prompt = f"{question}".strip()
        
        messages.append({"role": "user", "content": prompt},)
             
        return messages