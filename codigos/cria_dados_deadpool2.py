#Importando módulos
import tweepy
import re
import datetime
from tweepy import OAuthHandler

#Faz o processamento das palavras, removendo sinais de pontuação, links e quebras de linha.
def Processamento(frase):
    frase = re.sub(r"http\S+", "", frase).replace("!","").replace("?","").replace(",","").replace(".","").replace("#","").replace("-","").replace("\n"," ").replace("...","").replace(":","").replace(";","").lower()
    return frase

#Verifica se o usuário que postou o tweet é verificado ou não.
def eh_verificado(verificado):
    if verificado==False:
        return "Não"
    else:
        return "Sim"

# Autenticações
consumer_key = '3KeglA7No5W1uW6jC1mZ3otsp'
consumer_secret = 'Ki00sV1Vu090ipG4G0V6gXigEeAgTI3Q4TzTt31XxtPL1oYyFF'
access_token = '510599982-62P1ixOGiuZfXX4mwQlnNROIFa09O09aFI99BOH4'
access_secret = '2niZuKO0KQK9YnWWTHvVNmovW5j6UDJk1f52uWGEmK1va'
# Configurações das Autenticações
autorisacao = OAuthHandler(consumer_key, consumer_secret)
autorisacao.set_access_token(access_token, access_secret)
api = tweepy.API(autorisacao)

#Palavra chave
palavra = "Deadpool 2 -filter:retweets"
#Quantidade de tweets
qntd_tweets = 2500
tweets = [status for status in tweepy.Cursor(api.search, q=palavra,lang="pt-br",since="2018-04-26").items(qntd_tweets)]
#Variáveis zeradas
cont, cont_irrelevantes= 0, 0
escreve_texto= ""
#Abrindo arquivo ou criando caso não exista "Base de dados tweets" e escrevendo no mesmo
arquivo = open('Base de dados tweets - Caminhao.csv','w+')
arquivo.write('Nome,Texto,Data e Hora,Aparelho,Qntd. RTs,Qntd. Favs,Localizacao,Verificado\n')

#Percorrendo os tweets encontrados
for tweet in tweets:
    texto=Processamento(tweet.text)
    frase=texto
    texto=texto.split()
    #Processamento para saber se o tweet é relevante ou não.
    if texto[0]== "gostei" and texto[1]== "de" and texto[2]== "um" and texto[3]== "vídeo" and texto[4]== "@youtube" or texto[0][0]== "@" or texto[-1]== "@youtube":
        #Contando tweets irrelevantes
        cont_irrelevantes+=1
        continue
    # Informações para a base de dados
    nome = "@" + tweet.user.screen_name
    data = (tweet.created_at - (datetime.timedelta(hours=3))).strftime('%d/%m/%Y %H:%M:%S')
    aparelho = Processamento(tweet.source)
    qntd_rt = tweet.retweet_count
    qntd_fav = tweet.favorite_count
    localizacao = Processamento(tweet.user.location)
    verificado=eh_verificado(tweet.user.verified)
    print(nome,frase,data,aparelho,qntd_rt,qntd_fav,localizacao,verificado)
    #Contando tweets normais
    cont+=1
    #Escrevendo informações no arquivo
    arquivo.write(nome+','+frase+ ','+data+','+ aparelho+','+str(qntd_rt)+','+str(qntd_fav)+','+localizacao+','+verificado+'\n')

print('\nTweets Normais: ' + str(cont) +' ,Tweets Irrelevantes: ' + str(cont_irrelevantes))
