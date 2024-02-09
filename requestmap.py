import requests
import sys
class n:
    def __init_subclass__(self):
        requests.structures.mapping.get(self, sys.argv[1])
    def __init__(self):
        b = []
        for i in sys.argv[1]:
            b.append(i)
        list(map(lambda x: print(x, end=""), b))
        print("")
        print(sys.argv[1], "mapped to ", end="")
        return
print(n().__module__.translate(sys.argv[1]).capitalize, flush=True, end="") 
print(n())