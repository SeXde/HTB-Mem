import requests
import re
import hashlib

sesion = requests.session()

url = "http://206.189.121.131:32172"

getResponse = sesion.get(url)

rawResponse = getResponse .content.decode('utf-8')

cleanGetResult = re.findall('[A-Za-z0-9]{20}',rawResponse)[0]

md5String = hashlib.md5(cleanGetResult.encode('utf8')).hexdigest()

data={'hash': md5String}


postResponse = sesion.post(url = url, data = data).content.decode('utf-8')

cleanPostResponse = re.findall('HTB{.*}',postResponse)[0]

print('\nThe flag is: ' + '\'' + cleanPostResponse + '\'')