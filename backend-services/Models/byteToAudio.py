
import scipy.io.wavfile
import numpy as np
import soundfile as sf

# scipy writes the bytes to audio file using numpyarray. Here 16 denotes sample rate (samples/sec)
# opened a file containg byte strings and then converted them to a numpyarray and to .wav file

def convert_bytes_to_audio():
    f = open("test.txt","r")
    for line in f:
        scipy.io.wavfile.write('format.wav',16, np.frombuffer(str.encode(line),dtype ='B'))
    f.close()

def main():
    convert_bytes_to_audio()

if __name__ == '__main__':
    convert_bytes_to_audio()
