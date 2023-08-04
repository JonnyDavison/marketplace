# MarketPlace
<img src="" ><br>
<hr>

## Table of contents
  * [Overview](#overview)
  * [UX](#ux)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Structure](#structure)
    + [Skeleton](#skeleton)
    + [Design ](#design)
      - [Color Scheme](#color-scheme)
      - [Fonts](#fonts)
      - [Other](#other)
  * [Agile](#agile)
  * [Features](#features)
    + [Existing Features](#existing-features)
      - [Menu](#menu)
      - [About](#about)
      - [Accounts](#accounts)
      - [Bookings](#bookings)
      - [Booking Managment](#booking-management)
    + [Future Feature Considerations](#future-feature-considerations)
  * [Responsive Layout and Design](#responsive-layout-and-design)
  * [Tools Used](#tools-used)
    + [Python packages](#python-packages)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Deploy on heroku](#deploy-on-heroku)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Code](#code)
  * [Acknowledgements](#acknowledgements)

## Overview
Developed using Python (Django), HTML, CSS and JavaScript PostgreSQL database.
<br><br>
The deployed project can be accessed at [here]().<br><br>

## UX
<br>

### Strategy 
<hr>

#### User Stories <br>

|                              |#|                                User Story                                                   |
| :--------------:|---|:-------------------------------------------------------------------------------------------: |
| **Iteration-1**                       |  ||
|                                       |#| As a customer, I can navigate and access different ares of the website so that I can easily find and use all the features available |             
|                                       |#| As a user, I can easily find opening times so that I know what times and day the restaurant is open|
|                                       |#| As a Customer, I can create an account so that I don't have to enter all my details each time I book|
|                                       |#| As a customer, I can view my account details so that check they are correct|
|                                       |#| As a customer, I can edit my details so that I can keep them up to date or correct an error|
|                                       |#| As a customer, I can delete my account so that my details are no longer saved|
|                                       |  ||
|                                       |#| As a user, I can use email/username and password to log in so that my account is secure and unique to me|
|                                       |#| As a Customer, I can log out at any point so that I can keep my account secure|
|                                       |  ||
|                                       |#| As a Customer, I can use the website and understand the layout naturally so that I can intuitively browse the content|
|                                       |#| As a Customer, I want to read/view the menu so that I can see my dining options|
|                                       |  ||
|                                       |#| As a Customer, I want to read the menu so that I can see the price point|
|                                       |#| As a customer, I can find contact details easily so that I can communicate with the restaurant|
|                                       |#| As a customer, I can message the restaurant so that ask questions or advice of dietary requirements or special occasions |
|                                       |  ||
|                                       |#|As a Customer, I want to read/view an about page ** so that I can** learn more about the restaurant|
|                                       | |  |
|                                       |#| As a Customer, I want to book a table so that I can make plans and secure a table |
|                                       |#| As a Customer, I want to view my existing bookings so that I can check table times |
|                                       |#| As a Customer, I want to edit my booking so that I can change my time or date for my table |
|                                       |#| As a Customer, I want to delete my booking so that I can cancel my table |
|                                       |#| As a customer, I can select the party size so that I can make reservations for the correct number of guests |
|                                       |#| As a user, I can view multiple bookings I have made so that I know when my booking is and my party size|
|                                       |#| As a Admin/staff member, I can view all upcoming bookings so that I can make appropriate plans for the guests |
|                                       |#| As a Admin/Staff member, I can cancel bookings so that if a booking cancels by email, phone or other the booking can be deleted |
|                                       |#| As a |
|                                       |#| As a |
|                                       | | As a |
|                                       |#|  |
|                                       |#| As a |
|                                       |#| As a |
|                                       |#| As a |
|                                       |#| As a |
|                                       |#| As a |

**Goal:**<br>
Create a website for customers to learn about Pasture, read the menu and book a table. As well as allowing admin to see the bookings to allow planning for guests.

**Objectives:**<br> 
* Create a simple and intuitive User Experience
* Allow bookings to be taken online
* Allow staff to view the bookings
* Share relative information about Pasture
* Good UI/UX on all devices
<br>

### Scope
<hr>

**User Experience**
<br>
* Navigation bar is in the header on all pages
* Pages have suitable function for intended purpose
* Users actions are confrimed to them
* design is clean, clear and easy to follow

**Content**
<br>
* Contact information should be visabel in the footer on relavant pages
* Menus and prices should be displayed clearly on all devices
* Images from the Pasture, should be used across the site to portray the style and atmosphere
* Create a 'message us' section to share feed back with management

**Features**
<br>
* Booking feature available to allow customers to book a table a their prefered time and date
* Profiles for customer to view, edit and delete future bookings
* Booking management page to view, edit and delete bookings

**Account types**
<br>
* Customer accounts allow access to create, view, edit and delete their own bookings only
* Admin or management accounts allow the abilty to view, edit and delete all bookings


**Responsive Design**
<br>
* The design should be responsive on all pages to allow access from the vast majority of screen sizes 
<br><br>

### Structure
<hr>
there is 123 pages with approved access to 123
<br>

-The **Home** page is the 1st page displayed and is availale to all users
<br>

-The **About** page can be navigated to from the navigation bar in the header section of the page. It is availale to all users
<br>

-The **Menu** page can be navigated to from the navigation bar in the header section of the page. It is availale to all users
<br>

-The **Booking** page can be navigated to from the navigation bar in the header section of the page. It is availale only to authenticated/logged in users/admin
<br>

-**Login or Signup** can be navigated to from the navigation bar in the header section of the page. It is availale to customers, in order to create an account
<br>

-**Logout** button is available to all users from the header account section and will log the user out of their profile
<br>

-**Footer** contains relavant information for contact, message and opening times
<br>

-**Profile** page is available to logged in cutomers to show their information and future bookings;
<br>

-**Booking Management** page is availabel to Admin/Staff that are authenicated and logged in
<br>


#### FLOWCHART
The Flowchart for my program was created using XYZ
<br>
<img>
<br><br>


### Skeleton
<hr>

**Wireframes**
<br>
Wire frames where hand drawn as the developer enjoys hand drawing/design work
<br>

**Database**
<br>
Initial Schema
<img> make drop down

<br>

Final Schema
<img> make drop down
<br>


## Design 


#### Color Scheme


#### Fonts


#### Other

<hr>

## Agile
This project was developed using the Agile methodology.
<br>
User stories where created in GitHub issues, labeled and added to milestones as iterations. Each iteration contained a Kanban board which contained **To Do**, **In-Progress**, **Testing** and **Done**. It is worth noteing that the iteration/sprint times where kept at 1 week to allow better time management and prioritisation with the alloted time.


### Sprint Details

* **Sprint 1**
    - Set up Django
    - Create inital apps
    - Static pages
    - Templates
    - Navigation
    - Accounts 
    - CRUD functionality
    - Menu pages

    <br>

* **Sprint 2**
    - Bookings app
    - CRUD functionality
    - Innate design

 <br>

* **Sprint 3**
    - Testing
    - Docs
    - 
* **Sprint 4** <br>
    - S
    - 
    - 


## Features
### Existing Features
#### Menus
#### About
#### Accounts
#### Bookings
#### Booking management

<hr>


### Future Feature Considerations

#### Preorder

<hr>


## Responsive Layout and Design
Bootsrtap

**Tested devices:**
 - Iphone etc etc

## Tools Used

[GitHub](https://github.com/) - Hosting code
<br>

[Git](https://git-scm.com/) - Version control
<br>

[GitPod](https://www.gitpod.io/) - Code editor
<br>

[Heroku](https://dashboard.heroku.com/) - Project deployment
<br>

[Favicon.io](https://favicon.io/) - Website favicon
<br>

[Grammarly](https://app.grammarly.com/) - Spelling/Grammer checks
<br>

[Font Awesome](https://fontawesome.com/) - Icons/Buttons
<br>

[Bootstrap](https://getbootstrap.com/) - Front-end toolkit
<br>

[Google Fonts](https://fonts.google.com/) - Fonts
<br>

[PEP8 Validator](http://pep8online.com/) - Validating Python
<br>

[JsHint](https://jshint.com/) - Validating JavaScript
<br>

[HTML W3C Validator](https://validator.w3.org/) - used for validating the HTML
<br>

[CSS W3C Validator](https://jigsaw.w3.org/css-validator/) - used for validating the CSS
<br>

[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project
<br>

LightHouse - Proformance testing
<br>

### Python packages

* django 
* gunicorn 
* dj-database-url
* psycopg2
* django-allauth
* django-crispy-forms

## Testing
The testing documentation can be found at [TESTING.md](TESTING.md)

## Deployment

### Deploy on Heroku


## Credits
### Content

### Media
Stock images where downloaded from [Pexels](https://www.pexels.com/).
<br>
The home page background image was downlaoded from Pexels, and attributed to Rachel Claire
The menu page background image was downlaoded from Pexels, and attributed to Elevate

Licencing for using Pexel images can be found [here](https://www.pexels.com/license/) and has been adhered to across the site

### Code

## Acknowledgements
