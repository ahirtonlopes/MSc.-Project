# -*- coding: utf-8 -*-
"""
"""
__author__ = "Rodrigo Pasti"
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
import pickle
import text_processing as tp
#import tweets_set1
#import tweets_set2

"""
lê uma lista de tweets contida em arquivo
"""


def read_tweets():  
    #db = TwitterBNSC()
   # tweets = list(db.get_tweets(pagination=35000, page=1))
    tweetsUsers = {}   
    mongo = Mongo('GENDER')
    query = { '$group' : { '_id' : '$user', 'tweets': { '$push': {'text':"$text", 'gender':"$gender"} } }}
    r = mongo.db['labeled'].aggregate([query])['result']
    for c in r:
        tweetsUsers[c['_id']] = c['tweets']
    return tweetsUsers
    
    
def read_tweets2(database):  
    #db = TwitterBNSC()
   # tweets = list(db.get_tweets(pagination=35000, page=1))
    tweetsUsers = {}   
    mongo = Mongo(database)
    #'author_detection_twitter_message'
    
    #query = { '$group' : { '_id' : '$user', 'tweets': { '$push': {'text':"$text"} } }}
    query = [{ '$match': { 'shared':{'$eq':None} } }, { '$group' : {'_id' : '$profile', 'tweets': { '$push': {'text':'$text'} } } }]
    r = mongo.db['author_detection_twitter_message'].aggregate(query)['result']    
       
   # all_tweets = []
    users = []
    tweetsUsers = {}
    threshold = 1
    for content in r:
       id = content['_id']
       tweets = content['tweets']       
       if len(tweets) > threshold:
           profile = mongo.db['author_detection_twitter_message'].find_one({'id':id})           
           if profile['versions']:
               name = profile['versions'][0]['screen_name']              
               profile = {'nome':name, 'tweets':tweets}
               tweetsUsers[name] = tweets
               users.append(name)
               #all_tweets.append(profile)
    
    return [tweetsUsers,users]
      
   # print r
#    users = []
#    for c in r:
#        tweetsUsers[c['_id']] = c['tweets']
#        users.append(c['_id'])
#       
#    return [tweetsUsers,users]
    
        
#    BASES ANTIGAS:
#    tweetsListR = []
#    for tweet in tweets:
#        tweetsListR.append(tweet['text'].decode('utf-8'))
    
    #tweetsListR = tweets_set1.set1()
    #tweetsListR = tweets_set2.set2()    
    #Eliminar as quebras de linhas (\n)
   # nTweets = len(tweets) 
   # nTweets = 3000
   # for iTweet in range(0,nTweets):
    #    print tweets[iTweet]
     #   raw_input('-----------------------------------------------------------------')
       # tweetsList.append(re.sub("\n"," ", tweetsListR[iTweet]))        
    
    


#Abre um arquivo texto e coloca 
def textToList1(file_name):
    file = open(file_name, 'r')
    wordsList = []
    for line in file.readlines():        
        line = line[0:line.find('/')]
        #print line
        wordsList.append(line)
    file.close()
    return wordsList
    
def textToList2(file_name):
    file = open(file_name, 'r')
    documents = []
    for line in file.readlines():        
        documents.append(line)
    file.close()
    return documents
    
#Salva um objeto ou estrutura em um arquivo (Mudar caminho especificado)
def save_object(obj, objName, objType,fileNamePath):
    if fileNamePath is None:
        file = open('C:\\Users\\Ahirton\\Desktop\\Python\OutputFiles\\' + objName + '.' + objType, 'w+')
    else:
        file = open(fileNamePath + objName + '.' + objType, 'w+')
    pickle.dump(obj, file)
    file.close()
    
#Carrega um objeto de um arquivo (Mudar caminho especificado)
def load_object(objName,objType,fileNamePath):
    if fileNamePath is None:
        file = open('C:\\Users\\Ahirton\\Desktop\\Python\OutputFiles\\' + objName + '.' + objType, 'r') 
    else:
        file = open(fileNamePath + objName + '.' + objType, 'r') 
    obj = pickle.load(file)    
    file.close()
    return obj
    
