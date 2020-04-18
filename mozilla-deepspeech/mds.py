import os
from shutil import copyfile

def transcribeData():
    os.system('cmd /k "deepspeech --model deepspeech-models/output_graph.pbmm --audio audio/off-top-test.wav > output.txt"')
    copyfile('output.txt', '/stanfordnlp//newname.ext')
    print("Speech transcription complete.")

transcribeData()
