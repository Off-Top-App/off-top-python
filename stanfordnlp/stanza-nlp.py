from flask import Flask, request, jsonify
from flask_apscheduler import APScheduler
import datetime
import stanza
import stanfordnlp
import logging
import json

app= Flask(__name__)

config = {
    'use_gpu': True,
    'processors': 'tokenize, mwt, pos, lemma, ner',
    'lang': 'en',
    'tokenize_model_path': './stanza_resources/en/tokenize/ewt.pt',
    'pos_model_path': './stanza_resources/en/pos/ewt.pt',
    'pos_pretrain_path': './stanza_resources/en/pretrain/ewt.pt',
    'lemma_model_path': './stanza_resources/en/lemma/ewt.pt',
    'ner_model_path': './stanza_resources/en/ner/ontonotes.pt'
}

def nlpProcess(task_status):
    with open("output.txt") as output:
        for line in output:
            line= line.strip()

    nlp = stanza.Pipeline(**config)
    doc = nlp(line)

    print("Type:", type(doc))
    print("\nAnalyzing speech for Off-Top...\n")
    print("\nPipeline -> " + line)
    print(*[f'token: {token.text}\tner: {token.ner}' for sent in doc.sentences for token in sent.tokens], sep='\n')

    print('\n-----------------------------------------')
    print("Full features of text: \n")
    print(*[f'Text: {word.text}\tuPOS: {word.upos}\txPOS: {word.xpos}\tlemma: {word.lemma}\tFeatures: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
    print(task_status, str(datetime.datetime.now()))

if __name__ == '__main__':
    scheduler= APScheduler()
    scheduler.add_job(func= nlpProcess, args=['Analyzed Speech.'], trigger= 'interval', id= 'job', seconds= 10)
    scheduler.start()
    app.run(port= 8000)
