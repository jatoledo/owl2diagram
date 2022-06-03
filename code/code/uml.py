
# Class
class_ = """
    {% for element in elements %}
    class {{ element }} {
    
    }
{% endfor %}

"""
class2 = """
{% for element in elements %}
class "{{ element }}" {

}
{% endfor %}

"""
# class with data property
hierarchyClass ="""
    {% for key, value in elements.items() %}
    {{ value }} <|-- {{ key }} 
    {% endfor %}
"""
hierarchyClass2 ="""
    {% for key, value in elements.items() %}
    "{{ value }}" <|-- "{{ key }}" 
    {% endfor %}
"""
# Object properties
objectProperties = """
{% for key , value in elements.items() %}
{{ value[0] }}  --> {{ value[1] }}   :{{ key }}  
{% endfor %}
"""
dataProperties = """
    {% for key , value in elements.items() %}
    class {{ key }}  {
    
    {% for prop in value %}
        {{ prop }}  
     {% endfor %}
    } 
    {% endfor %}
"""