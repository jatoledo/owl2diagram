```mermaid
	classDiagram

    
    class Organization {
    
    }

    class Researcher {
    
    }

    class Student {
    
    }


    

Organization  --> Researcher   :hasMember  

Student  --> Researcher   :hasMentor  

Researcher  --> Organization   :partOf  

    
    class Organization  {
    
    
        foundedIn  
     
    } 
    
```