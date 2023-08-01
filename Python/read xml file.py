import xml.etree.ElementTree as ET 


t = ET.parse('book.xml')
root = t.getroot()
print(root)
print(root[0].attrib)
print(root[5][0].text) 

