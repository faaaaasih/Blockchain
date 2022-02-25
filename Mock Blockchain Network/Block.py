import hashlib
import json

def hashdata(inputdata):
    encoded = inputdata.encode()
    hashvalue = hashlib.sha256(encoded)
    hex = hashvalue.hexdigest()
    return hex

"""
def calculateNonce(inputhexvalue):  #assume the threshold is 0000....
    nonce = 0 
    for 
"""

def createBlock(BlockNumber, Data):
    numtostr = str(BlockNumber)
    dicttostr = json.dumps(Data)

    index = 0
    nonce = 0
    hashedvalue = ""

    while (index==0):
        finaldata = str(numtostr + dicttostr) + str(nonce)
        hashedvalue = hashdata(finaldata)

        first4hash = hashedvalue[0:4]

        if (first4hash == "0000"):
            break
        
        nonce +=1
    
    finalBlock = {
        "BLOCK NUMBER": BlockNumber,
        "NONCE": nonce,
        "DATA TX": Data,
        "HASH": hashedvalue
    }

    finalBlockdict = json.dumps(finalBlock, indent=4)

    return finalBlockdict


a = createBlock(1,{"TEST": "TEST1", "TEST2": "TEST4"})

print (a)

    
