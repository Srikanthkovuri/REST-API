# REST-API
* As we all know REST-API is,
   * A **REST API (Representational State Transfer API)** is a type of **application programming interface (API)** that adheres to the principles of REST architecture.
   * **Uniform Interface**: REST APIs use a uniform interface 
      * typically HTTP
      * with standard methods like GET, POST, PUT, DELETE, etc. 
      * to perform CRUD (Create, Read, Update, Delete) operations on resources.   
**To create a REST-API applications using** 
   * **FASTAPI** framework in python
   * Need to install 'fastapi module',to install it type
   ```bash
   pip install fastapi[standard]
   ```
   * Need to install server 'uvicorn module' to host,for installing
   ```bash
   pip install uvicorn
   ```
## Library
* This folder has all neccessary folders and modules,
   * Which helps in creating Docker container
   * Taking inputs from the user who is executing this, but not from others
   * Storing data in postgres database, Accessing data
   * With the help of pre-defined modules
      * Sqlalchemy
      * FastAPI
      * Uvicorn
   * [ref](https://github.com/Srikanthkovuri/REST-API/tree/main/Library) 
## numeric
* This folder has a module **main.py**,which has
  * Classes for taking inputs
      * NumericReq 
  * Showing outputs
      * NumericRes 
  * Functions for Numeric calucations like addition,subtraction,division, etc.
      * add, sub, mul, div of two numbers 
* For debugging, Run -> add configuration -> fastapi -> 'file-name.py' ->F5
* Now,upon successful execution, we will be able to see **result** in Response-Body on our browser,
  * By requsting to the server where it is hosting
  * By changing Requestclass inputs 
* [refer](https://github.com/Srikanthkovuri/REST-API/tree/main/numeric)

 
## hello.py
* create a file as <file-name.py>
* Now, define function which prints a message like as i did on **hello.py**
* For debugging, Run -> add configuration -> fastapi -> 'file-name.py' ->F5
* As we installed uvicorn server, it will host application on specific server with ip address
* Now,we have to request to that server
* Now,upon successful execution, we will be able to see message on our browser
   * By requsting to the server where it is hosting
* [refer](https://github.com/Srikanthkovuri/REST-API/blob/main/hello.py)

