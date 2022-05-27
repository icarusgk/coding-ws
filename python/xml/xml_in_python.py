import os

from lxml import etree

xml_string = "<a><b>hello</b></a>"

# * From text to XML

root = etree.fromstring(xml_string)  # Returns an element

# * dump() function
etree.dump(root)
# <a>
#   <b>hello</b>
# </a>

# * From file to XML
# Use the parse function, returns an ElementTree

xml_path = "xml_file.xml"
tree = etree.parse(xml_path)
print(type(tree))  # <class 'lxml.etree._ElementTree'>

root = tree.getroot()
print(type(root))  # <class 'lxml.etree._Element'>


# * Access the information in an XML document
os.chdir('python')
os.chdir('xml')

xml_file = 'xml_file.xml'
root = etree.parse(xml_file).getroot()

print("Printing the root of the file")
etree.dump(root[1])

states = root[2]
for state in states:
    print(state.text)

# California
# Texas
# Florida
# Hawaii

attr_xml_file = 'xml_file1.xml'
root = etree.parse(attr_xml_file).getroot()

# The get() method is used to access the specified attribute.
states = root[0]
for state in states:
    print(state.get('name'))

# Hawaii
# Florida
# Texas
# California

# The keys() and items() methods can be used to get
# all attributes of a tag:

print(root.keys())
# ['name', 'capital']
print(root.items())
# [('name', 'United Stated of America'), ('capital', 'Washington')]

xml_string = "<a><b>hello</b></a>"
root = etree.fromstring(xml_string)  # returns an Element

# The function tostring() takes an element and returns
# a bytes object that can be later saved to a file.
print(etree.tostring(root))  # b'<a><b>hello</b></a>'

# The method write() saves an instance of ElementTree directly to a file.
# If we have worked with a lxml Element,
# we should convert it to ElementTree first.
tree = etree.ElementTree(root)
tree.write("xml2_write_file.xml")
