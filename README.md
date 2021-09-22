CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Data Source
 
INTRODUCTION
------------

The idea of the project is to build movie recommendation engine to predict user behaviour and recommend based on the relevence to the user and movie. Recommendations build on Rank based, user collaborative filtering and matix factorization (Funk SVD)

REQUIREMENTS
------------
* Numpy
* Pandas
* streamlit


DATA SOURCE
------------
The data has been gathered from MovieTweeting https://github.com/sidooms/MovieTweetings.


SETUP
------------
* The zip contains the necessary file and data in order to run the application.
* Check the requirement file and install the necessary libraies.
* In the terminal window run the main.py file.
* I have used a web application to display my result( Streamlit). A webpage url will popup. 
* Initially for the first run it will created a model from the data and stores in a pickle file.
* Once the model has been stored in a pickel, we are ready to make recommendations.
* In the left side of the sidebar you can select "User" or "Movie" inorder to find recommendations for users and recommendation based on movie respectively.

Example
------------
| User_id       | Movie_id           
| ------------- |:-------------:
| 53856         | 14142 
| 66            | 15324      
| 53966         | 2638984      


DATA PREPROCESSING
-----------
The data preprocessing has been done in the Recommendation data notebook for your reference.
