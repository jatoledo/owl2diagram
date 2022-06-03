
class_query = """
SELECT * WHERE { 
?class a owl:Class .
#?class rdfs:comment ?cm .
   FILTER (!isBlank(?class)) 
   }
"""

hierarchy_query = """
SELECT ?subClass ?superClass
WHERE {
    ?subClass rdfs:subClassOf ?superClass .
    FILTER (!isBlank(?superClass)) 
}
"""

dataProp_query = """

select distinct ?prop  ?class   where {
  ?prop rdf:type owl:DatatypeProperty    .
  ?prop rdfs:domain ?class .
  FILTER (!isBlank( ?class)) 
}	
"""

objectProp_query = """
select ?domain ?prop ?range where { 
  ?prop rdf:type owl:ObjectProperty.
  ?prop rdfs:domain ?domain.
  ?prop rdfs:range ?range.
  FILTER (!isBlank( ?prop)).
  FILTER (!isBlank( ?domain)) .
  FILTER (!isBlank( ?range)) .
}
"""