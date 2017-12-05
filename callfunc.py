#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
__author__ = "Ahirton Lopes"
__copyright__ = "Copyright 2015/2016, Mackenzie University"
__credits__ = ["Ahirton Lopes", "Rodrigo Pasti", "Leandro de Castro"]
__license__ = "None"
__version__ = "1.0"
__maintainer__ = "Ahirton Lopes"
__email__ = "ahirton.xd@gmail.com"
__status__ = "Beta"
"""
"""
'''
-----------------------------------------------------------------------------------------------------------------------
LEITURA DE TWEETS CONTIDOS EM ARQUIVO CSV E EXTRACAO DE META-ATRIBUTOS TEXTUAIS
-----------------------------------------------------------------------------------------------------------------------
"""
'''
#Passos:
    #--------------------------------------------------------------------------------------------------------
    # Devem ser utilizados dois metodos para a viabilizacao dos testes de classificacao 
    #--------------------------------------------------------------------------------------------------------
    #(1) Metodo 1 - Coleta automatica tweet a tweet por arquivos .csv
    #(2) Metodo 2 - Coleta automatica de tweets concatenados por arquivos .csv
    #--------------------------------------------------------------------------------------------------------
'''
import sys
from extract_meta_attributes import MetaAttributes
import csv
import text_processing as tp

'''
-----------------------------------------------------------------------------------------------------------------------
(1) MECANISMO DE COLETA AUTOMATICA DE TWEETS POR ARQUIVO CSV - METODO 1 (TWEET A TWEET)
-----------------------------------------------------------------------------------------------------------------------
'''

#Coleta automatica tweet a tweet via arquivos .csv e utilizacao do extrator de meta-atributos

#with open("cidinhacampos_tweets.csv", "rb") as f:
#    reader = csv.reader(f, delimiter="\t")
#    for i, line in enumerate(reader):

#        print 'tweet [{}] = {}'.format(i, line)        
        
#        tweetatweet = MetaAttributes('{}'.format(line))
#        print tweetatweet.all_meta_attributes
#        sys.stdout = open("logtweetatweetcidihacampos.txt", "a")
        
'''
-----------------------------------------------------------------------------------------------------------------------
(2) MECANISMO DE COLETA AUTOMATICA DE TWEETS POR ARQUIVO CSV - METODO 2 (CONCATENADOS)
-----------------------------------------------------------------------------------------------------------------------
'''

# Concatenacao dos tweets de cada linha em um so texto

#with open("[CM30] realwbonner_tweets.csv", "rb") as f:
#     reader = csv.reader(f, delimiter="\t")
#     master_row = [""]
     
#     for row in reader:
#         master_row = [master_row[col] + row[col] for col in range(0,len(master_row))]
#         print master_row

#Coleta automatica dos tweets concatenados em arquivo .csv e utilizacao do extrator de meta-atributos         
         
#with open("[CM30] realwbonner_tweets.csv", "rb") as f:
#    reader = csv.reader(f, delimiter="\t")
#    for i, line in enumerate(reader):
        
#        print 'tweet [{}] = {}'.format(i, line)        

#        concatenados = MetaAttributes('{}'.format(line))
#        sys.stdout = open("logconcatenadosm30.txt", "a")
#        print concatenados.all_meta_attributes

'''
-----------------------------------------------------------------------------------------------------------------------
(3) TESTE DO EXTRATOR DE META-ATRIBUTOS (TODOS OS META-ATRIBUTOS) E NORMALIZACAO DO VETOR NUMPY RESULTANTE
-----------------------------------------------------------------------------------------------------------------------
'''

#m1 = MetaAttributes('[Devido ao sucesso de 10 Mandamentos, Record estica o numero de pragas pra 15! @sensacionalista]')

#print m1.all_meta_attributes

# Normalizacao do vetor numpy resultante

#oldmin = min(m1.all_meta_attributes)
#oldmax = max(m1.all_meta_attributes)
#oldrange = oldmax - oldmin
#newmin = 0.
#newmax = 1.
#newrange = newmax - newmin
#if oldrange == 0:           
    #if oldmin < newmin:     
        #newval = newmin
    #elif oldmin > newmax:    
        #newval = newmax
    #else:                    
        #newval = oldmin
    #normalm1 = [newval for v in m1.all_meta_attributes]
#else:
    #scale = newrange / oldrange
    #normalm1 = [(v - oldmin) * scale + newmin for v in m1.all_meta_attributes]

#print normalm1

'''
-----------------------------------------------------------------------------------------------------------------------
(4) TESTE DO EXTRATOR DE META-ATRIBUTOS (UM A UM)
-----------------------------------------------------------------------------------------------------------------------
'''

#m = MetaAttributes('Obrigada aos chantagistas salafrarios chantagiados de merda adorei!')

#print m.C1
#print m.C2
#print m.C3
#print m.C4
#print m.C5
#print m.C6
#print m.C7
#print m.C8
#print m.C9
#print m.C10
#print m.C11
#print m.C12
#print m.C13
#print m.C14
#print m.C15
#print m.C16

#print m.W1
#print m.W2
#print m.W3
#print m.W4
#print m.W5
#print m.W6
#print m.W7
#print m.W8
#print m.W9
#print m.W10
#print m.W11
#print m.W12
#print m.W13_N

#print m.TS1
#print m.TS2
#print m.TS3
#print m.TS4
#print m.TS5
#print m.TS6
#print m.TS7
#print m.TS8
#print m.TS9
#print m.TS10

#print m.TM1
#print m.TM2
#print m.TM3
#print m.TM4
#print m.TM5
#print m.TM6

#print m.PC1
#print m.PC2
#print m.PC3
#print m.PC4
#print m.PC5

'''
-----------------------------------------------------------------------------------------------------------------------
(5) TESTE DO PROCESSADOR TEXTUAL
-----------------------------------------------------------------------------------------------------------------------
'''
#print ("oi")
docsTokenized = tp.remove_accents(['GOVERNO de SP vai pagar 25 mil a quem denunciou suspeito de matar ambulante no Metro. Secretaria de Seguranca Publica fixou valor nesta quarta (18) no Diario Oficial.'])
print(docsTokenized)
