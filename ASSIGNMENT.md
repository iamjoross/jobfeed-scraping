# Programming assignment – Jobfeed Python developer

Your task is to write an application (in Python) that runs daily and synchronizes data between two external systems: an AWS S3 bucket and a  RESTful API. You do not need to implement the REST API.

XML files with all active job advertisements from theguardian.com website are delivered every day to S3 bucket. Daily file is accessible via URL in this format: https://jobfeed-assignment-data.s3.eu-west-1.amazonaws.com/Jobs.%Y-%m-%d.0.xml (e.g. https://jobfeed-assignment-data.s3.eu-west-1.amazonaws.com/Jobs.2022-07-07.0.xml for July 7 2022).

Your solution should download this data daily and ensure it is synchronized with an external API.

## Requirements

* Newly added jobs are uploaded via API (HTTP POST)
* Disappeared(expired) jobs are removed via API (HTTP DELETE)
* Assume yesterday as day of initial delivery (all jobs will be posted to API)
* Feel free to assume external API routes and JSON input. (e.g., use httpbin.org)
* You can use any intermediary storage (should your solution require one)

**NB**: Job URLs are unique.

It should take you ±4 hours to complete the assignment, but you can take as much time as you need. We do not expect production-ready code, but it should be a good working prototype that showcases your skills.

## Result of the assignment

Your submission should contain the following:

* Source code of your application
* Short description of the approach and limitations of the implementation
* Instructions on how to run your application on our side
* What was your thought process when implementing it (design)

## Points of attention:

* Use of modern Python features
* Code quality, testing, etc
* System design

**Good luck!**

_This assignment is copyright of Textkernel. Do not share this assignment or your solution on public websites (e.g. GitHub, coding competitions, etc)._


