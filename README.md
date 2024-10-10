# WINERY [(*Live site*)]()


## Introduction 

. 

![start screen responsive](./README-images/)


## Table of contents

- [Live site](#winery)
  - [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [Project Rationale](#project-rationale)
    - [Website Goals and Objectives](#website-goals-and-objectives)
    - [Target Audience](#target-audience)
  - [E-Commerce Business Model](#e-commerce-business-model)
  - [Marketing Strategies](#marketing-strategies)
    - [Search Engine Optimisation](#search-engine-optimisation)
    - [SEO Strategies Implemented](#seo-strategies-implemented)
    - [Social Media](#social-media)
    - [Newsletter Marketing](#newsletter-marketing)
  - [Agile methodology](#agile-methodology)
    - [Overview](#overview)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [GitHub Projects](#github-projects)
    - [EPICs](#epics)
    - [User Stories](#user-stories)
  - [UX/UI design](#uxui-design)
    - [Wireframe](#wireframe)
    - [Structure \& Logical Flow (database design)](#structure--logical-flow-database-design)
    - [Colour Scheme](#colour-scheme)
    - [Fonts](#fonts)
    - [Responsiveness (media queries)](#responsiveness)
  - [Security Measures and Protective Design](#security-measures-and-protective-design)
    - [User Authentication](#user-authentication)
    - [Password Management](#password-management)
    - [Form Validation](#form-validation)
    - [Database Security](#database-security)
  - [Features](#features)
    - [Header](#header)
    - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Coding languages used](#coding-languages-used)
    - [Frameworks and Libraries used](#frameworks-and-libraries-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [To deploy the project to Heroku](#to-deploy-the-project-to-heroku)
    - [To fork the project](#to-fork-the-project)
    - [To clone the project](#to-clone-the-project)
  - [Credits](#credits)
    - [Project Inspiration](#project-inspiration)
    - [Content](#content)
    - [Colour Theme](#colour-theme)
    - [Media](#media)
    - [Tools](#tools)
  - [Acknowledgements](#acknowledgements)


## Project Rationale

### Website Goals and Objectives

### Target Audience


## E-Commerce Business Model


## Marketing Strategies

### Search Engine Optimisation

### SEO Strategies Implemented

### Social Media

### Newsletter Marketing


## Agile Methodology

### Overview

Agile methodology is a project management approach that emphasizes flexibility, collaboration, and iterative progress towards a well-defined goal. It is particularly effective in software development where requirements and solutions evolve through the collaborative effort of self-organizing cross-functional teams. Agile methodologies aim to deliver small, incremental changes in a product to improve quality and adaptability to changing needs.

### MoSCoW Prioritization

The MoSCoW prioritization technique is used to determine the importance of various features and tasks in a project. This method categorizes features into four groups: Must Have, Should Have, Could Have, and Won't Have. This helps in effective time management and ensures that the most critical functionalities are delivered first.

### GitHub Projects

Using GitHub Projects, tasks are managed and progress tracked through project boards. Each board represents status of the User Story (Epic, To Do, In Progress, Done, Future features). Issue labels include the user story persona, prioritization and iterations (milestones).

[Link to the project board](https://github.com/users/VL-ocean/projects/4/views/1) & [Link to the project table](https://github.com/users/VL-ocean/projects/4/views/2)

<details>
<summary>Iteration 1</summary>
<hr>
<b>Board</b>
<img src="./README-images/iteration-1-board.png">
<hr>
<b>Table</b>
<img src="./README-images/iteration-1-table.png">
</details>

<details>
<summary>Milestones Progress</summary>
<hr>
<b>Overall view</b>
<img src="./README-images/milestone-progress.png">
<hr>
<b>The completed milestones are closed</b>
<img src="./README-images/1-2-milestones-closed.png">
<hr>
<b>The milestones to complete are in open status</b>
<img src="./README-images/3-4-milestones-in-progress.png">
</details>

<details>
<summary>Issue sample (iteration 2)</summary>
<hr>
<b>Issue Sample</b>
<img src="./README-images/issue-sample-iter-2.png">
</details>

### EPICs

Epic is a large body of work that is broken down into user stories. Each Epic in this project represents a key aspect of the platform's development and ensures comprehensive coverage of the required functionalities.

- [**EPIC 1: Project Planning**](https://github.com/VL-ocean/winery/issues/6)
    - [USER STORY: Agile Methodology](https://github.com/VL-ocean/winery/issues/1)
    - [USER STORY: Design Database Schema](https://github.com/VL-ocean/winery/issues/2)
    - [USER STORY: Design Website Visuals](https://github.com/VL-ocean/winery/issues/3)
    - [USER STORY: Create Wireframes](https://github.com/VL-ocean/winery/issues/4)
    - [USER STORY: Create Django Project](https://github.com/VL-ocean/winery/issues/5)

Summary: Covers the user experience design process and development environment setup

- [**EPIC 2: Registration and User Account Management**](https://github.com/VL-ocean/winery/issues/11)
    - [USER STORY: User Registration](https://github.com/VL-ocean/winery/issues/7)
    - [USER STORY: User Login and Logout Features](https://github.com/VL-ocean/winery/issues/8)
    - [USER STORY: Password Reset](https://github.com/VL-ocean/winery/issues/9)
    - [USER STORY: Profile Management](https://github.com/VL-ocean/winery/issues/10)

Summary: It encompasses user-related functionalities focusing on managing user accounts effectively within the system.


### User Stories

With an emphasis on delivering a seamless user experience, the goal of this project is to provide a comprehensive platform that serves both visitors and registered users. The platform will allow for the development and maintenance of content, present developer profiles, and provide opportunities for interaction. The following user stories outline the essential functionalities and the rationale behind them.

#### Developer

- 

#### Site Visitor

- 

#### Registered User

- 

#### Site Admin

- 


## UX/UI design

### Wireframe

The original layouts look different from the finished blog as some changes were made during the development process.

<details>
<summary>Home</summary>
<img src="./README-images/">
</details>



### Structure & Logical Flow (database design)

The database schema outlines the structure and relationships between key tables for the platform. The User table stores basic user information and authentication details. The Profile table 

The database model diagram was designed using Lucidchart:

![Screenshot of flowchart](./README-images/)

### Colour Scheme

The colours were mostly taken from bootstrap colour palette. They are:
- `#212529` - text colour 

Custom colours:
- `#e99767` - border accent colour 

![Custom colour palette](./README-images/)

### Fonts

- 

![Fonts](./README-images/)


### Responsiveness

The website is responsive to different layouts depending on the size of the viewport based on the Bootstrap media queries.

![media queries](./README-images/)


## Security Measures and Protective Design

### User Authentication

- Django's LoginRequiredMixin is used to ensure that any requests to access secure pages by non-authenticated users are redirected to the login page.
- Django's UserPassesTestMixin is used to limit access based on certain permissions, ensuring users can only edit/delete content they authored. If the user doesn't pass the test, they are shown an HTTP 403 Forbidden error.

### Password Management

- Use Django's built-in password management tools to ensure passwords are hashed and stored securely.
- Enforce strong password policies to enhance user account security.

### Form Validation

- If incorrect or empty data is added to a form, the form won't submit, and a warning will appear to the user informing them which field raised the error.

### Database Security

- The database URL and secret key are stored in the env.py file to prevent unwanted connections to the database. This setup was implemented before the first push to GitHub.
- Cross-Site Request Forgery (CSRF) tokens are used on all forms throughout the site to enhance security.


## Features

### Header

*Visitor view*

![Visitor view](./README-images/)

*User View*

![User view](./README-images/)

The header 



### Future Features

- 


## Technologies Used

### Coding languages used

* HTML
* CSS
* Python
* JavaScript

### Frameworks and Libraries used

**Django**
* Framework used to build this project. Provides a built in admin panel and includes many helper template tags that make writing code quick and efficient.

**Django-Allauth**
* Used for User authenticaion (register, login and logout).

**Django Crispy Forms**
* Used to control rendering of Django forms.

**PostgreSQL**
* The database used by the deployed project on Heroku.
  
**psycopg2**
* PostgreSQL database adapter for the Python programming language.

**Gunicorn**
* Python HTTP server for WSGI applications.

**WhiteNoise**
* Designed to serve static files for Django applications.

**Django RichTextField**
* A Django model field and widget that renders a customizable rich text/WYSIWYG widget.

**Django Resized**
* Resizes image origin to specified size.

**Cloudinary**
* The cloud platform used to store static media files.

**Balsamic**
* Used for the wireframes

**Git**
* Used for version control.

**GitHub**
* Used to store the project's code after being pushed from Git.

**GitPod**
* Used as a platform to develop code in a ready-to-code developer environment.

**Heroku**
* The cloud platform used to deploy the project in the live environment.

**Bootstrap**
* The front end development framework used for styling along with custom CSS.
  
**Lucidchart**
* Used for the entity relationship diagram


## Testing

The website underwent an extensive testing process to ensure its functionality, accessibility, and performance. This involved validating the code, assessing accessibility, conducting performance tests, performing cross-device testing, verifying browser compatibility, evaluating user stories, and incorporating user feedback to improve the overall user experience. 

Testing summary and results can be found in [TESTING.md](TESTING.md) file.


## Deployment

### To deploy the project to Heroku

Follow these steps to deploy your Django project to Heroku from VS Code:
| |
| --- |
| **Step 1** Create a New Heroku App |
| - Access the Heroku Dashboard: Log in to your Heroku account and access the dashboard. |
| - Create a New App: Click on the New button in the top-right corner of the dashboard and select Create new app from the dropdown menu. |
| - App Name and Region: Enter a unique name for your app and choose a region closest to you (EU or USA). Click Create App to create the app. |
| **Step 2** Configure Environment Variables |
| - Reveal Config Vars: From the new app Settings, click Reveal Config Vars. |
| - Set Environment Variables: Set your environment variables as follows: |
|   - `CLOUDINARY_URL`: Insert your own Cloudinary API key here. |
|   - `DATABASE_URL`: Insert your own ElephantSQL database URL here. |
|   - `DISABLE_COLLECTSTATIC`: Set to 1 for temporary purposes, and remove it for the final deployment. |
|   - `SECRET_KEY`: This can be any random secret key. |
| **Step 3** Prepare the Project for Deployment |
| - Create a `requirements.txt` File: This file lists all the dependencies required by your project. You can install the project's requirements using `pip3 install -r requirements.txt`. If you have your own packages installed, update the `requirements.txt` file using `pip3 freeze --local > requirements.txt`. |
| - Create a `Procfile`: This file specifies the commands Heroku should run to start your app. Create the Procfile using `echo web: gunicorn app_name.wsgi > Procfile`. Replace `app_name` with the name of your primary Django app, which is the folder where `settings.py` is located. |
| **Step 4** Connect Your GitHub Repository to Heroku |
| - Automatic Deployment: Select Automatic Deployment from the Heroku app settings to automatically deploy your app whenever you push changes to your GitHub repository. |
| - Manual Deployment: Alternatively, you can connect your GitHub repository to Heroku manually using the Terminal/CLI: |
|   - Login to Heroku: Run `heroku login -i` to log in to your Heroku account. |
|   - Set the Remote for Heroku: Run `heroku git:remote -a app_name` to set the remote for Heroku. Replace `app_name` with your app name. |
|   - Push to Heroku: After performing the standard Git add, commit, and push to GitHub, you can now type `git push heroku main` to deploy your app. |
| **Step 5**  Verify Your Deployment |
| - Open App: Once your app is deployed, you can open it by clicking on the Open App button in the Heroku dashboard. This will open your app in a web browser. |
| - Verify App: Verify that your app is running correctly by checking for any errors or issues. |

### To fork the project

Forking the **GitHub** repository allows you to create a duplicate of a local repository. This is done so that modifications to the copy can be performed without compromising the original repository.

- Log in to **GitHub**.
- Locate the repository.
- Click to open it.
- The fork button is located on the right side of the repository menu.
- To copy the repository to your **GitHub** account, click the button.

### To clone the project

- Log in to **GitHub**.
- Navigate to the main page of the repository and click **Code**.
- Copy the **URL** for the repository.
- Open your local **IDE**.
- Change the current working directory to the location where you want the cloned directory.
- Type git clone, and then paste the **URL** you copied earlier.
- Press **Enter** to create your local clone.


## Credits

### Project Inspiration

- 

### Content

- 

### Colour Theme

- 

### Media

- [Coffee and Chocolate photo](https://www.pexels.com/)

### Tools

- [Abobe Colour](https://color.adobe.com/create/color-wheel)
- [FontJoy](https://fontjoy.com/)


## Acknowledgements

  - [Cohort Facilitator - Marko Tot](https://github.com/tmarkec) for support in the classroom and guidance through the course.
  - [Mentor - Dick Vlaanderen](https://github.com/dickvla) for support throughout the project, ideas and advice.