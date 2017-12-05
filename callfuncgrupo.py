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
'''
-----------------------------------------------------------------------------------------------------------------------
LEITURA DE TWEETS CONTIDOS EM ARQUIVO CSV E EXTRACAO DE META-ATRIBUTOS TEXTUAIS
-----------------------------------------------------------------------------------------------------------------------
"""
'''
import text_processing as tp

'''
-----------------------------------------------------------------------------------------------------------------------
(1) TESTE DO PROCESSADOR TEXTUAL
-----------------------------------------------------------------------------------------------------------------------
'''
#print ("oi")
#docsTokenized = tp.tagging(['Governo de SP vai pagar R$ 25 mil a quem denunciou suspeito de matar ambulante no Metro. Secretaria de Seguranca Publica fixou valor nesta quarta (18) no Diario Oficial.'])
#print(docsTokenized)

docsToken = tp.tagging(["Espero que curtam o meu trabalho"])
#print(docsToken)



