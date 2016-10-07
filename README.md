# proj2-flask
A starter project for using the Flask framework, I worked on this 
for a class.

## Author: Jared Paeschke, paeschke@cs.uoregon.edu

## Application
This project uses Flask, Jinja2, Arrow, and CSS style sheets to 
serve webpages. Using a data file and a Jinja template html web 
pages are created and served. Users should be able to follow 
the format of the data file located in ./data/schedule.txt to 
make other schedules.

## Instruction for running
From your preferred command line do the following:
* git clone http://github.com/mahananaka/proj2-flask.git
* cd proj2-flask
* bash ./configure (this might take a minute to run)
* make service

At this point you should be able to open webpages on port 8000.
If your on the machine you installed it to, you may do this 
by going to http://127.0.0.1:8000/. If you installed it to a
different machine you will need to get the ip address for it.

Out of the box, the only pages are a 404 not found page and the 
schedule page, which the root domain will route you to. This 
schedule page is for the 10 week CIS 322 class held in the 
Fall 2016 term at UO. The current week is also highlighted so
that it stands out.

##Troubleshooting info
I built this projected and tested it on a Raspberry Pi 3 running Rasbian 
Jessie. I cannot guarantee the success you will have on other systems. 
More steps may be required to install on other hardware.

###### Python Virtual Environment not installed
One issue I ran into was pyvenv was not installed by default on my Pi 3.
To install this you can use the following.

`sudo apt-get install python3-venv`
