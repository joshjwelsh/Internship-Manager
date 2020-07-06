import json
import sys

filename = 'InternJob.txt'

class Application():
    def __init__(self, comp_name):
        self.name = comp_name
        self.response = 'waiting'

    def __str__(self):
        print(self.name)

    def updateFile(self):
        self.my_App = {
            'name':self.name,
            'response':self.response
        }
        with open(filename,'a+') as f:
            json.dump(self.my_App,f)


if len(sys.argv) == 2:
    app = Application(sys.argv[1])
    app.updateFile()
