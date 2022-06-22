import json
import requests

class Comparison:
    def __init__(self,file1,file2):
        self.file1 = file1
        self.file2 = file2
        file1 = open(self.file1)
        file2 = open(self.file2)
        self.file1Contents = json.load(file1)
        self.file2Contents = json.load(file2)
        file1.close()
        file2.close()
    
    def compare(self):
        if float(self.file1Contents["seconds time elapsed"]) < float(self.file2Contents["seconds time elapsed"]):
            self.sendSlackNotification(self.file1+" is better")
        else:
            self.sendSlackNotification(self.file2+" is better")
    
    def sendSlackNotification(self,message):
        #curl -X POST -H 'Content-type: application/json' --data '{"text":"'${nodeStatusDictionary[$nodeName]}'"}' https://hooks.slack.com/services/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
        url = 'https://hooks.slack.com/services/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'
        payload = {'text':message}
        request = requests.post(url, json = payload)
        print(request.text)

comparison = Comparison("output1.json","output2.json")
comparison.compare()