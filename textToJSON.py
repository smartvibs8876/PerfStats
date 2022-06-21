import json
import sys

class TextToJSON:
    def __init__(self,inputTextFile,outputJSONFile):
        self.inputTextFile = inputTextFile
        self.outputJSONFile = outputJSONFile
        self.inputTextFileContents = ""

    def readTextFile(self):
        file = open(self.inputTextFile, 'r')
        self.inputTextFileContents = file.readlines()

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

print(sys.argv[1],sys.argv[2])
textToJSONInstnce = TextToJSON(sys.argv[1],"output1.json")
textToJSONInstnce.convertToJSON()
textToJSONInstnce = TextToJSON(sys.argv[2],"output2.json")
textToJSONInstnce.convertToJSON()