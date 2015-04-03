import xml.etree.ElementTree as ET

db = ET.parse("senticnet3.rdf.xml")
root = db.getroot()
print(root)
