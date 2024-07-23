# MSE Group Project

## Setup Project
Create a virtual environment. After activating the virtual environment, install the dependencies:
```
pip install -r requirements.txt
```
Download the embedding_data.json and put it into app/index_data:
```
https://drive.google.com/file/d/18gihYE29E6mfDoqZmorzufEldpFl_9Lt/view?usp=sharing
```
To get the user interface of the search engine running, execute `main.py` from the root of the repository:
```
python3 app/main.py
```
If you want to get the result lists of multiple queries in form of a tab-separated .txt file, store a file named `queries.txt` in the root of the repository. Then execute `main.py` from the root of the repository with the flag `-b` or `-batchfile`:
```
python3 app/main.py -b
```
The result will be stored in `results.txt`.

Our code of the crawler can be found in the following repository (by Julien):
```
https://github.com/julien32/modern-search-engines-crawler
```
