import xml.etree.ElementTree as ET

from colors import show_colors

tree = ET.parse('MenuColor06.xml')
root = tree.getroot()

parts = []
rgbs = []


for part in root.iter('string'):
    parts.append((part.attrib['name'], part.text))

    rgb = part.text.split(',')
    rgbint = [int(i) for i in rgb] 
    rgbs.append(rgbint)

show_colors(rgbs)
