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

app= Flask(__name__)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
global data_pipeline
global t

config = {
    'use_gpu': True,
    'processors': 'tokenize, mwt, pos, lemma, ner',
    'lang': 'en'

}

model_file_path= 'deepspeech-models/output_graph.pbmm'
lm_file_path = 'deepspeech-models/lm.binary'
trie_file_path = 'deepspeech-models/trie'
BEAM_WIDTH = 500
LM_ALPHA = 0.75
LM_BETA = 1.85

model = deepspeech.Model(model_file_path, BEAM_WIDTH)
model.enableDecoderWithLM(lm_file_path, trie_file_path, LM_ALPHA, LM_BETA)
sample_rate= model.sampleRate()

print("\n")
nlp = stanza.Pipeline(**config)

def transcribe():
    t= 0
    inference_time= 0.0
    filename= 'audio/off-top-test.wav'
    w= wave.open(filename, 'r')
    rate= w.getframerate()
    frames= w.getnframes()
    buffer= w.readframes(frames)
    audio_length = len(buffer) * (1 / sample_rate)

    if (rate != sample_rate):
        print('Warning: original sample rate ' + str(rate) + 'Hz is lower than ' + str(sample_rate) + 'Hz. Up-sampling might produce erratic speech recognition.')

    data_16= np.frombuffer(buffer, dtype= np.int16)
    type_of= type(data_16)
    print(type_of)
    start= timer()
    result= model.stt(data_16)
    end= timer() - start
    t+= end
    logging.debug('Transcribed Data.', str(datetime.datetime.now()))
    logging.debug('Process took %0.3fs for %0.3fs audio file.' % (end, audio_length))
    data_pipeline= result
    print('Result: ', result)
    #return [result]

def nlpProcess(task_status):
    with open("output.txt") as output:
        for line in output:
            line= line.strip()
    #doc = nlp(line)
    doc = nlp(data_pipeline)
    print("Type:", type(doc))
    print("\nAnalyzing speech for Off-Top...\n")
    print("\nPipeline -> " + line)
    print(*[f'token: {token.text}\tner: {token.ner}' for sent in doc.sentences for token in sent.tokens], sep='\n')

    print('\n-----------------------------------------')
    print("Full features of text: \n")
    print(*[f'Text: {word.text}\tuPOS: {word.upos}\txPOS: {word.xpos}\tlemma: {word.lemma}\tFeatures: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
    print(task_status, str(datetime.datetime.now()))

def transcribeData():
    os.system('cmd /k "deepspeech --model deepspeech-models/output_graph.pbmm --audio audio/off-top-test.wav > output.txt"')
    shutil.copyfile(r'C:\\Users\\smika\\Desktop\\CSUN\\COMP 490\\OFF-TOP [Final Senior Design Project]\\Python\\Flask\\off-top-python\\mozilla-deepspeech\\output.txt', r'C:\\Users\\smika\\Desktop\\CSUN\\COMP 490\\OFF-TOP [Final Senior Design Project]\\Python\\Flask\\off-top-python\\stanfordnlp\\input.txt')
    print("Speech transcription complete.")

if __name__ == '__main__':
    scheduler= APScheduler()
    scheduler.add_job(func= transcribe, trigger= 'interval', id= 'mds_job', seconds= 25, max_instances= 10)
    #scheduler.add_job(func= nlpProcess, args=['Analyzed Speech.'], trigger= 'interval', id= 'nlp_job', seconds= 25, max_instance= 10)
    scheduler.start()
    app.run(debug=True)
