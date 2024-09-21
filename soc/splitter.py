from typing import AnyStr, List, Union

class RFPTextSplitter():
    def __init__(self, data:AnyStr):
        self.data = data
    
    def split(self, line_delimiter:AnyStr="\r\n",  serial_delimiter:AnyStr=" ") -> List:      
        l =[]    
        texts = self.data.split(line_delimiter)
        for text in texts:
            words = text.strip().split(serial_delimiter, 1)
            l.append(words if len(words) > 1 else [words[0], ""])
        return l
    
    def split(self, split_desc:AnyStr) --> List: 
        pass