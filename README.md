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

- Need to download pre-trained English model and extract it using:
	`curl -LO https://github.com/mozilla/deepspeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz tar xvf deepspeech-0.6.1-models.tar.gz`
	*Make sure to rename the models folder to "deepspeech-models".

**Description:**
- Inside this branch navigate into mozilla-deepspeech. You will see a script called mds:
  `mds.py` - Sets the pre-trained model arguments, and takes in an audio file from mozilla-deepspeech/audio folder, and returns the results in output.txt inside the same folder.

**How to use:**
- Locate the directory of `mds.py` inside mozilla-deepspeech and then run `python3 mds.py`. This will automatically transcribe the audio file and generate a .txt file with the content that can be found in the directory.
- Check the output.txt after the script runs to verify the results.



### Stanford CoreNLP/Stanza:
Python script that takes in input as a text file containing the results from MozillaDeepSpeech and performs the following Natural Language Processing operatiopns using the StanfordNLP library, currently known as Stanza:
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
   
- Need to have stanza package installed using:
   (Linux) `sudo apt-get install stanza`
   (Windows)`pip3 install stanza`
   (Mac) `pip3 install stanza`

- Need to download the pre-trained English model and extract it using:
	Launch the Python interactive interpreter and first, run `import stanza` then, `stanza.download('en', '~/stanza_resources)`
	*By default, Stanza stores its models in a folder in your home directory. The English model should be downloaded to `off-top-python/stanfordnlp`.
	*Make sure to specify your own directory (the second argument in the download command.
	*Make sure the name of the model folder is "stanza_resources".

**Description:**
- Inside this branch navigate into stanfordnlp. You will see a script called ner.py
  `ner.py` - Takes in input as a text file and prints the processed results (Tokens, POS', NER tags).

**How to use:**
Locate the directory of `ner.py` inside stanfordnlp and then run `python3 ner.py`. This will automatically run the processes and generate the results on the terminal.
*Make sure you have the input .txt file in the same directory which is the same file that Mozilla DeepSpeech generated with the results.
