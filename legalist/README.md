# LegaList

This project contains all the assignment task for legalist

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements 
if running locally

```bash
pip install -r requirements.txt
```

## Usage

```python
import scrapy

scrapy crawl quotes_default
```

# Assignment Details:

As you know time was short for the assignment.
I tried to complete maximum within the time capacity.

### 1: We basically use most of the time virtual environment.

Here I have used Docker to setup the entire project.


### 2: Having a running scrapy spiders.

Wrote 7 spiders entirely and majority of the time was spent there.
Plus this is my main area of expertise


### 3: Postgres as a datastore for the items scraped

Setup the entire database locally and ran few tests.
Due to the shortage of time I just made one table
But you can see the file pipeline to check my schema idea
for the project.
It can be completed on demand if further time is provided


### 4: Json exports for the items scraped

I ran the spiders and stored the data in json file
I want to give a heads up I have not QA the data due
to shortage of time


### 5: At least one medium and one hard spiders from the below list

All spiders and done except one.
Majority of the time was spent here


### 6: Proper docker deployments

Docker deployment files are attached


### 7: Reuse code as much as possible (DRY principle)

I have made the spider code minimum and tried to reuse and
inherit the code as much as i could


### 8: Have a separate spider for each type

Done


### 9: Export the data to json files and to postgres

I have attached the exported files for json data
For postgres I have written a pipeline to export all 
the data to postgres while the spider is running
and yielding data


### 10: Make sure we don’t hit the website too hard. (implement/configure rate limiting)

For this I have added a download delay of 1 for the site
Working fine on my side. We can increase its value for further safety 


### 11: Run spiders as cron job daily at 11am and 11pm

0 11,23 * * * scrapy crawl quotes_default

Please have a look at the crawler-cron file
it is scheduling the spiders on the time mentioned above


### 12: Implement decent logging mechanism to be able to easily debug

I tried to write the code in a way that is self explanatory
Also added some comments to further explain the code 
we can easily attach loggers as well
import logging
logger = logging.getLogger(__name__)


### 13: Implement proxying(optional see below)

Didn't have time to work on this


### 14: We want to be able to pause/resume the scraping job from where we left in case
of failure

 I have added a spider named quotes_default_redis
 Please have a look to check its functionality

 