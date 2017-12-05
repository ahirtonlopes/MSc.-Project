# -*- coding: utf-8 -*-
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
        #documentsProcessed.append(nltk.word_tokenize(documents[iDoc].decode('utf-8')))
        documentsProcessed.append(nltk.word_tokenize(documents[iDoc])) # Adiciona à lista a partir da ordenação
    return documentsProcessed 
    

    
    