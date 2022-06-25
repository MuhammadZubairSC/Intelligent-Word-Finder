import json
from difflib import get_close_matches


class Dictionary_():
    
    def __init__(self):
        self.data = json.load(open("data.json"))
    
    def translate(self, w):
        w = w.lower()
        if w in self.data:
            return self.data[w]
        elif w.title() in self.data:
            return self.data[w.title()]
        elif w.upper() in self.data: #in case user enters words like USA or NATO
            return self.data[w.upper()]
        elif len(get_close_matches(w, self.data.keys())) > 0:
            return "Did you mean %s instead?" % (''.join(get_close_matches(w, self.data.keys())[0:1]))
        else:
            return "The word doesn't exist. Please double check it."