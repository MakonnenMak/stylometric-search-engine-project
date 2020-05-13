# stylometric-search-engine-project

*Still working on it*

Authorship attribution via POS tagging and semantic tree analysis. Utilizes an simple inverted index for quick lookups. The goal of the project being a moderation management tool for forum sites + social media applications.

## Setup 

* Run ```pipenv install -r requirements.txt```
* Additionally the **Code** directory in the root of the project requires a data directory and StanfordNLP directory. The data directory should contain a proper JSON from [here](https://files.pushshift.io/reddit/comments/).
The StanfordNLP should contain the [stanford NLP required files and JAR](https://stanfordnlp.github.io/CoreNLP/). I didn't include them in the repository due to the large size
* Run python3 main.py to run project.
