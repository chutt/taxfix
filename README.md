# MDM report tool
 
Hi!
 
We have a skeleton for a project we started and would like your help with progressing it.
 
It's a simple tool that imports data and produces some reports,
the data comes from https://jsonplaceholder.typicode.com.
 
So far we imported some users manually into a SQLite database, which you can find in the `migrations` folder.
We would like to import related data to this database from the API, using a script `load_data.py`.
 
Specifically we would like to add `todos` and `albums` from the URL above to this app,
loading data from API only for existing, manually imported users already in there.
 
Once you have the new data loaded, we would like to make a simple report using it:
 
Showing users, with the number of `albums` and unfinished `todos` they have,
please show users with most `albums` and least unfinished `todos` first in the list.
 
And finally it would be good to add testing in the way you see fit.
You will find the existing report in `report.py` and test in the `/tests` folder.
 
 
---
## Setup
 
This skeleton app uses Python3, you can install dependencies by running eg: `pip3 install -r requirements.txt`.
 
Running the migrations: `python3 migrations.py`
 
Loading data from API: `python3 load_data.py`
 
Running report: `python3 report.py`
 
And finally to run tests: `pytest`
 
---
## Sending it back
 
Please either zip up this project and email it, or create a git repository and share it with us.
Thank you!