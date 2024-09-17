# Library
* This folder has all neccessary folders and modules,
   * Which helps in creating Docker container [ref](https://github.com/Srikanthkovuri/REST-API/blob/main/Library/Docker-compose.yml)
   * Taking inputs from the user who is executing this, but not from others
   * Storing data in postgres database, Accessing data
   * With the help of pre-defined modules
      * Sqlalchemy
      * FastAPI
      * Uvicorn
## api
* This folder has a module **models.py** which has classes
   * BookReq
      * Has attributes which helps in taking inputs from the user who is executing
   * BookRes
      * Has attributes which will display all the inputs given by user on the browser in 'response body'   
   *[ref](https://github.com/Srikanthkovuri/REST-API/blob/main/Library/api/models.py) 
## db
* This folder has two modules
   * **datbase.py**
      * This module helps in creating connection with database
      * [ref](https://github.com/Srikanthkovuri/REST-API/blob/main/Library/db/database.py) 
   * **models.py**
      * This module has class
      * It will create table with the neccessary fields and values given by user i.e from api->models.py
      * It will create table with the name given and fileds with the attributes it has
      * [ref](https://github.com/Srikanthkovuri/REST-API/blob/main/Library/db/models.py)   
## main.py
* This module has two functions
   * **create_book**
      * This function helps in passing values which was taken from user
      * storing it in database
   * **get_books**
      * This function helps in returning the values
* [ref](https://github.com/Srikanthkovuri/REST-API/blob/main/Library/main.py)   