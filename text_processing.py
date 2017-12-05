# -*- coding: utf-8 -*-

"""
__author__ = "Ahirton Lopes e Rodrigo Pasti"
__copyright__ = "Copyright 2015/2016, Mackenzie University"
__credits__ = ["Ahirton Lopes", "Rodrigo Pasti", "Leandro de Castro"]
__license__ = "None"
__version__ = "1.0"
__maintainer__ = "Ahirton Lopes"
__email__ = "ahirton.xd@gmail.com"
__status__ = "Beta"
"""
'''
"""
-----------------------------------------------------------------------------------------------------------------------
FUNÇÕES PARA TRATAMENTO TEXTUAL E FORMATAÇÃO
-----------------------------------------------------------------------------------------------------------------------
"""
'''

import re
import nltk
import semantic_dictionaries
import unicodedata
import file_utils
from nltk.corpus import mac_morpho
      
"""
Recebe uma lista de documentos e retorna o tratamento destes na forma de lista
de tokens
"""
def tokenize(documents):
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        #adicionar a lista
        #documentsProcessed.append(nltk.word_tokenize(documents[iDoc].decode('utf-8')))
        documentsProcessed.append(nltk.word_tokenize(documents[iDoc])) # Adiciona à lista a partir da ordenação
    return documentsProcessed
   # print docsPro[0:10]
    
"""
# Recebe uma lista de documentos na forma de tokens e retorna os respectivos bigrams
"""
def tokenizeBigram(documents):
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados  
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados      
        #adicionar a lista
        documentsProcessed.append(nltk.bigrams(documents[iDoc])) # Adiciona à lista a partir da ordenação    
    return documentsProcessed
   # print docsPro[0:10]

"""
Separa um texto em sentenças (frases) - Aqui, por ora em portugues!
"""
def tokenize_sentence(documents):    
    tkr = nltk.data.load('tokenizers/punkt/portuguese.pickle') # Dicionário em Português para reconhecimentos das diferentes palavras/pontuação   
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        documentsProcessed.append(tkr.tokenize(documents[iDoc])) # Adiciona à lista a partir da ordenação
    return documentsProcessed

"""
Remove stop words de uma lista de documentos
"""
def remove_stopwords(documents):
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    stopwords = semantic_dictionaries.stop_words() + semantic_dictionaries.stop_words_sincronica() # Indicação das stopwrods a serem utilizadas, via dicionários 
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        tokens = documents[iDoc] # Lista para verificação dos tokens gerados via documentos       
        #stop words para cada token do documento corrente
        nTokens = len(tokens) # len = Retorna o comprimento dos tokens gerados
        importantWords = [] # Cria lista para as palavras importantes a não serem eliminadas
        for iToken in range(0,nTokens): # Para cada token gerado segundo ordenação            
            if tokens[iToken] not in stopwords: # Verificar se cada token é ou não stopword
                importantWords.append(tokens[iToken]) # Se não for stopword, processa-se como palavra importante
        documentsProcessed.append(importantWords) # Reconfigura-se o documento com as stopwrods removidas
    return documentsProcessed
    
"""
# Faz o stemming de uma lista de documentos (disponivel: Pt e En)
"""
def stemming(documents,lang):
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    if lang == 'Pt': # Se linguagem português
        stemmer = nltk.stem.RSLPStemmer() # Stemmer via NTLK para língua portuguesa
    elif lang == 'En': # Se linguagem inglês
        stemmer = nltk.stem.lancaster.LancasterStemmer() # Stemmer via NTLK para língua inglesa
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        tokens = documents[iDoc] # Lista para verificação dos tokens gerados via documentos    
        nTokens = len(tokens) # len = Retorna o comprimento dos tokens gerados
        stemWords = [] # Cria lista de palavras para stemming
        for iToken in range(0,nTokens): # Para cada token gerado segundo ordenação        
            stemWords.append(stemmer.stem(tokens[iToken])) # Processa-se os tokens eleiminando as variações morfológicas de uma palavra (redução)
        tokens = stemWords # Lista para verificação dos tokens gerados (sentenças sem variações morfológicas)
        documentsProcessed.append(tokens) # Reconfigura-se o documento com as as variações morfológicas removidas
    return documentsProcessed 
    

"""
Remove palavras de um documento que contenham algum dos simbolos contidos em 
uma lista de entrada
"""
def remove_words_with(documents,listSym):    
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        tokens = documents[iDoc] # Lista para verificação dos tokens gerados via documentos
        tokensNR = [] # Cria lista para os tokens gerados
        nTokens = len(tokens) # len = Retorna o comprimento dos tokens gerados  
        for iToken in range(0,nTokens): # Para cada token gerado segundo ordenação verifica-se a existência dos símbolos em listSym
            foundSymbol = False
            for sym in listSym:               
                if tokens[iToken].find(sym) != -1:
                    foundSymbol = True
                    break                    
            if foundSymbol == False:
                tokensNR.append(tokens[iToken])                
        #if len(tokensNR) > 0:
        documentsProcessed.append(tokensNR) 
    return documentsProcessed
    
    
"""
# Faz a conversão de um texto para todas as letras minusculas   
"""   
def text_lower(documents):
    nDocs = len(documents)
    documentsProcessed = []     
    for iDoc in range(0,nDocs):
        tokens = documents[iDoc]        
        nTokens = len(tokens)        
        for iToken in range(0,nTokens):
            tokens[iToken] = tokens[iToken].lower()        
        documentsProcessed.append(tokens)
    return documentsProcessed

"""
# Remove pontuações de um conjunto de documentos
"""
def remove_punctuation(documents):  
    nDocs = len(documents)
    documentsProcessed = []     
    for iDoc in range(0,nDocs):
        tokens = documents[iDoc]
        tokensNR = []
        nTokens = len(tokens)       
        for iToken in range(0,nTokens):
           # print tokens[iToken].decode('utf-8')           
            punctuation = ',.?!:;" '
            for sym in punctuation:
                tokens[iToken] = tokens[iToken].replace(sym,'')
            #print tokens[iToken]
            if len(tokens[iToken]) > 0:
                tokensNR.append(tokens[iToken])
        #if len(tokensNR) > 0:
        documentsProcessed.append(tokensNR) 
    return documentsProcessed
#    nDocs = len(documentsProcessed)
#    for iDoc in range(0,nDocs):
#        if len(documentsProcessed[iDoc])<1:
#            print 'fuuuuuuuuuuuuuuuuu'
#    return documentsProcessed



"""
# Remove acentos de um conjunto de documentos
"""
def remove_accents(documents):  
    nDocs = len(documents)
    documentsProcessed = []     
    for iDoc in range(0,nDocs):
        tokens = documents[iDoc]
        nTokens = len(tokens)       
        for iToken in range(0,nTokens):
            #print tokens[iToken].decode('utf-8')
            #uStr = tokens[iToken].decode('utf-8')#unicode(tokens[iToken])
            strNorm = unicodedata.normalize('NFKD', tokens[iToken])#.decode('utf-8'))
            tokens[iToken] = strNorm.encode('ASCII', 'ignore')            
            #print tokens[iToken]
        documentsProcessed.append(tokens)
    return documentsProcessed
    
"""
Faz um tagging (analise morfologica de uma lista de documentos)
"""
def tagging(documents):
    nDocs = len(documents)
#    print nDocs
    documentsProcessed = []
    unigram_tagger = []
    try:        
        unigram_tagger = file_utils.load_object('tagger1','tagger', None)
        print unigram_tagger          
    except:
        train_set =  mac_morpho.tagged_sents()
        #test_set =  mac_morpho.tagged_sents()[10001:10010]   
        unigram_tagger = nltk.UnigramTagger(train_set)
        file_utils.save_object(unigram_tagger, 'tagger1','tagger', None)
    
    for iDoc in range(0,nDocs):
        #tokens = documents[iDoc]    
        documentsProcessed.append(unigram_tagger.tag(documents[iDoc]))
    return documentsProcessed

