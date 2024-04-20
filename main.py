# Yash Patel
# Project start date: 1-8-24
# Extract points of interest and their attributes (name, coordinates, address, category, hours of operation, reviews, number of reviews, and ratings) from log file and print in a structured XML file

# 1-8-24: Researched programming concepts required for project (regular expressions, XML processing, etc.)
# 1-13-24: Wrote preliminary python code which extracts points of interest from log file using regular expression patterns
# 1-17-24: Wrote code to print extracted points of interest to XML file
# 1-20-24: Made XML file more structured using .toprettyxml() from minidom
# 1-22-24: Regular expression patterns were incorrect but fixed name_pattern this day
# 2-10-24: Rewrote regular expression patterns for coordinates and number of reviews
# 2-15-24: Rewrote regex pattern for name attribute (fixed it)

import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Define the regular expression patterns for the attributes
name_pattern = re.compile(r':0x[a-fA-F0-9]+\\\",\\\"([\w\s\u4e00-\u9fff-]+)\\\",null,')
coordinates_pattern = re.compile(r'\[null,null,(-?\d+\.\d+),(-?\d+\.\d+)\]')
# address_pattern = re.compile(r'(?:null,){3}\\"([^"]*São Paulo - SP, \d{5}-\d{3}, Brazil)\\"(?:,null){5,6}')

# category_pattern = re.compile(r'\[\\"[A-Za-z]+ [A-Za-z]+\\",\\"[A-Za-z]+\\"\],\\"[A-Za-z]+\\",null,null,null,')
# hours_pattern = re.compile(r'\[\\\"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\\\",\[\\"Open 24 hours\\"\]')
reviews_pattern = re.compile(r'\\\"([\d,]+ reviews)\\\"')
num_reviews_pattern = re.compile(r',(\d+)],null,null,\[')
# ratings_pattern = re.compile(r'\s*(\d+(\.\d+)?)/\d+')

# Open the log file
with open('demofile2.txt', 'r') as file:
    data = file.read()

# Extract the points of interest
name = name_pattern.findall(data)
coordinates = coordinates_pattern.findall(data)
# address = address_pattern.findall(data)
# category = category_pattern.findall(data)
# hours = hours_pattern.findall(data)
reviews = reviews_pattern.findall(data)
num_reviews = num_reviews_pattern.findall(data)
# ratings = ratings_pattern.findall(data)

# Create the XML file
root = ET.Element("root")

for i in range(len(name)):
    point_of_interest = ET.SubElement(root, "point_of_interest")
    ET.SubElement(point_of_interest, "name").text = name[i]
    if i < len(coordinates):
        coords = ET.SubElement(point_of_interest, "coordinates")
        lat, lon = coordinates[i]
        ET.SubElement(coords, "latitude").text = lat
        ET.SubElement(coords, "longitude").text = lon
    # ET.SubElement(point_of_interest, "address").text = address[i]
    # ET.SubElement(point_of_interest, "category").text = category[i]
    # ET.SubElement(point_of_interest, "hours").text = hours[i]

    reviews_elem = ET.SubElement(point_of_interest, "reviews")
    ET.SubElement(reviews_elem, "numberOfReviews").text = num_reviews[i] if i < len(num_reviews) else ""
    # ET.SubElement(reviews_elem, "ratings").text = ratings[i]

# Create a string representation with line breaks and indents
xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")

# Write the XML file with line breaks and indents
with open("output.xml", "w") as file:
    file.write(xml_str)

print("\nPoints of interest and their attributes have been printed to 'output.xml'.")
