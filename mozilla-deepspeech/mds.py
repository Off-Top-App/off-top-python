import os
import wave
import deepspeech
import logging
import numpy as np
from shutil import copyfile
from timeit import default_timer as timer

app= Flask(__name__)

model_file_path= 'deepspeech-models/output_graph.pbmm'
lm_file_path = 'deepspeech-0.6.0-models/lm.binary'
trie_file_path = 'deepspeech-0.6.0-models/trie'
BEAM_WIDTH = 500
LM_ALPHA = 0.75
LM_BETA = 1.85
model = deepspeech.Model(model_file_path, BEAM_WIDTH)
model.enableDecoderWithLM(lm_file_path, trie_file_path, LM_ALPHA, LM_BETA)

filename= 'audio/off-top-test.wav'
w= wave.open(filename, 'r')
inference_time= 0.0
rate= w.getframerate()
frames= w.getnframes()
buffer= w.readframes(frames)
sample_rate= model.sampleRate()
audio_length = len(audio) * (1 / frames)

if

start= timer()
result= model.stt(data_16)
end= timer() - start
time+= end
logging.debug('Process took %0.3fs for %0.3fs audio file.' % (end, audio_length))

def transcribeData():
    os.system('cmd /k "deepspeech --model deepspeech-models/output_graph.pbmm --audio audio/off-top-test.wav > output.txt"')
    shutil.copyfile(r'C:\\Users\\smika\\Desktop\\CSUN\\COMP 490\\OFF-TOP [Final Senior Design Project]\\Python\\Flask\\off-top-python\\mozilla-deepspeech\\output.txt', r'C:\\Users\\smika\\Desktop\\CSUN\\COMP 490\\OFF-TOP [Final Senior Design Project]\\Python\\Flask\\off-top-python\\stanfordnlp\\input.txt')
    print("Speech transcription complete.")


if __name__ == '__main__':
    app.run(debug=True)
