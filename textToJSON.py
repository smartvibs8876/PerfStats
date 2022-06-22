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
        file.close()

    def convertToJSON(self):
        performanceDict = dict()
        self.readTextFile()
        substr = "seconds time elapsed"
        for line in self.inputTextFileContents:
            fields = line.split()
            if substr in line:
                lineContents = line.split()
                secondsIndex = fields.index("seconds")  
                time = lineContents[secondsIndex-1]
                performanceDict[substr] = time 
            try:
                hashIndex = fields.index("#")
            except ValueError:
                continue
            for character in fields[hashIndex+1]:
                if character.isdigit() == True:
                    performanceDict[fields[hashIndex-1]] = " ".join(fields[hashIndex+1:]) 
                    break 
        JSONObject = json.dumps(performanceDict, indent = 4)
        with open(self.outputJSONFile, "w") as outputFile:
            outputFile.write(JSONObject)

try:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[1].replace(".txt","")+"-"+sys.argv[2]+".json"
    textToJSONInstnce = TextToJSON(inputFileName,outputFileName)
    textToJSONInstnce.convertToJSON()
except IndexError:
    print("Invalid command line arguments")
