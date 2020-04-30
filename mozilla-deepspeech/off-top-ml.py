import os
import wave
import deepspeech
#import deepspeech-gpu
import stanza
import logging
import datetime
import json
import numpy as np
from shutil import copyfile
from timeit import default_timer as timer
from flask import Flask, request, jsonify
from flask_apscheduler import APScheduler
import ffmpeg
import librosa

def transcribeData():
    os.system('cmd /k "deepspeech --model deepspeech-models/output_graph.pbmm --audio audio/off-top-test.wav > output.txt"')
    shutil.copyfile(r'C:\\Users\\smika\\Desktop\\CSUN\\COMP 490\\OFF-TOP [Final Senior Design Project]\\Python\\Flask\\off-top-python\\mozilla-deepspeech\\output.txt', r'C:\\Users\\smika\\Desktop\\CSUN\\COMP 490\\OFF-TOP [Final Senior Design Project]\\Python\\Flask\\off-top-python\\stanfordnlp\\input.txt')
    print("Speech transcription complete.")

transcribeData()
