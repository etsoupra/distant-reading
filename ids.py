import xml.etree.ElementTree as ET
tree = ET.parse('Datasets_ID.xml')
root = tree.getroot()
header = root[2].getiterator()
iter_ = root[2].getiterator()

ns = {'id': 'http://www.openarchives.org/OAI/2.0/'}
for header in root[2].findall('id:header', ns):
    identifier = header.find('id:identifier', ns)
    print identifier.text
