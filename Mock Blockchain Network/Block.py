import hashlib
import json
from flask import Flask


app = Flask(__name__)


class CreateBlock:
    
    def hashdata(self,inputdata):
        encoded = inputdata.encode()
        hashvalue = hashlib.sha256(encoded)
        hex = hashvalue.hexdigest()
        return hex
    
    def mineblock(self,data):
        index =0
        nonce =0

        hashedvalue = ""

        while (index == 0):
            finaldata = str(data)+ str(nonce)
            hashedvalue = self.hashdata(finaldata)
            first4hash = hashedvalue[0:4]
            nonce+=1

            if (first4hash == "0000"):
                break
        
        return nonce,hashedvalue

    
    def createBlock(self,Blocknumber,data):
        numtostr = str(Blocknumber)
        dicttostr = str(data)
        data_to_be_mined = numtostr + dicttostr

        value_nonce,hash_value_mined = self.mineblock(data_to_be_mined)
        
        finalBlock = {
        "BLOCK NUMBER": Blocknumber,
        "NONCE": value_nonce,
        "DATA TX": data,
        "HASH": hash_value_mined}

        finalBlockdict = json.dumps(finalBlock, indent=4)

        return finalBlockdict


@app.route('/')
def blockcreation():

    block = CreateBlock()

    a = block.createBlock(1,
    {"Hello":"MynameisFasih",
    "StupidIdiot": "GetLost"})
    
    return a



"""    
@app.route('/')
def blockcreation():
    a = createBlock(6565656,{"TEST": "TEST1", "TEST2": "TEST4"})
    return a


#print (a)    
"""