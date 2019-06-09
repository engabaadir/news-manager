# News Manager Project
This is a project for Udacity's 
[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Why this Project?
1. To enhance student's SQL database skills. 
1. To get practice interacting with a live database both from the command line and from your code. 
1. To explore a large database with over a million rows. 
1. To build and refine complex queries and use them to draw business conclusions from data.

## Questions to Answer:
1. **What are the most popular three articles of all time?** 
    Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
2. **Who are the most popular article authors of all time?** 
	That is, when you sum up all of the articles each author has written, which authors get the most page views? 
	Present this as a sorted list with the most popular author at the top.
3. **On which days did more than 1% of requests lead to errors?**  
	The log table includes a column status that indicates the HTTP status code that the news site sent 
	to the user's browser. 

## Core Tools Used for this Project
1. PostgreSQL database
2. Python 3.7.3
## Project Requirements:
This project runs in a virutal machine using Vagrant so to get things done, follow the below steps.
#### Installing the Prerequisites:
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
These files will configure the virtual machine and install all the tools needed to run this program.
1. Download the database file: [sql data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Unzip the data folder to get the newsdata.sql file.
1. Move the newsdata.sql file into the vagrant directory
1. Download the project: [News Manager](https://github.com/engabaadir/news-manager.git)
1. Upzip it and copy all the files into the vagrant directory into a folder named *news_manager_project*
#### Starting the Virtual Machine:
1. Open Terminal and navigate to the project folders we setup above.
1. cd into the vagrant directory
1. Run ``` vagrant up ``` to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant/news_manager_project ```
#### Importing the data into the database:
1. Import the data using the following command: ``` psql -d news -f newsdata.sql ```
1. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
## Run the project!
1. If you aren't in *news_manager_project* directory, cd into the correct project directory: ``` cd /vagrant/news_manager_project ```
1. Run ``` python news_manager.py ```

## Expected Output: 

[=========PROCESSING OUTPUT===========]

MOST POPULAR THREE ARTICLES OF ALL TIME:
[1] "Candidate is jerk, alleges rival" — 338647 views
[2] "Bears love berries, alleges bear" — 253801 views
[3] "Bad things gone, say good people" — 170098 views

MOST POPULAR ARTICLE AUTHORS OF ALL TIME:
[1] Ursula La Multa — 507594 views
[2] Rudolf von Treppenwitz — 423457 views
[3] Anonymous Contributor — 170098 views
[4] Markoff Chaney — 84557 views

DAYS WITH MORE THAN 1% OF ERRORS:
July 17, 2016 — 2.2% errors
