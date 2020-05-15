# stylometric-search-engine-project


Authorship attribution via POS tagging. Utilizes an simple inverted index for quick lookups. The goal of the project being a moderation management tool for forum sites + social media applications.

## Setup 

* Run ```pipenv install -r requirements.txt```
* Additionally the **Code** directory in the root of the project requires a data directory. The data directory should contain a proper JSON from [here](https://files.pushshift.io/reddit/comments/). I didn't include it in the repository due to the large size
* Code/main.py should specify the JSON you want to use for the execution of the program
* Run python3 Code/main.py to run project.
