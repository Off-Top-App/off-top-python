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