# MSE Group Project

## Setup Project
Create a virtual environment. After activating the virtual environment, install the dependencies:
```
pip install -r requirements.txt
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
