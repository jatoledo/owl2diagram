import rdflib
from jinja2 import Template
from code.query import class_query, hierarchy_query, dataProp_query, objectProp_query
from code.uml import class_, hierarchyClass, dataProperties, objectProperties
import os
class_template = Template(class_)
hierarchyClass_template = Template(hierarchyClass)
dataProperties_template = Template(dataProperties)
objectProperties_template = Template(objectProperties)

def get_name(url):
    a = url.find('#')
    if a > -1:
        return url.split("#")[-1]
    else:
        return url.split("/")[-1]

g = rdflib.Graph()
#g.parse('core.owl', format="xml")
file='core2.owl'
g.parse(file, format=rdflib.util.guess_format(file))

# Get Class
l = []
for r in g.query(class_query):
    l.append(get_name(r["class"]))

class_diagram = class_template.render(elements=l)
# get hierarchy class
data = {}
for r in g.query(hierarchy_query):
    data[get_name(r["subClass"])] = get_name(r["superClass"])

hierarchyClass = hierarchyClass_template.render(elements=data)
print(hierarchyClass)

# get dataProp
csvDicData_ = dict()
for r in g.query(dataProp_query):
    csvDicData_.setdefault(get_name(r["class"]), []).append(get_name( r["prop"]))

dataProperties = dataProperties_template.render(elements=csvDicData_)


# get Object Prop
objectProp = dict()
for r in g.query(objectProp_query):
    objectProp.setdefault(get_name(r["prop"]), []).append(get_name(r["domain"]))
    objectProp.setdefault(get_name(r["prop"]), []).append(get_name(r["range"]))


# print(objectProp)
objectProp = objectProperties_template.render(elements=objectProp)


f = open("diagram.txt", "w")
# skinparam linetype ortho\n
f.write("@startuml\n" + class_diagram + hierarchyClass + dataProperties + objectProp + "\n@enduml")
f.close()
#os.system('java -jar plantuml.jar  -tsvg webapp/static/assets/img/diagram.txt')



output = ('''
```mermaid
classDiagram''' +dataProperties+'''
```
''')
print(output)
f = open("diagram4.md", "w")
f.write(output)
f.close()