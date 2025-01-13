# Marine Hub: Most Wanted Pirates

A web application inspired by One Piece, designed for the Marines to efficiently log, view, edit, and delete the most wanted pirates lists. The hub allows Marine officers to manage and maintain a real-time database of bounties, track wanted pirates, and update their status with ease, ensuring that the latest criminal activity is always up to date.

![Site Preview](static/images/sitepreview.gif)

[Link to site](https://marine-hub-c8dbfbfaea4e.herokuapp.com/)<br>
[Link to repository](https://github.com/MCamish29/op_marine_hub.git)<br><br>
_To open links in a new tab, hold CTRL + Click_

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Database](#database)
- [Testing](#testing)
- [Validation](#validation)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Acknowledgments](#acknowledgments)

## Features
The web app allows Marine officers to perform the following actions to manage the most wanted pirate lists:
- Add new pirate records.
![Add](static/images/newlisting.webp)
- Edit existing pirate records.
![Edit](static/images/editlisting.webp)
- Delete existing pirate records.
![Delete](static/images/deletelisting.webp)
- View most wanted pirates with bounty details.
![Home](static/images/index.webp)
- User authentication to edit the site.
- Responsive design for easy use on desktop and mobile devices<br>
<img src="static/images/pixel7view.webp" alt="Mobile" width="200" height="auto">
<img src="static/images/tabletview.webp" alt="Tablet" width="309" height="auto">

## Future enhancements
* Adding a commenting system for users to engage with pirate listings.
* Search functionality will allow users to efficiently find pirates by name, bounty, or other details.

<br>

# Installation

### 1. Clone the repository
Clone the GitHub repository to your local machine : [Link to repository](https://github.com/MCamish29/op_marine_hub.git)

### 2. Install dependencies
pip install -r requirements.txt

### 3. Apply migrations
python manage.py migrate

### 4. Run server
python manage.py runserver

### Prerequisites

Make sure you have the following installed:

- Django (Django~=4.2.1)
- Any other dependencies (e.g., PostgreSQL, Redis, etc.)
- gunicorn (gunicorn~=20.1)
- PostgreSQL (dj-database-url~=0.5 psycopg2~=2.9)
- Cloudinary (cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15)
- Summernote (django-summernote~=0.8.20.0)
- whitenoise (whitenoise~=5.3.0)


You can install them via `pip3`<br>
Packages must be added to requirements.txt `pip3 freeze --local > requirements.txt`

# Database

## Entity-Relationship Diagram (ERD)

### User Table
| **Key**          | **Name**        | **Type**           |
|-------------------|-----------------|--------------------|
| Primary Key       | `id`            | Integer            |
| Attribute         | `username`      | String             |
| Attribute         | `email`         | String             |
| Attribute         | `password`      | String             |
| Attribute         | (other default fields) | Various   |

### Wanted Table
| **Key**          | **Name**        | **Type**           |
|-------------------|-----------------|--------------------|
| Primary Key       | `id`            | Integer            |
| Attribute         | `pirate_name`   | String             |
| Attribute         | `slug`          | String             |
| Attribute         | `bounty`        | Big Integer        |
| Attribute         | `pirate_image`  | String (Cloudinary)| 
| Attribute         | `description`   | Text               |
| Attribute         | `created_on`    | Date               |
| Attribute         | `updated_on`    | Date               |
| Attribute         | `status`        | Integer (Choices)  |
| Foreign Key       | `author_id`     | Integer (References `User.id`) |

## Relationships
- **User → Wanted**: One-to-Many relationship
  - A single `User` can create multiple `Wanted` records.
  - `author_id` in the `Wanted` table is a foreign key referencing `User.id`.

<br>

# Testing 

| **Test** | **Steps** | **Expected Result** | **Result** |
| --- | --- | --- | --- |
| **Home page displays from URL** | 1. Open the browser. <br> 2. Type the URL into the address bar: [https://marine-hub-c8dbfbfaea4e.herokuapp.com/](https://marine-hub-c8dbfbfaea4e.herokuapp.com/) <br> 3. Press **Enter**. | The home page loads with its contents, including the navigation bar and footer. | Pass |
| **Additional listings displayed** | 1. Navigate to the home page if not already there. <br> 2. Scroll down to the bottom of the page. <br> 3. Click on the "Next" button to view more listings. | Additional pirate listings are displayed in the same format as the current page. | Pass |
| **Login to existing account** | 1. Navigate to the top right corner of the homepage. <br> 2. Click the **Login** button in the navbar. <br> 3. Enter the username in the "Username" field. <br> 4. Enter the password in the "Password" field. <br> 5. Click the **Sign In** button. | After signing in, the user is redirected to the home page, with a confirmation message appearing at the top-right corner. The navbar should now display the **Logout** button. | Pass |
| **Login to existing account - incorrect password/username** | 1. Navigate to the top right corner of the homepage. <br> 2. Click the **Login** button in the navbar. <br> 3. Enter an incorrect username or password in the fields. <br> 4. Click the **Sign In** button. | The user remains on the login page and sees an error message indicating that the login credentials are incorrect. | Pass |
| **Logging out of account** | 1. Navigate to the top-right corner of the homepage. <br> 2. Click the **Logout** button in the navbar. <br> 3. Confirm that you want to log out by clicking the **Sign Out** option in the prompt. | After signing out, the user is redirected to the home page. A confirmation message appears, and the navbar now displays the **Login** and **Register** options instead of **Logout**. | Pass |
| **Registering a new account** | 1. Navigate to the top-right corner of the homepage. <br> 2. Click the **Register** button in the navbar. <br> 3. Enter the **username** in the required field. <br> 4. Enter the **email** in the required field. <br> 5. Enter a **password** that meets the required criteria. <br> 6. Click the **Sign Up** button. | After completing the registration, the user account is created successfully, and a confirmation message appears at the top-right corner. The navbar will now display the **Logout** option. | Pass |
| **Registering a new account - without entering username** | 1. Navigate to the **Register** page. <br> 2. Leave the **username** field blank. <br> 3. Enter the other required fields: **email** and **password**. <br> 4. Click the **Sign Up** button. | The system will display an error message indicating that the username field is required and will prevent the form from being submitted. | Pass |
| **Registering a new account - with incorrect password requirements** | 1. Navigate to the **Register** page. <br> 2. Enter the **username** and **email**. <br> 3. Enter a password that does not meet the required criteria (e.g., too short or lacks special characters). <br> 4. Click the **Sign Up** button. | The system will display an error message indicating that the password does not meet the required criteria, and the form will not submit. | Pass |
| **Viewing pirate details as a visitor** | 1. On the homepage, browse the list of pirates. <br> 2. Click on the name of any pirate. | The user is redirected to the pirate details page, where they can view all information about the pirate, including their bounty, description, and image. No edit/delete buttons should be visible to visitors. | Pass |
| **Viewing pirate details as creator of listing** | 1. Log in as the creator of a pirate listing. <br> 2. On the homepage, click on the name of the pirate listing they created. | The user is redirected to the pirate details page, where they can see all the pirate's information, including a button to **Edit** or **Delete** the listing. | Pass |
| **Returning to home page** | 1. Navigate to any page other than the home page (e.g., a pirate's details page). <br> 2. Click the **Home** button in the navbar. | The user is redirected back to the home page, regardless of their current page. | Pass |
| **Edit current listing as creator of listing** | 1. On the pirate details page, click the **Edit** button. <br> 2. Make changes to the pirate's information (e.g., bounty, description). <br> 3. Click **Save Changes**. | The changes are saved, and the user is redirected back to the pirate details page. The updated information should be visible. | Pass |
| **Cancel edit of current listing as creator of listing** | 1. On the pirate details page, click the **Edit** button. <br> 2. Modify the fields, but then click the **Cancel** button. | The user is redirected back to the pirate details page without saving any changes, and the original information is displayed. | Pass |
| **Delete listing as creator of listing** | 1. On the pirate details page, click the **Delete** button. <br> 2. Confirm the deletion by clicking **Delete** in the confirmation prompt. | The pirate listing is deleted, and the user is redirected to the homepage where the deleted listing no longer appears. A success message will be shown. | Pass |
| **Create a new listing** | 1. On the navbar, click the **New Listing** button. <br> 2. Fill in all required fields (pirate name, bounty, description, image). <br> 3. Click **Create Listing**. | After submitting the form, the user is redirected to the homepage, where the newly created pirate listing is displayed. | Pass |
| **Create a new listing - missing required fields** | 1. Click the **New Listing** button on the navbar. <br> 2. Leave some required fields blank (e.g., pirate name). <br> 3. Click **Create Listing**. | The form will display an error message indicating which required fields are missing and will not allow submission until all fields are completed. | Pass |


# Validation

### W3C

All HTML pages were passed through [W3C HTML Validator](https://validator.w3.org/) to ensure it met required standards. The HTML pages were all successful when passing the code through from page source.

All CSS pages were passed through [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) successfully.

### PEP8

All Python files were passed through [Code Institute PEP8 Linter](https://pep8ci.herokuapp.com/#) to ensure it met required standards. The only warnings given related to the settings.py file this was due to 4 lines in AUTH_PASSWORD_VALIDATORS being greater than the desired amount of characters, this code was installed by Django on setup.

### JSHint

The Javascript file was passed [JSHint](https://jshint.com/) successfully.

## Bugs

Bugs were found during development of the site and resolved which can be seen on the [Kanban workflow](https://github.com/users/MCamish29/projects/2/views/1).


# Deployment


1. Log in to Heroku or create account
2. Click the **new** button on the top right to display drop down
3. Select **create new app**
4. Enter app name - *this must be a unique name*
5. Choose relevant region
6. Click **create app**
7. On the application dashboard select **settings**
8. Scroll down to *Config Vars*
9. Click on **Reveal_Config vars**
10. Enter **DATABASE_URL**
11. Click add
12. Enter **Cloudinary API**
13. Click add
14. Enter **Secret Key**
15. Click add
16. Select **deploy** at the top of the application dashboard
17. Select **GitHub** as deployment method
18. Search for repository name and click **connect**
19. Scroll down and select either **Enable Automatic Deploys** or **Deploy Branch** for manual deployment.
20. This will then run the process to deploy the application
21. Click on **View** once successfully deployed

# Technologies Used

* **VSCode** was the code editor used for the project
* **Django** was the framework used through out the project
* **Python, HTML, CSS, Javascript** was the language used through out the project
* **Heroku** was used to deploy the application
* **Git** was used to commit code
* **GitHub** was used to store the repo
* **Code Institute Python Linter** was used for python validation
* **W3C** was used for HTML and CSS validation
* **JSHint** was used for Javascript validation
* **Cloudinary** was used to store images
* **Google Fonts** was used for styling


# Acknowledgments

* Thank you to Code Institute for there comprehensive guides and support.
* A big thank you to my Code Institute mentor Graeme Taylor for all his guidance, support and endless counts of knowledge.
* All pirate information and images was provided by [One Piece Fandom](https://onepiece.fandom.com/wiki/Bounties/List)

