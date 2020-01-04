#Módulos
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

dados = pd.read_csv('Base de dados tweets - Deadpool.csv')

# TREINA

#Tweets para treinamento do modelo
textos_treinamento=[
    "vo ir ver deadpool hoje uhu",
    "deadpool eh mto bom vsf",
    "deadpool 2 eh muito bom pqp",
    "Mano nem gosto muito de filme de heróis mas To afim de ver Deadpool de novo",
    "aAaaaaaAAAAAAAAAAAAAA EU QUERO ASSISTIR DEADPOOL QUE ODIOOOOOOOOooooooooooo",
    "Muito feliz de ter visto deadpool 2",
    "só to com raiva dessas crianças dando spoiler sobre deadpool 2 por isso q saporra tem q ficar 18 anos msm",
    "Deadpool filmão da porra cheio de referencia muita satira podem assistir vale muito",
    "Deadpool 18 anos foi ridículo a censura aqui agr é tipo Rússia",
    "Não achei o Deadpool 2 nada de especial Ri muito mais com o 1",
    "Deadpool 2 é muito bom",
    "GENTE DEADPOOL 2 QUE FILMÃO",
    "Exatamente tudo o que eu achei de Deadpool 2  Mei sem graça o DEADPOOL 2 não",
    "Eu não vi o Stan Lee em Deadpool 2 e esse foi o único ponto q fiquei triste nesse filme que é MARAVILHOSAMENTE DIVERTIDO PRA CACETE",
    "Ah esqueci de falar ontem Deadpool 2 é muuuuuito bom Mesmo nível do 1 não decepcionou",
    "O Filme do deadpool foi horrível",
    "Será que eles poderiam devolver meu dinheiro que gastei pra assistir deadpool 2",
    "Não gostei do filme do deadpool, pois a quantidade de piadas é muito excessivas",
    "deadpool é um dos melhores filmes da marvel, na minha opinião",
    "Vi Deadpool 2 e a conclusão foi de que perdi meu tempo",
    "Quero ir no cinema assistir deadpool 2",
    "fui na pre estreia de deadpool mas queria mesmo uma de han solo",
    "Todo mundo falando de Deadpool e eu aqui só pensando em Guerra Infinita",
    "acabei de voltar do cinema fui ver deadpool",
    "Não fui ver DeadPool",
    "eu disse que ia dormir e estou aqui pensando se vou ou não assistir Deadpool",
    "n pode ser real que deadpool saiu dos cinemas e eu não fui ver",
    "O pior é que Deadpool nem foi tão exagerado assim pra proibirem pra menores de 18",
    "eu gostei mais ou menos de deadpool tem umas piadas que tão muito pesadas pro meu gosto",
    "Queria ter ido ver deadpool hoje mas fiquei com preguiça e upei uns 5 niveis",
    "Assisti Deadpool 2, é OK só",
    "Nunca vi nenhum deadpool"
]
#Classificações
classe_treino=[
    "Positivo","Positivo","Positivo","Positivo","Negativo","Positivo","Negativo","Positivo",
    "Negativo","Negativo","Positivo","Positivo","Negativo","Positivo","Positivo","Negativo",
    "Negativo","Negativo","Positivo","Negativo","Neutro","Neutro","Neutro","Neutro","Neutro",
    "Neutro","Neutro","Neutro","Negativo","Neutro","Neutro","Neutro"
]

#Treinando naive bayes e cria modelo para classificar
vectorizer = CountVectorizer(ngram_range=(1,2))
freq_tweets = vectorizer.fit_transform(textos_treinamento)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classe_treino)

# RECEBE TWEETS PARA SEREM CLASSIFICADOS

#Recebe coluna "Texto" que consta os tweets 
testes = dados['Texto'].values

#variavel "classifica" recebe classificação dos tweets da variavel testes
freq_testes = vectorizer.transform(testes)
classifica = modelo.predict(freq_testes)
print(classifica)

cont_pos, cont_neg, cont_neu = 0,0,0

# Conta positivos, negativos e neutros
'''
for i in range(len(classifica)):
    if classifica[i] == 'Positivo':
        cont_pos+=1
    elif classifica[i] == 'Negativo':
        cont_neg+=1
    elif classifica[i] == 'Neutro':
        cont_neu+=1
'''

#Calculo porcentagem
'''
total = cont_pos+cont_neg+cont_neu
print (cont_pos,cont_neg,cont_neu)
'''
#Imprime
'''
print ('Porcentagem pos.: {:.2f} %'.format((cont_pos/total)*100))
print ('Porcentagem neg.: {:.2f} %'.format((cont_neg/total)*100))
print ('Porcentagem neu.: {:.2f} %'.format((cont_neu/total)*100))
'''
# CRIA ARQUIVO CÓPIA

#Cria arquivo copia já classificado pelo modelo criado acima
arquivo_copia = open('Base de dados tweets - Deadpool copia.csv','w+')
arquivo_copia.write('Nome,Texto,Classificacao,Data e Hora,Aparelho,Qntd. RTs,Qntd. Favs,Localizacao,Verificado\n')

for i in range(len(classifica)):
    arquivo_copia.write(dados["Nome"][i]+','+dados["Texto"][i]+ ','+str(classifica[i])+','+ str(dados["Data e Hora"][i])+','+str(dados["Aparelho"][i])+','+str(dados["Qntd. RTs"][i])+','+str(dados["Qntd. Favs"][i])+','+str(dados["Localizacao"][i])+','+str(dados["Verificado"][i])+'\n')

# FILTRAGEM

dados_copia = pd.read_csv('Base de dados tweets - Deadpool copia.csv')

#Informa como resultado as categorias da coluna e valores
print (dados_copia['Classificacao'].value_counts())

#print (dados_copia[dados_copia['Classificacao']== 'Negativa'])

#Imprime os tweets mais retweetados
'''
lis_rts = [12, 14, 14, 15, 17, 17, 19]
for i in range(len(lis_rts)):
    print (dados_copia[dados_copia['Qntd. RTs'] == lis_rts[i]])
'''
'''
print (dados_copia[dados_copia['Qntd. RTs'] == 143])
print (dados_copia[dados_copia['Qntd. RTs'] == 19])
'''

#Ordena lista de retweets e imprimi os maiores 
'''
rts_ord = sorted(dados_copia['Qntd. RTs'].values)
print (rts_ord)
print (rts_ord[-1])
print (rts_ord[-2])
print (rts_ord[-3])
'''

''' 
CASO QUEIRA FILTRAR OUTRAS COLUNAS COMO "Localizacao" BASTA FAZER: 

dados_copia['Localizazao'], ...

'''
