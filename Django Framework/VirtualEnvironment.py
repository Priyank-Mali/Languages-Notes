'''
-> How to Set Up a Virtual Environment in Python 
-> Why It's Useful

When developing software with Python, a basic approach is to install Python 
on your machine, install all your required libraries via the terminal, 
write all your code in a single .py file or notebook, 
and run your Python program in the terminal.

This works fine for simple Python scripting projects. 
But in complex software development projects, like building a Python library,
an API, or software development kit, often you will be working with multiple files, multiple packages, and dependencies. 
As a result, you will need to isolate your Python development environment for that particular project.


Consider this scenario: you are working on app A, using your system installed Python and you pip install packageX version 1.0 to your global Python library. 
Then you switch to project B on your local machine, and you install the same packageX but version 2.0, which has some breaking changes between version 1.0 and 2.0.


When you go back to run your app A, you get all sorts of errors, and your app does not run. This is a scenario you can run into when building software with Python. 
And to get around this, we can use virtual environments.



A virtual environment in Python is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. 
It allows you to create an isolated environment for your Python projects, ensuring that each project can have its own dependencies regardless of what dependencies are installed globally on your system



steps:

-> pip install virtualenv

-> python -m venv <virtual-environment-name>
    make sure:
        mkdir projectA
        cd projectA
        python3.8 -m venv env

-> Activate:
    env/Scripts/activate.bat //In CMD
    env/Scripts/Activate.ps1 //In Powershel

-> Now you can Install packages using ->Ex:...  pip install django

-> pip list 

-> pip freeze > requirements.txt (You can name this requirements.txt file whatever you want.)

To recreate your development environment, your friend will just need to follow the above steps to activate a new virtual environment.
Instead of having to install each dependency one by one, they could just run the code below to install all your dependencies within their own copy of the project:

-> pip install -r requirements.txt

-> deactivate



Python virtual environments give you the ability to isolate your Python development projects from your system installed Python and other Python environments. 
This gives you full control of your project and makes it easily reproducible.

When developing applications that would generally grow out of a simple .py script or a Jupyter notebook, 
it's a good idea to use a virtual environment.
'''