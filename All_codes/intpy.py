from lxml import etree

# Parse the XML file
tree = etree.parse('xml_file.xml')

# Define the XPath expression to find the desired elements
xpath_expr = '//title'

# Use XPath to find elements
elements = tree.xpath(xpath_expr)

# Iterate over the elements and print their text content
for element in elements:
    print(element.text)
