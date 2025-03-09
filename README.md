About the Project/Project Title

CRUD Python module – A tool for Creating, Reading, Updating and Deleting a MongoDB database to be used by Grazioso Salvare, an international rescue-animal training company. The company also wanted an accompanying dashboard to go along with the CRUD module that would be able to provide a map location of the dog, filter the types of dogs based upon the preferred traits of the rescue dogs and a chart to identify the percentage of eligible dogs in the shelter. 


Motivation

The Motivation for this project is to provide Grazioso Salvare a method to manage a database of rescue-animals located in five of the animal shelters in the Austin, Texas region. Grazioso Salvare would like to be able to identify the age and breed of the dogs that fit the profile of potential search-and-rescue animals.

Getting Started

You must first get the MongoDB CRUD utility up and running to use the Dashboard.

To get a local copy of the MongoDB CRUD utility up and running, follow these simple example steps:
1.	Install MongoDB, mongoimport utility and pymongo driver
2.	Download the animal_shelter.py file
3.	Obtain a copy of the animal_shelter_outcomes.csv file
4.	Import the animal_shelter_outcomes.csv file into a database
5.	Start MongoDB

To get a local copy of the accompanying Dashboard, follow these simple steps:

1.	Follow the above steps to get the CRUD module working
2.	Install dash and pandas
3.	Download the Animal Shelter Dashboard.ipynb Jupyter Notebook file
4.	Edit the Connection Variables in the Animal Shelter Dashboard.ipynb file

Now you can incorporate the animal_shelter.py file into your project to use the create, read update and delete functions in the animal_shelter.py module.

Installation

To use this software, you will need to install the pymongo, pandas and Dash using the following command:

python -m pip install pymongo
pip install dash
pip install pandas
