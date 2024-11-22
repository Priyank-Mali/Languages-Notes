1] API (Application Programming Interface) : 

    API is set of rules and protocols that allows one softwere application to interact to another.

            request
    app1 <-------------> app2
            response
            
            talk(through api)
    
    communication means : exchanging data

2] Key Concepts of APIs:

    1] Endpoints :

    2] HTTP Methods:

        GET       : Fetch data
        POST      : Submit new data.
        PUT/PATCH : Update existing data.
        DELETE    : Remove data.

        (CRUD)
    
    3] Request/Response Format (file formate)   : JSON or XML.

    4] Authentication and Security :

        APIs may require authentication tokens or keys to control access.



3] 1st (SOAP)

    Simple Object Access Protocol
    
    used for exchanging structured information in web services
    
    if both app are written in different languages but still they communicates (through --> XML file formate)

                    request
    app1(python) <-------------> app2(java)
                    response

    XML is language agnostic =>  capable of parsing and processing data, making it a universal format for data exchange.

    XML is a plain text format that can be read and interpreted by any programming language with a suitable parser.


4] process of communication

                    request
    app1(python) <-------------> app2(java)
                    response

    1] 1st : Data Conversion

                      converted
        python data ---------------> XML     

    2] 2nd : (Serialization) now data sending to network 

                bytearray  -> this is called Serialization      
        XML ----------------->  
    
    3] 3rd :  over the network data will reach to app2 
                but app2 only understand XML
 
                    converted into XML -> this is called deserialization
        bytearray ----------------------------> app2(java)


5] As we human we never satisfied

    arguing:
    XML --> is slow and heavy > writing into tags

6] Rest API 

    REST APIs commonly use --> JSON (JavaScript Object Notation) for data exchange.
    
    JSON uses a key-value structure

    REST --> Representational State Transform

    user request to show some graph :

        (graph)     (json)               (python object)        (table/data)
        Frontend -------------> Backend -------------> Database -----------> HardDisk(data in form of 0/1)

        this is how data is transform in different state --> thats why its called --> REST

7] 

    Rest Endpoints -->  are basically we apply -->  CRUD operation on data/resourses 
    
    but how will we do it --> we need some address to perfome 

    EX : address 
        /earth/india/gujarat/surat/flatno/999  
        
        --> this is know in programing world as -- URI (Uniform Resource Identifiers) 

        HTTP method + address --> Rest APIs

    Idempotent :
        An HTTP method is considered idempotent if making multiple identical requests has the same effect as making a single request. 
        In other words, no matter how many times you repeat the same request, the result will always be the same. (safe)

        GET / PUT / DELETE
    
    Non-idempotent : 

        POST :
            POST request multiple times will create multiple resources with unique IDs. (not safe)


8]  REST Message Components:

    1]Request Message Components : sent from the client to the server

        1> HTTP Method 
        
        2> URL (Uniform Resource Locator) : The endpoint or address of the resource
        
        3> Headers : Metadata about the request

                => Content-Type --> XML/JSON
                => Authorization
                => Accept
                => Cache-Control
        
        4> Body : For methods like POST or PUT

                {
                    "name" : "priank"
                }
        
        5> Query Parameters : /?name=priyank?age=99

        6> Path Parameters : /user/{id}/
    
    2] Response Components : response message is sent from the server back to the client 

        1> status code (200 / 201 / 404 / ...)
        2> Headers
        3> Body : actual data returned by the server in formats such as JSON, XML, or HTML.