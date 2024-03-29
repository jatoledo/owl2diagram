__author__ = "Jhon Toledo"
__credits__ = ["Jhon Toledo"]
__copyright__ = "Copyright © 2023 Jhon Toledo"

__license__ = "Apache-2.0"
__maintainer__ = "Jhon Toledo"
__email__ = "ja.toledo@upm.es"


# __main__.py

import sys
import rdflib
from jinja2 import Template
from .query import class_query, hierarchy_query, dataProp_query, objectProp_query
from .uml import class_, hierarchyClass, dataProperties, objectProperties,objectPropertiesList

class_template = Template(class_)
hierarchyClass_template = Template(hierarchyClass)
dataProperties_template = Template(dataProperties)
objectProperties_template = Template(objectProperties)
objectPropertiesList_template = Template(objectPropertiesList)

def get_name(url):
    a = url.find('#')
    if a > -1:
        name = url.split("#")[-1]
        # return url.split("#")[-1]
    else:
        name = url.split("/")[-1]
        # return url.split("/")[-1]
    for ch in ['-', '_', ':']:
        name = name.replace(ch, '')
    return name
def get_classes(g):
    # Get Class
    l = []
    for r in g.query(class_query):
        l.append(get_name(r["class"]))
    return l
def get_class_diagram(classes):
    class_diagram = class_template.render(elements=classes)
    return class_diagram


def get_class_hierarchy(g):
    # get hierarchy class
    data = {}
    for r in g.query(hierarchy_query):
        data[get_name(r["subClass"])] = get_name(r["superClass"])
    return data


def get_class_hierarchy_diagram(data):
    hierarchyClass = hierarchyClass_template.render(elements=data)
    return hierarchyClass


# get dataProp
def get_data_prop(g):
    csvDicData_ = dict()
    for r in g.query(dataProp_query):
        csvDicData_.setdefault(get_name(r["class"]), []).append(get_name(r["prop"]))
    return csvDicData_


def get_data_diagram(data):
    dataProperties = dataProperties_template.render(elements=data)
    return dataProperties


def get_object_prop(g):
    # get Object Prop
    objectProp = dict()
    for r in g.query(objectProp_query):
        objectProp.setdefault(get_name(r["prop"]), []).append(get_name(r["domain"]))
        objectProp.setdefault(get_name(r["prop"]), []).append(get_name(r["range"]))
    return objectProp


def get_object_diagram(data):
    if type(data) == dict:
        objectProp = objectProperties_template.render(elements=data)
    else:
        objectProp = objectPropertiesList_template.render(elements=data)
    return objectProp


def save_diagram(diagram, output_path):
    """
    :param diagram:
    :return:
    """
    output = "```mermaid\n"
    output += "\tclassDiagram\n"
    output += diagram
    output += "\n```"
    # print(output)
    f = open(output_path, 'w')
    f.write(output)
    f.close()


def workflow(ontology_path, output_path):
    g = rdflib.Graph()
    g.parse(ontology_path, format=rdflib.util.guess_format(ontology_path))
    class_diagram = get_class_diagram(get_classes(g))
    hierarchy_diagram = get_class_hierarchy_diagram(get_class_hierarchy(g))
    # print("get object prop")
    # print(get_object_prop(g))
    object_diagram = get_object_diagram(get_object_prop(g))
    data_diagram = get_data_diagram(get_data_prop(g))

    #print(class_diagram)
    save_diagram(class_diagram + hierarchy_diagram + object_diagram + data_diagram, output_path)
    # save_diagram(class_diagram + object_diagram, output_path)
def main():
    """Generate a diagram of a given ontology"""
    workflow(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()