from abc import abstractmethod
from typing import List
from googlesearch import search
from itertools import islice


class Rag():
    def __init__(self, top_k:int=3) -> None:
        self.top_k = top_k
    
    @abstractmethod   
    def searh (self, query) -> List:
        pass


class Rag_GoogleSearch(Rag):
    def search(self, query, top_k=3) -> List:
         results = search(query, num_results=10, lang="en")
         self.results: list =  list(islice(results, self.top_k))       
         return self.results
    


if __name__ == "__main__":
    rag = Rag_GoogleSearch(5)
    results = rag.search("CCES stands for what?")

    print(", ".join(results))
