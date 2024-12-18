1] What is Flask?

    --> Flask is a Python-based web application framework. The Werkzeug WSGI toolkit and the Jinja2 template engine are the foundations of Flask. Both are Pocco initiatives.
    --> Flask is a (microweb)web framework that allows developers to build lightweight web applications quickly and easily with Flask Libraries. 
    --> It was developed(April 1 , 2010) by Armin Ronacher(Australia's Open source Developer), leader of the International Group of Python Enthusiasts(POCCO). 
    --> It is basically based on the WSGI toolkit and Jinja2 templating engine.
    --> WSGI -- Web Server Gateway Interface(standerliz version of web application) --> it's toolkit --> Werkzeuk --> in which implements requests, response objects , and other utility function.  
    

2] Advantages of Flask

    --> Flask is a lightweight backend framework with minimal dependencies.
    --> Flask is easy to learn because its simple and intuitive API makes it easy to learn and use for beginners.
    --> Flask is a flexible Framework because it  allows you to customize and extend the framework to suit your needs easily.
    --> Flask can be used with any database like:- SQL and NoSQL and with any Frontend Technology such as React or Angular.
    --> Flask is great for small to medium projects that do not require the complexity of a large framework.
    --> Single-page applications, RESTful API-based applications, SAS applications, small to medium-sized websites, static websites, Microservices, and serverless apps are all possible.

3] What is WSGI server flask?

    --> The Web Server Gateway Interface (WSGI) is a Python interface that connects web servers and web apps. The Apache HTTP server module mod wsgi makes it possible for Apache to serve Flask applications.

4] Why does a flask need a WSGI server?

    --> Because Flask's development server is designed for ease of development without much configuration for fine-tuning and optimization, you'll definitely need something like a production WSGI server like Gunicorn. Gunicorn, for example, comes in a variety of variants depending on the problem you're attempting to solve.

5] What is Werkzeuk?

    --> Werkzeug (German for "tool") is a BSD-licensed utility package for the Python programming language, essentially a toolkit for Web Server Gateway Interface (WSGI) applications. Software objects for request, response, and utility functions can be created with Werkzeug.

6] installation

    --> python -m venv venv
    --> create --> app.py
    --> python app.py
    or
    --> python -m flask run
    ---------------------------
    #   if name is not app.py
    --> setting environment variable (in windows)
    --> set FLASK_APP=hello.py
    --> set FLASK_ENVIRONMENT=development
    --> flask run
    or
    --> python -m flask run
    ----------------------------
    --> flask run --host=0.0.0.0

7] How does a Flask routing work?

    --> App routing is a technique for mapping a certain URL to a function that is supposed to do a specific activity. It is used to navigate to a certain page in the online application.
    --> app.route(rule, options)
    --> The rule parameter represents URL binding with the function.
    --> The options is a list of parameters to be forwarded to the underlying Rule object.

    --> app.run(host, port, debug, options)
    --> host
        Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally
    --> port
        Defaults to 5000
    --> debug
        Defaults to false. If set to true, provides a debug information
    --> options
        To be forwarded to underlying Werkzeug server.


8] flask request

9] Session Handling

    --> Session handling is a process of managing the interactions between users and servers. The session is created when the user connects to a particular server for the first time. It can last as long as the user needs or it can be terminated by either of the two parties involved in that session.

    --> The project was created to handle sessions without any dependencies on other libraries or frameworks and allows developers to use it with any framework they want. The team also provides a few examples of how it can be used in different applications like an e-commerce website or a social media app.

    --> There are four types of sessions:
        One-time session
        Recurring session
        Scheduled session
        Customized session

    --> For example, when a user logs into your website, his credentials will remain on the server until he logs out, regardless of which web page he sees after entering in. As a result, a session is used to manage this. Session Management is a method used by the Web container to keep track of a user's session information.

10] What are session and cookies ? 

    --> Cookies are client-side files that save user information on a local computer. User data is stored in sessions, which are server-side files. The lifetime of cookies is determined by the user. The session ends when the user closes the browser or logs out of the programme. It can only hold a certain quantity of data

    --> cookies --> made on server --> stored in client side

11] HTTP status codes

    --> The Status-Code element in a server response is a three-digit integer, with the first digit defining the response class and the remaining two digits serving no categorization function. S.N. Code and Description are two of the five possible values for the first digit.
    
        Informational responses ( 100 – 199 )
        Successful responses    ( 200 – 299 )
        Redirection messages    ( 300 – 399 )
        Client error responses  ( 400 – 499 )
        Server error responses  ( 500 – 599 )