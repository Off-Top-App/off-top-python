import stanfordnlp

config = {
    'use_gpu': True,
    'processors': 'tokenize,mwt,pos,lemma,depparse', # Comma-separated list of processors to use
    'lang': 'en', # Language code for the language to build the Pipeline in
    'tokenize_model_path': './en_ewt_models/en_ewt_tokenizer.pt', # Processor-specific arguments are set with keys "{processor_name}_{argument_name}"
    'mwt_model_path': './en_ewt_models/en_ewt_mwt_expander.pt',
    'pos_model_path': './en_ewt_models/en_ewt_tagger.pt',
    'pos_pretrain_path': './en_ewt_models/en_ewt.pretrain.pt',
    'lemma_model_path': './en_ewt_models/en_ewt_lemmatizer.pt',
    'depparse_model_path': './en_ewt_models/en_ewt_parser.pt',
    'depparse_pretrain_path': './en_ewt_models/en_ewt.pretrain.pt'
}
nlp = stanfordnlp.Pipeline(**config) # Initialize the pipeline using a configuration dict
doc = nlp("The Data Scientist will be responsible for designing and implementing a program for analyzing complex, large-scale data sets used for modeling, data mining, research, and predictive analysis purposes.") # Run the pipeline on input text
#doc.sentences[0].print_tokens()

for i, sentence in enumerate(doc.sentences):
    print(f"====== Sentence {i+1} tokens =======")
    print(*[f"index: {token.index.rjust(3)}\ttoken: {token.text}" for token in sentence.tokens], sep='\n')
print(type(doc))
#doc.sentences[0].tokenize()
#doc.sentences[0].print_string()
print('------')
doc.sentences[0].print_dependencies()
#token = doc.token[0]
#print(token)
