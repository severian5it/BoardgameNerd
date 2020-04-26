<div align="center">
    <h1>  Boardgame Archive </h1>
</div>

<div align="center">
    <a href="https://boardgame-nerd.herokuapp.com/"> View  Live Website</a>
</div>

## Introduction

BoardGame Archive has been created by Pierluca Del Buono to serve Boardgame Geeks to manage their
collection. The site allow visitors to search a vast catalogue of Boardgame, add them to their 
collection, and writing notes and assigning scores


## Table of Contents
1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
1. [Features](#features)
1. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Storage Types](#data-storage-types)
    - [Collections Data Structure](#collections-data-structure)
        - [Users Collection](#users-collection)
        - [Boardgame Collection](#boardgame-collection)
1. [Technologies Used](#technologies-used)
1. [Testing](#testing)
1. [Deployment](#deployment)
[Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
1. [Credits](#credits)
1. [Contacts](#contacts)
1. [Disclaimer](#disclaimer)

# UX

## User stories

As a user of BoardGame Archive I expect/need/want:

1. to search a wide catalogue of boardgame.
1. to be informed about what is hot in the boardgame community.
1. to add a boardgame to my collection.
1. to remove a boardgame to my collection.
1. to find the best fit game to the number of my friends, I want to filter my search results by 
   number of players.
1. to find the best fit game to the time I have, I want to filter my search results by 
   duration.
1. as a father/ mother, I want to know suggested age of a boardgame .
1. to add/update a rating to the boardgame I own.
1. to add/update a review to the boardgame I own.
1. to be able to connect to their social media channels, to be informed about new features.
1. to be easily in contact with the website manager via a contact form.
1. to have informative feedback from the website regarding the interaction, including a clear information
about loading status and pop up and modals when my actions are completed successfully.
1. to navigate the site also from mobile or from table, in way that the site is responsive to different
kind of device

## Wireframes

Wireframe mockups, created using [Balsamiq](https://balsamiq.com/), are available in diffent format:
 1. Laptop
    1. [Landing](wireframes/landing/LandingLaptop.pdf)
    1. [Search](wireframes/search/SearchLaptop.pdf)
    1. [Search Details](wireframes/searchDetails/SearchDetailsLaptop.pdf)
    1. [Collection](wireframes/collection/collectionLaptop.pdf)
    1. [Collection Details](wireframes/collectionDetails/collectionDetailsLaptop.pdf)
 1. Tablet
     1. [Landing](wireframes/landing/LandingTablet.pdf)
     1. [Search](wireframes/search/SearchTablet.pdf)
     1. [Search Details](wireframes/searchDetails/SearchDetailsTablet.pdf)
     1. [Collection](wireframes/collection/collectionTablet.pdf)
     1. [Collection Details](wireframes/collectionDetails/collectionDetailsTablet.pdf)
 1. Mobile
     1. [Landing](wireframes/landing/LandingMobile.pdf)
     1. [Search](wireframes/search/SearchMobile.pdf)
     1. [Search Details](wireframes/searchDetails/SearchDetailsLaptop.pdf)
     1. [Collection](wireframes/collection/collectionMobile.pdf)
     1. [Collection Details](wireframes/collectionDetails/collectionDetailsMobile.pdf)
     
Modal not dependent on the device:
   1. [Log in](wireframes/modal/loginModal.pdf)
   1. [Register](wireframes/modal/registerModal.pdf)

# Features

# Information Architecture
## Database Choice

a NoSQL database has been selected for his low latency response, keeping in mind the need to scale up 
increasing the number of user and query.
MongoDB was the optimal choice, being free of cost in his limited edition, good start, and with the possibility
to increase resource throwing more money to it.

The Design of Data didn't respect The 3NF, because NoSQL database are doing join poorly, and a level
of redundancy has been introduced, to speed up the response time.

## Data Storage Types
The types of data used in the project are:

* ObjectId
* String
* Integer
* Boolean
* DateTime
* Object

and some of them are collected into Arrays

## Collections Data Structure
the website relies on two database collections:

## Users Collection

| Title | Field Name | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Name | username | text, `maxlength="40"` | string
Email Address | email | email, `maxlength="40"` | string
Password | password | text, `maxlength="15"` | string

#### BoardGame Collection

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Boardgame relation ID | _id | None | ObjectId 
Username | username | text, `maxlength="40"` | string
Title | primary_name | text, `maxlength="50"` | string
BGG id | id | - | integer
Image Thumbnail | thumbnail| - | string
Image | image | - | string
Min Player | minplayers | - | integer
Max Player | maxplayers | - | integer
Playing Time | playingtime | - | integer
Min Playing Time | minplaytime | - | integer
Max Playing Time | maxplaytime | - | integer
Age | age | - | integer
Game Description | description | - | string
Language Dependence | language_dependence | - | string
List of category | boardgamecategory | - | Array(string)
List of mechanics | boardgamemechanic | - | Array(string)
List of family category | boardgamefamily | - | Array(string)
List of Designer| boardgamedesigner | - | Array(string)
List of Artist| boardgameartist | - | Array(string)
List of Publisher| boardgamepublisher | - | Array(string)
Date Bought | dateAdded | timepicker | datetime
Rating| rating | - | integer
User Review| review | `maxlength="200"` | string
 # Technologies Used

# Testing

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 
- How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

## Heroku Deployment

To deploy to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
ROOT_PASSWORD | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

# Contact
To contact me feel free to email

 `pdelbuono  (at)  gmail (dot) com`
 
# Disclaimer

The content of this website is educational purposes only.