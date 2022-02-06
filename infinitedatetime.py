import datetime

class ____________________________________________: 
    def __init__(self, depth):
        self._depth = depth

    def __getattr__(self, name):
        if name == "datetime":
            if self._depth == 1:
                return datetime.datetime
            return ____________________________________________(self._depth-1)
        return getattr(datetime, name)

def __getattr__(name: str):
    if name == "__path__":
        return []

    return ____________________________________________(int(name[1:])) 

