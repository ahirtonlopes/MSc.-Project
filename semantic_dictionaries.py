#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
"""
__author__ = "Rodrigo Pasti e Ahirton Lopes"
__copyright__ = "Copyright 2015/2016, Mackenzie University"
__credits__ = ["Ahirton Lopes", "Rodrigo Pasti", "Leandro de Castro"]
__license__ = "None"
__version__ = "1.0"
__maintainer__ = "Ahirton Lopes"
__email__ = "ahirton.xd@gmail.com"
__status__ = "Beta"
"""
"""
#Palavras que não agregam semantica alguma ao texto
def stop_words():
    sw = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j',
          'k','l','ç','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U',
          'I','O','P','A','S','D','F','G','H','J','K','L','Ç','Z','X','C','V',
          'B','N','M','!','@','#','$','%','¨','&','*','(',')','_','+','-','--','=',
          '´','`','^','~',':',';','?','|','{','[','}','<','>','.',',','/','//','...',
          '"',"'","''",'``','no', 'na', 'do', 'da', 'de', 'as', 'os', 'nos', 'nas', 
          'dos', 'das', 'se', 'em','para','que','pela','pelo', 'com','sem',
          'um','uma','pra',' ', 'aos', 'etc', 'e/ou', 'ou','ate','por']
    return sw
    

def stop_words_sincronica():
    states1 = ['sp','rj','rs','mg']
    states2 = ['são','paulo','rio','grande','sul','parana']
    names = ['maria','silva','antonio']
    
    return states1+states2+names
'''
Sentiment analysis
'''
def positive_words():
    
#    pw = ['lindo', 'pena', 'gostei', 'adorei', 'adoro', 'ótimo', 'favorito', 'amei', 
#          'maravilhoso', 'melhor', 'legal', 'massa', 'bom', 'rindo', 'engraçado', 
#          'engraçada', 'top', 'curti', 'curtindo', 'amo', 'amei', 'sensacional', 
#          'gosto', 'fã', 'fan', 'liked', 'saudade', 'imperdível', 'preferido','feliz',
#          'demais','d+']
    pw = ['lindo', 'gostei', 'adorei', 'adoro', 'ótimo', 'favorito', 'amei', 
          'maravilhoso', 'melhor', 'legal', 'massa', 'rindo', 'engraçado', 
          'engraçada', 'amo', 'amei', 'sensacional', 
          'gosto', 'fã','predileto', 'imperdível', 'preferido','feliz',
          'demais','d+','saudade']               
    return pw
    
    
def negative_words():
    #nw = ['ruim','pessimo','merda','=(']
   # nw = ['ruim','pessimo','merda','calamidade','lixo','vergonha','=(','=/',':(',':-(']
    nw = ['ruim','pessimo', 'horrivel', 'calamidade','lixo','vergonha',
          'horrivel', 'besta','chato','merda', 'bosta', 'sacana', 'entendiante',
          'enjoei', 'triste', 'pior', 'odeio', 'tédio', 'burrice', 'idiota', 
          'imbecil', 'enojado','absurdo','absurdos']
    return nw
    #EXEMPLOS DE PALAVRAS BIGRAMAS
   # nw = ['é mal', 'era mal', 'é ruim', 'era ruim', 'foi ruim']
       
def positive_words_bigram():
    nwb = [('sem', 'graça'), ('muito','ruim'), ('muito', 'chato'), ('muito', 'legal'),('uma','pena')]
    return nwb
    

def not_subjetive_words():
    nsw = [('boa','noite')]
    return nsw
    
def positive_emoticons():
    pe = ['=3','=-3','=D','=-D','=p','p=','P=','*)','(*','*-)','(-*','*-*','*--*',
          '*_*','*__*','*.*',':)','(:',':-)','(-:',':-))','((-:',':]','[:',':^)','(^:',
          ':}','{:',':>','<:',':3',':b',':B','=B','=B',':-b',':c)',':D',':d',':-D',
          ':o)',':P',':p',':-P',':-p',':Ů',':-Ů',';)','(;',';-)','(-;',';]','[;',
          ';-]','[-;',';^)','(^;',';D',';d','^^','^.^','^..^','^_^','^__^','^-^',
          '^--^','(=','=]','[=','8-)','(-8','8)','(8','8D','8-D','xD','x-D','xp',
          'XP','X-P','x-p','o/','\o/']
    return pe
    
def negative_emoticons():
    ne = ["D=","D-=",")*","):","D:","=\\",":(",":((",")):",":'(", ":┤(", ":'-(",
          ")-':",":-(",")-:",":(","):",":'(",":┤(",")':",":'-(",")-':",":-.",":@",
          "@:",":[",":-[",":{", "}:",":-|","|-:",":<",">:",":-<",":c",":-c",":o",
          "o:",":O",":-O","O-:",":s","s:",":S","S:",";(",");",";@","@;",";s","S;",
          "s;","<.<","=(",")=","=/","\=","=@","@=","°o°","°O°","D-","D:","D;","D=",
          "D8","=s",":s",":C","=C"]#,"=\",':\']
    return ne




def negative_facts_words():
    nfw = ['invadir', 'invasão', 'explodir', 'explosão', 'protesto', 'depredar',
          'arrastao','assalto', 'assassino', 'assassinato', 'sequestro', 
          'sequestrado', 'roubo','corruptos','corrupcao', 'acidente', 'tráfico',
          'drogas', 'drogado', 'greve', 'grevistas', 'paralização', 'terrorismo',
          'terrorista', 'morto', 'morte','passeata','tiroteio','balear', 
          'baleado', 'prender', 'fogo', 'incendio', 'incendiar', 'ataque',  
          'atacado', 'atacar', 'covardemente', 'covarde', 'preso','hack', 
          'hacked', 'hackeado', 'deface','irregular']
    #nfw = ['invadir', 'invasão', 'ataque',  'atacado', 'atacar', 'hack', 
    #      'hacked', 'hackeado', 'deface']
    return nfw

def positive_facts_words():
    pfw = ['vencedor','vencer','premiado','premio','comemorando','comemorar',
           'sucesso','superação','superou','esperança','surpresa','aprovacao',
           'recomendam','recomendar','aprovado','resgate','ajuda']
    return pfw
    
def neutral_facts_words():
    neutral = []
    
    return neutral

