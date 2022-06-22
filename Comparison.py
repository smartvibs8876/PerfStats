import json
import requests
import sys

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
        try:
            package1,release1 = sys.argv[1].split("-")
            release1 = release1.replace(".json","")
            package2, release2 = sys.argv[2].split("-")
            release2 = release2.replace(".json","")
        except IndexError:
            print("Invalid command line arguments")
        
        if float(self.file1Contents["seconds time elapsed"]) < float(self.file2Contents["seconds time elapsed"]):
            difference = float(self.file2Contents["seconds time elapsed"]) - float(self.file1Contents["seconds time elapsed"])
            message = "package " + package1 + " of release " + release1 + " is better than " + "package " + package2 + " of release " + release2 + " by "+ str(difference)
            print(message)
            #self.sendSlackNotification(message)
        else:
            difference = float(self.file1Contents["seconds time elapsed"]) - float(self.file2Contents["seconds time elapsed"])
            message = "package " + package2 + " of release " + release2 + " is better than " + "package "+ package1 + " of release " + release1 + " by "+ str(difference)
            print(message)
            #self.sendSlackNotification(message)

    def sendSlackNotification(self,message):
        #curl -X POST -H 'Content-type: application/json' --data '{"text":"'${nodeStatusDictionary[$nodeName]}'"}' https://hooks.slack.com/services/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
        url = 'https://hooks.slack.com/services/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'
        payload = {'text':message}
        request = requests.post(url, json = payload)
        print(request.text)

try:
    comparison = Comparison(sys.argv[1],sys.argv[2])
    comparison.compare()
except IndexError:
    print("Invalic command line arguments")