# Neighbourhood
>[Peninah Njeri](https://github.com/peninah-njeri)  
  
# Description  
This project allows users to post their hood, posts, police stations and businesses around their neighbourhood
##  Live Link  
 Click [View Site](.....)  to visit the site
  
## User Story  
  
* A user can view different neighbourhoods  
* A user can post their neighbourhood   
* Search for businesses  
* A user can write a post for other users to see
* A user can view their profile page. 
* A user can add a business name that is near the neigbourhood 
  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
```bash
https://github.com/peninah-njeri/neighborhood
```
##### Navigate into the folder and install requirements  
 ```bash
 cd Neighborhood pip install -r requirements.txt 
 ```
##### Install and activate Virtual  
```bash
- python3 -m venv venv - source venv/bin/activate
```
##### Install Dependencies  
```bash
 pip install -r requirements.txt 
``` 
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations watch
 ``` 
 Now Migrate
```bash
python manage.py migrate 
```
##### Run the application  
```bash
python manage.py runserver 
```
##### Testing the application  
```bash
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently. 
  
## Contact Information   
If you have any queries or contributions, please email me at [peninahgathuru@gmail.com]  
  
## License 
* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)]
* Copyright (c) 2019 **Pesh**