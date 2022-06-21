import json
import requests

class TextToJSON:
    def __init__(self,inputTextFile,outputJSONFile):
        self.inputTextFile = inputTextFile
        self.outputJSONFile = outputJSONFile
        self.inputTextFileContents = ""

    def readTextFile(self):
        file = open(self.inputTextFile, 'r')
        self.inputTextFileContents = file.readlines()
    
    def sendSlackNotification(self,performanceObject):
        #curl -X POST -H 'Content-type: application/json' --data '{"text":"'${nodeStatusDictionary[$nodeName]}'"}' https://hooks.slack.com/services/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
        url = 'https://hooks.slack.com/services/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'
        print(performanceObject)
        payload = {'text':performanceObject}
        request = requests.post(url, json = payload)
        print(request.text)

    def convertToJSON(self):
        performanceDict = dict()
        self.readTextFile()
        substr = "seconds time elapsed"
        #index = 0
        for line in self.inputTextFileContents:
            fields = line.split()
            #index += 1
            if substr in line:
                lineContents = line.split()
                time = lineContents[0]
                performanceDict[substr] = time 
            try:
                hashIndex = fields.index("#")
            except ValueError:
                #print("# value doesnt exist for line :-",index)
                continue
            performanceDict[fields[hashIndex-1]] = fields[hashIndex+1] 
        JSONObject = json.dumps(performanceDict, indent = 4)
        with open(self.outputJSONFile, "w") as outputFile:
            outputFile.write(JSONObject)

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
        if float(self.file1Contents["seconds time elapsed"]) < float(self.file1Contents["seconds time elapsed"]):
            self.sendSlackNotification(self.file1+" is better")
        else:
            self.sendSlackNotification(self.file2+" is better")
    
    def sendSlackNotification(self,message):
        #curl -X POST -H 'Content-type: application/json' --data '{"text":"'${nodeStatusDictionary[$nodeName]}'"}' https://hooks.slack.com/services/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
        url = 'https://hooks.slack.com/services/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'
        payload = {'text':message}
        request = requests.post(url, json = payload)
        print(request.text)


textToJSONInstnce = TextToJSON("perfOut1.txt","output1.json")
textToJSONInstnce.convertToJSON()
textToJSONInstnce = TextToJSON("perfOut2.txt","output2.json")
textToJSONInstnce.convertToJSON()
comparison = Comparison("output1.json","output2.json")
comparison.compare()