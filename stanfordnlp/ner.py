import stanza
import os
import stanfordnlp

config = {
    'use_gpu': True,
    #'tokenize_pretokenized': True,
    #'no_ssplit': True,
    'processors': 'tokenize, mwt, pos, lemma, ner', # Comma-separated list of processors to use
    'lang': 'en', # Language code for the language to build the Pipeline in
    'tokenize_model_path': './stanza_resources/en/tokenize/ewt.pt',
    #'mwt_model_path': './stanza_resources/en/pretrain/ewt.pt',
    'pos_model_path': './stanza_resources/en/pos/ewt.pt',
    'pos_pretrain_path': './stanza_resources/en/pretrain/ewt.pt',
    'lemma_model_path': './stanza_resources/en/lemma/ewt.pt',
    'ner_model_path': './stanza_resources/en/ner/ontonotes.pt'
}

with open("output.txt") as output:
    for line in output:
        line= line.strip()

nlp = stanza.Pipeline(**config)
doc = nlp(line)

print("Type:", type(doc))
print("\nAnalyzing speech for Off-Top...\n")
print("Pipeline -> " + line)
print(*[f'token: {token.text}\tner: {token.ner}' for sent in doc.sentences for token in sent.tokens], sep='\n')

print('\n-----------------------------------------')
print("Full features of text: \n")
print(*[f'Text: {word.text}\tuPOS: {word.upos}\txPOS: {word.xpos}\tlemma: {word.lemma}\tFeatures: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
