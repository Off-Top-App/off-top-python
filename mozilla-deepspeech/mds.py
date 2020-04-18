import os
from shutil import copyfile

def transcribeData():
    os.system('cmd /k "deepspeech --model deepspeech-models/output_graph.pbmm --audio audio/off-top-test.wav > output.txt"')
    shutil.copyfile(r'C:\\Users\\smika\\Desktop\\CSUN\\COMP 490\\OFF-TOP [Final Senior Design Project]\\Python\\Flask\\off-top-python\\mozilla-deepspeech\\output.txt', r'C:\\Users\\smika\\Desktop\\CSUN\\COMP 490\\OFF-TOP [Final Senior Design Project]\\Python\\Flask\\off-top-python\\stanfordnlp\\input.txt')
    print("Speech transcription complete.")

transcribeData()
