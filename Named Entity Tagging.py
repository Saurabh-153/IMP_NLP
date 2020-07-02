import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)
sent

......................................

from spacy.en import English

nlp = English()
parsed_text = nlp(raw_text)

def is_content_word(token):
    lemma_mask = {'do', 'be', 'use', 'have'}
    pos_mask = {'PUNCT', 'SPACE'}
    tag_mask = {'TO', 'CC', 'IN', 'DT', 'PRP$', 'PRP', 'EX'}
    return not token.tag_.startswith('W') and token.lemma_ not in lemma_mask and token.pos_ not in pos_mask and token.tag_ not in tag_mask

def some_parsing_routine(parsed_text):
    for chunk in parsed_text.noun_chunks:
       chunk_token.orth_
       chunk.root.head.orth_
    for ent in parsed_text.ents:
        ent.orth_
    for token in parsed_text:
        token.orth_
        if not is_content_word(token):
        if token.pos_ == 'VERB':
            ......
        elif token.pos_ == 'NOUN':
            ......
        else:
            ......
    for sent in parsed_text.sents:
        sent.orth_
        
