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

### Mozilla DeepSpeech:
Python script that takes a .WAV audio input and transcribes the content into a text file called output.txt

**Pre-Reqs:**
- Need to have Python3 installed and `pip3`.

- Need to set up a virtual environment in Python skip to 'Activate' if you already have one set up.
  - Use the following command to install virtual-env: 
   (Linux) `sudo apt install python3-venv`
   (Windows) `pip3 install virtualenv`
  - Create a virtual directory which has the required scripts using: `python3 -m venv my-venv`
  - Activate the virtual env using the following command: `source my-venv/bin/activate`


- Need to have PyTorch package installed using:
   (Linux) `pip3 install torch torchvision`
   (Windows)`pip3 install torch===1.4.0 torchvision===0.5.0 -f https://download.pytorch.org/whl/torch_stable.html`
   (Mac) `pip3 install torch torchvision` *MacOS Binaries dont support CUDA, install from source if CUDA is needed

- Need to have deepspeech package installed using:
   (Linux) `sudo apt-get install deepspeech`
   (Windows)`pip3 install deepspeech`

- Need to have sox package installed using:
   (Linux) `sudo apt-get install -y sox`
   (Windows) download and install the .exe file from `https://sourceforge.net/projects/sox/files/sox/`
   (Mac) install `homebrew` using: `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null`
		 install `sox` using: `brew install sox`
   
- Need to download pre-trained English model and extract it using:
	`curl -LO https://github.com/mozilla/deepspeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz tar xvf deepspeech-0.6.1-models.tar.gz`
	*Make sure to rename the models folder to "deepspeech-models".

**Description:**
- Inside this branch navigate into mozilla-deepspeech. You will see a script called mds:
  `mds.py` - Sets the pre-trained model arguments, and takes in an audio file from mozilla-deepspeech/audio folder, and returns the results in output.txt inside the same folder.

**How to use:**
- Locate the directory of `mds.py` inside mozilla-deepspeech and then run `python3 mds.py`. This will automatically transcribe the audio file and generate a .txt file with the content that can be found in the directory.
- Another way of using the MDS instance is by calling the `transcribeData()` function in another instance.
- Check the output.txt after the script runs to verify the results.

### Stanford CoreNLP/Stanza:
Python Flask server that checks for input from a text file containing the results from MozillaDeepSpeech and performs the following Natural Language Processing operatiopns using the StanfordNLP library, currently known as Stanza:
- TokenizeProcessor.
- POSProcessor.
- LemmaProcessor.
- NERProcessor.

**Pre-Reqs:**
- Need to have Python3 installed and `pip3`.

- Need to set up a virtual environment in Python skip to 'Activate' if you already have one set up.
  - Use the following command to install virtual-env: 
   (Linux) `sudo apt install python3-venv`
   (Windows) `pip3 install virtualenv`
  - Create a virtual directory which has the required scripts using: `python3 -m venv my-venv`
  - Activate the virtual env using the following command: `source my-venv/bin/activate`
   
- Need to have flask package installed using:
   (Linux) `sudo apt-get install flask`
   (Windows)`pip3 install flask`
   (Mac) `pip3 install flask`

- Need to have flask_apscheduler package installed using:
   (Windows)`pip3 install flask_apscheduler`
   (Mac) `pip3 install flask_apscheduler`

- Need to have datetime package installed using:
   (Windows)`pip3 install datetime`
   (Mac) `pip3 install datetime`

- Need to have stanza package installed using:
   (Linux) `sudo apt-get install stanza`
   (Windows)`pip3 install stanza`
   (Mac) `pip3 install stanza`

- Need to download the pre-trained English model and extract it using:
	Launch the Python interactive interpreter and first, run `import stanza` then, `stanza.download('en', '~/stanza_resources')`
	*By default, Stanza stores its models in a folder in your home directory. The English model should be downloaded to `off-top-python/stanfordnlp`.
	*Make sure to specify your own directory (the second argument in the download command.
	*Make sure the name of the model folder is "stanza_resources".

**Description:**
- Inside this branch navigate into stanfordnlp. You will see a script called `stanza-nlp.py` which is a Flask server.
`stanza-nlp.py` - The Flask server runs through a task scheduler, checks for input from a text file, and displays the processed results (Tokens, POS', NER tags) on the terminal every 10 seconds.

**How to use:**
Locate the directory of `stanza-nlp.py` inside stanfordnlp and then run `python3 stanza-nlp.py`. This will automatically run the processes and generate the results on the terminal.
*Make sure you have the input .txt file in the same directory which is the same file that Mozilla DeepSpeech generated with the results.

### NER Training Dataset [ML] | Webscraping | Data Preprocessing:
This part deals with Acquiring data from the web, preprocess it, clean it and annotate it to be well formatted as a training dataset.

**Pre-Reqs:**
- Need to have Python3 installed and `pip3`.

- Need to set up a virtual environment in Python skip to 'Activate' if you already have one set up.
  - Use the following command to install virtual-env: 
   (Linux) `sudo apt install python3-venv`
   (Windows) `pip3 install virtualenv`
  - Create a virtual directory which has the required scripts using: `python3 -m venv my-venv`
  - Activate the virtual env using the following command: `source my-venv/bin/activate`
   
- Need to have requests package installed using:
   - (Linux) `sudo apt-get install requests`
   - (Windows)`pip3 install requests`
   - (Mac) `pip3 install requests`

- Need to have urllib.request package installed using:
   - (Windows)`pip3 install urllib2`
   - (Mac) `pip3 install urllib2`

- Need to have pandas package installed using:
   - (Windows)`pip3 install pandas`
   - (Mac) `pip3 install pandas`

- Need to have beautifulsoup4 package installed using:
   - (Linux) `sudo apt-get install beautifulsoup4`
   - (Windows)`pip3 install beautifulsoup4`
   - (Mac) `pip3 install beautifulsoup4`

- Need to have re2 package installed using:
   - (Linux) `sudo apt-get install re2`
   - (Windows)`pip3 install re2`
   - (Mac) `pip3 install re2`
   
- Need to have nltk package installed using:
   - (Linux) `sudo apt-get install nltk`
   - (Windows)`pip3 install nltk`
   - (Mac) `pip3 install nltk`
   
- Need to have unicodedata package installed using:
   - (Linux) `sudo apt-get install unicodedata`
   - (Windows)`pip3 install unicodedata`
   - (Mac) `pip3 install unicodedata`

**Description:**
- In order to build a training dataset for our custom NERProcessor model we went used webscraping tools to mine terms, names, keywords brands related to Sport and Food.
- The data we gathered was not in the perfect form, we had to clean and preprocess it for example: Dataset generation, splitting, tokenization, character removal, filtering out punctuation, etc.
- The training dataset had to be in BIO format, that's why we annotated our data accordingly.
- Inside this branch navigate into stanfordnlp/preprocessing. You will see two folders, 'clean-data' which includes the processed/cleaned data, and 'data' which includes raw unprocessed and scraped data. 
You will also find 3 Python scripts - `cleaning.py`, `deep_clean.py`, `datasetGen.py` which were used to preprocess and clean the raw data.
- Each website you scrape needs a dedicated script to fit its outline. Inside the same branch navigate into stanfordnlp/webscraping and you will find 12 Python scripts - `webScrape.py`, `webScraping.py`, `webScrapingFastFood.py` which were used to scrape raw data from various websites.
- The resulting annotated data and built training dataset can be found inside stanfordnlp/dataset under `offtop-main-train.bio`

**How to use:**
Locate the directory of `cleaning.py`, `deep_clean.py`, `datasetGen.py` inside stanfordnlp/preprocessing and then for example run `python3 deep_clean.py`. This will automatically run the process, generate the results on the terminal, and create an output file called clean-output.txt
Locate the directory of `webScrape.py`, `webScraping.py`, `webScrapingFastFood.py` inside stanfordnlp/webscraping and then for example run `python3 webScrape.py`. This will automatically run the process, generate the results on the terminal, and create an output file called food-scrape.txt