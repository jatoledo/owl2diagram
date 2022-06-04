
    ```mermaid
    classDiagram
    
    class Feature {
    
    }

    class Alojamiento {
    
    }

    class BedAndBreakfast {
    
    }

    class Hostel {
    
    }

    class Hotel {
    
    }

    class LodgingBusiness {
    
    }

    class Motel {
    
    }

    class Albergue {
    
    }

    class Alojamiento {
    
    }

    class Apartahotel {
    
    }

    class Hostal {
    
    }

    class Hotel {
    
    }

    class Concept {
    
    }


    
    LodgingBusiness <|-- BedAndBreakfast 
    
    LodgingBusiness <|-- Hostel 
    
    Hotel <|-- Hotel 
    
    LodgingBusiness <|-- Motel 
    
    Alojamiento <|-- Alojamiento 
    
    Alojamiento <|-- Apartahotel 
    
    Alojamiento <|-- Hostal 
    
    Alojamiento <|-- Albergue 
    

Alojamiento  --> Concept   :categoria  

    
    class Alojamiento  {
    
    
        numCamas  
     
        numHabitaciones  
     
    } 
    
    ```
    