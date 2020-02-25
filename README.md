# off-top-python
Repository for Off-Top's Flask App and for our Machine Learning services.

### PDF Miner:
Python script that mines PDF files, converts them to text and creates a text file with all the collected data using PDF Miner library.

**Pre-Reqs:**
- Need to have Python3 installed and `pip3`.

- Need to set up a virtual environment in Python.
  - Use the following command to install virtual-env: 
   (Linux) `sudo apt install python3-venv`
   (Windows) `pip3 install virtualenv`
  - Create a virtual directory which has the required scripts using: `python3 -m venv my-venv`
  - Activate the virtual env using the following command: `source my-venv/bin/activate`

- Need to have pdfminer package installed using:
   (Linux) `sudo apt-get install python-pdfminer`
   (Windows)`pip3 install pdfminer`

**Description:**
- Inside this branch navigate into pdfminer/src. You will see 2 scripts:
  `pdf_miner_multiple.py` - Takes in multiple pdf files from a folder called pdf and returns .txt files inside a folder called txt in the branch.
  `pdf_miner_single.py` - Takes in a single pdf file hardcoded inside the script in the bottom and returns a .txt file version of the pdf inside the same directory.

**How to use:**
1. For multiple files - Locate the directory of `pdf_miner_multiple.py` inside pdfminer/src and then run `python3 pdf_miner_multiple.py`. This will automatically generate .txt files and can be found in the directory.

2. For single files - Locate the directory of `pdf_miner_single.py` inside pdfminer/src and then run `python3 pdf_miner_single.py`. This will display the pdf file in the terminal and automatically generate .txt file in the directory.
- Make sure to hardcode the pdf file's name inside the script which you want to convert if you're using the single miner.

