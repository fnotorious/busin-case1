import json
import requests
##from xml.etree import ElementTree             <- uncomment this line of code if you want to attempt XML

response = requests.get("http://www2.miami-dadeclerk.com/Developers/api/OfficialRecords/xml?parameter1=1992&parameter2=R438823&authKey=E28FA24F-3EEA-4D11-8630-22D6FE606328")

data = response.json()
print(json.dumps(data, indent=4))

#string_xml = response.content                  <- uncomment this line of code if you want to attempt XML
#tree = ElementTree.fromstring(string_xml)      <- uncomment this line of code if you want to attempt XML