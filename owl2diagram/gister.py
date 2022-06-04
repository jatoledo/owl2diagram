import argparse
import sys
import rdflib
from main import get_class_diagram, get_class_hierarchy_diagram, get_object_diagram, get_data_diagram, get_data_prop
from main import get_classes, get_class_hierarchy, get_object_prop, save_diagram
import prefixes


def get_prop_vals(g, properties):
    """
    Get values about the graph itself
    :param g: rdf Graph
    :param properties:
    :return: return values
    """
    vals = []
    t = "select ?val where {?s <%s> ?val}"
    for p in properties:
        results = g.query(t % p)
        for res in results:
            vals.append(res["val"])
    return vals


def get_titles(g):
    """
    According to https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#title
    :param g: rdf Graph
    :return: a list of titles
    """
    props = [
        prefixes.DC+"title",
        prefixes.DCTERMS+"title",
        prefixes.SCHEMA+"name"
    ]
    return get_prop_vals(g, props)


def get_descriptions(g):
    """
    According to https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#description
    :param g: rdf Graph
    :return: a list of descriptions
    """
    props = [
        prefixes.DC+"description",
        prefixes.DCTERMS+"description",
        prefixes.SHEMA+"description",
        prefixes.RDFS+"comment",
        prefixes.SKOS+"note"
    ]
    return get_prop_vals(g, props)


def get_abstracts(g):
    """
    According to https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#abs
    :param g: rdf Graph
    :return: a list of abstracts
    """
    props = [
        prefixes.DC+"abstract",
        prefixes.DCTERMS+"abstract"
    ]
    return get_prop_vals(g, props)


def workflow(ontology_path, output_path, title, desc, abstract):
    # g = rdflib.Graph()
    # g.parse(ontology_path, format=rdflib.util.guess_format(ontology_path))
    class_diagram = get_class_diagram(get_classes(g))
    hierarchy_diagram = get_class_hierarchy_diagram(get_class_hierarchy(g))
    object_diagram = get_object_diagram(get_object_prop(g))
    data_diagram = get_data_diagram(get_data_prop(g))
    save_diagram(class_diagram + hierarchy_diagram + object_diagram + data_diagram, output_path)


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', required=True, help="Ontology file.")
    parser.add_argument('-o', '--output', required=True, help="Output file.")
    parser.add_argument('-t', '--title', action="store_true", help="To look into titles.")
    parser.add_argument('-d', '--description', action="store_true", help="To look into description.")
    parser.add_argument('-a', '--abstract', action="store_true", help="To look into abstract.")

    args = parser.parse_args()
    return args.input, args.output, args.title, args.description, args.abstract


def main():
    input_path, out_path, title, desc, abstract = parse_arguments()
    g = rdflib.Graph()
    g.parse(input_path, format=rdflib.util.guess_format(input_path))
    if title:
        print(get_titles(g))
    if desc:
        get_descriptions(g)
    if abstract:
        get_abstracts(g)

    # save_diagram(diagram)
    # workflow(input_path, out_path, )


if __name__ == "__main__":
    main()






