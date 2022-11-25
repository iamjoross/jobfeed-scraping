# Job Board Scraper
## Jobfeed Python Assignment

### Description
Job Board Scraper is an xml scraper pipeline scheduled to run everyday at 6am. It is a simple pipeline that scrapes on job board sources, parses them and persist(mocked) data scraped.

### Instructions
1. Install Docker(https://docs.docker.com/get-docker/)
2. In the root directory, build docker image by running `docker image build -t job_scraper:v1` in the terminal.
3. Run the docker image build by running `docker run -it -p 5000:5000 job_scraper:v1` in the terminal.