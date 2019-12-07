# Diet Plan

## Index
[Brief](#brief)
   * [Solution](#solution)

[Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)

[Testing](#testing)
   * [Report](#report)


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
![Initial ERD](/Documentation/ERD_Initial_Plan.png {:height="50%" width="50%"})

The initial plan for the ERD consisted in meeting the requirements set by the project brief,
 the application should have contained at least two tables with a relationship between them.
  As shown above the diet table has a one to many relationship with food table,
  meaning that diets can have multiple foods but not the other way round.


However, it is likely that different meals will be part of many diets. Hence, the delivered solution includes of a secondary table that facilitate a many to many realtionship between food and diet.

#### Delivered solution
![Final ERD](/Documentation/ERD_Final.png)


As shown in the final ERD as well as food and diet tables, a user table was added. After completing the initial ERD tables, it made sense that different food can belong to different diets.
A user table was also added so that a diet plan can only be modified or deleted by the owner of diet only.
The agile methodology enabled the addition of this features, i.e. once the minimum viable product was met, I was able improve the functionalties.


<a name="testing"></a>
## Testing

JUnit, Mockito and Selenium tests have been used for automated testing, and SonarLint/SonarQube for static reporting and refactoring.

<a name="report"></a>
### Report

[Link to Final Surefire Report](/Documentation/Surefire_Report.pdf)

Test coverage for the backend is at 84%, there are as of yet no working Selenium tests but hope to get these running soon.
The SonarQube static report shows 9 code smells remaining, 0 bugs, 0 duplications and 0 vulnerabilities.

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
### Wireframes
Diets
![Diet Page](/Documentation/diet.png)
Foods
![Food Page](/Documentation/food.png)
### Final Appearance

<a name="improve"></a>
## Improvements for the Future

<a name="auth"></a>
## Authors

Hafiz Patwary



