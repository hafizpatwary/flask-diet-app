# Diet Plan

## Index
[Brief](#brief)
   * [Solution](#solution)

[Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)

[Testing](#testing)


[Deployment](#depl)
   * [Technologies Used](#tech)

[Front End Design](#FE)

[Improvements for the Future](#improve)

[Authors](#auth)

<a name="brief"></a>
## The Brief
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.
<a name="solution"></a>
### Solution
My project focuses around health and lifestyle. The web appliation I created allow the user to vist the website and create a customizable diet that they want to follow.
The diets will consist of meals, that the user can create and add to their diet.

<a name="architecture"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagrams
#### Initial plan

<img src="/Documentation/ERD_Initial_Plan.png" alt="Initial ERD" width="60%" height="60%"/>

The initial plan for the ERD consisted in meeting the requirements set by the project brief,
 the application should have contained at least two tables with a relationship between them.
  As shown above the diet table has a one to many relationship with food table,
  meaning that diets can have multiple foods but not the other way round.


However, it is likely that different meals will be part of many diets. Hence, the delivered solution includes of a secondary table that facilitate a many to many realtionship between food and diet.

#### Delivered solution
![Final ERD](/Documentation/ERD_Final.png)


In the final ERD as well as food and diet tables, a user table was added. After completing the initial ERD tables, it made sense that different food can belong to different diets.
A user table was also added so that a diet plan can only be modified or deleted by the owner of diet only.
The agile methodology enabled the addition of this features, i.e. once the minimum viable product was met, I was able improve the functionalties.


<a name="testing"></a>
## Testing

Testing has been done using pytest. The coverage report for the backend is 54%.
With pytest I was able to test functionality that did not require user login, as most functions in my app
requires user login, the coverage for testing could have been improved by using another tool called Selenium.
However due to the time contraint this was not covered.

[Coverage Image](/Documentation/#)


<a name="depl"></a>
## Deployment

The test and deployment process for the web app was automated using Jenkins, a CI server.
Jenkins run in a GCP instance that automatically deploys the webapp into deployment server, with a webhook to GitHub which is triggered with every push event.

Jenkins justification:
* Open source tool with great community support.
* Contains plugins to facilitate automation
* High customisation


![Deployment Pipeline](/Documentation/CI_pipeline.png)
<a name="tech"></a>
### Technologies Used

* Database: GCP SQL Server
* Programming language: Python
* Framework: Flask
* Deployment: Gunicorn
* CI Server: Jenkins
* Test Reporting: Pytest
* VCS: [Git](https://github.com/devops-cohort/hafiz)
* Project Tracking: [Trello](https://trello.com/qasoloproject)
* Live Environment: GCP

<a name="FE"></a>
## Front End Design

### Initial Front End Sketch



### Final Appearance
#### Diets page

<img src="/Documentation/diet_page.png" alt="Diet Page" width="70%" height="70%"/>

#### Add food to diet

<img src="/Documentation/addfood.png" alt="Add food to Diet" width="70%" height="70%"/>


#### Foods page

<img src="/Documentation/food_page.png" alt="Food Page" width="70%" height="70%"/>


<a name="improve"></a>
## Improvements for the Future

Add author of diet in the homepage
Add total calories in diet card
Add functionality to make diet private or public
Search functionality as the food will increase
Mobile frinedly
<a name="auth"></a>
## Authors

Hafiz Patwary



