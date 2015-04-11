import xml.etree.ElementTree as ET

def add_underscore(s):
    return s.replace(' ', '_')

db = ET.parse("senticnet3.rdf.xml")
root = db.getroot()

cl = root.getchildren()
master_dict = {}

for child in cl:
    concept = add_underscore(child.find('{http://sentic.net/api}text').text)
    raw_semantics = child.findall('{http://sentic.net/api}semantics')
    semantics = []
    for el in raw_semantics:
        semantics.append(el.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource'].split('/')[-1])

    pleasantness = child.find('{http://sentic.net/api}pleasantness').text
    attention = child.find('{http://sentic.net/api}attention').text
    sensitivity = child.find('{http://sentic.net/api}sensitivity').text
    aptitude = child.find('{http://sentic.net/api}aptitude').text
    polarity = child.find('{http://sentic.net/api}polarity').text

    master_dict[concept] = {
            'name': concept,
            'semantics': semantics, 
            'pleasantness': pleasantness, 
            'attention': attention,
            'sensitivity': sensitivity,
            'aptitude': aptitude,
            'polarity': polarity
        }
print '['
for c in master_dict:
    print master_dict[c],','
print ']'
