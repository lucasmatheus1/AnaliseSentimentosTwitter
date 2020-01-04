#Módulos
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

dados = pd.read_csv('Base de dados tweets - Caminhao.csv')

# TREINA

#Tweets para treinamento do modelo
textos_treinamento=[
    "Isso não é apenas por conta da Gasolina, é por impostos altos, por preços de água e energia subindo loucamente, por desemprego! isso é por eles, por mim, por você, por todos nós!",
    "Povo comemorando que a 'Greve Continua' . Quero ver uma mãe com seu filho morrendo no hospital por falta de medicação não entregue pelos caminhoneiros reclamar de alguma coisa, já que apoiaram tanto a greve!",
    "Eu entendo e apoio completamente a #Grevedecaminhoneiros mas por favor, deixem os caminhões que estão abastecidos de comida para os animais passarem, eles não merecem passar fome por causa da ganância desses políticos que nem pra ajudar o povo servem.",
    "O protesto tá lindo d+",
    "Os caminhoneiros de Cuiabá não desapontaram a nação. São verdadeiros exemplos.",
    "Parabéns aos caminhoneiros Eles conseguiram marcar e organizar uma greve no Brasil inteiro Eu não consigo nem marcar de sair com meu grupinho de amigos",
    "A greve dos caminhoneiros mostrou como somos dependentes de profissões menosprezadas e esquecidas pela sociedade. Ter um diploma não te faz melhor que ninguém.",
    "A greve dos caminhoneiros está longe de trazer a luz. Mas acaba com muita ideia macabra, como a política de preços do Parente e da Miriam Leitão, porca-voz de qualquer parente do FHC.",
    "O governo que congelou os investimentos em saúde e educação está dizendo ao vivo que está preocupado com as crianças  sem escola e com a saúde da população...",
    "Essa greve dos caminhoneiros nós faz compreender que 'OS CAMINHÕES TEM MOTORES POTENTES PARA TRANSPORTAR UM PAÍS, MAS TAMBÉM TÊM FREIOS BONS PARA PARAR UMA NAÇÃO'.",
    "A GREVE TEM QUE CONTINUAR SIM! BASTA!",
    "Minha única preocupação é com os ANIMAIS INDEFESOS,que estão presos,em alguns locais sem comida,as PESSOAS doentes,que PRECISAM de suporte e material médico no hospital pois podem correr graves riscos!",
    "As forças armadas vão enfrentar os caminhoneiros para saírem das estradas.. GREVE É DIREITO! Está na hora de uma mobilização ainda maior, com todos os seguimentos da sociedade.O governo está achando que tem a força maior, mas essa força é nossa, do povo!",
    "Temer implantando o exército na manifestação Chamando manifestantes de 'minoria' que não deixam os demais trabalharem para o bem da população Temer, nossa vergonha é você",
    "Os caminhoneiros só querem redução no preço dos combustíveis, mas o governo, que era sócio do PT até outro dia, não consegue fazer isso; A greve continua e eu apoio!",
    "Os caras nunca se preocuparam com saúde, educação, segurança, e crianças e agora querem vir pagar de 'Preocupados' Hipócritas.",
    "Essa greve é muito ruim, nos prejudica, nós não temos alimentos, nossa locomoção é prejudicada",
    "O governo tem que acabar com essa greve, estou sendo prejudicado, a greve tem afetado minha família.",
    "Os caminhoneiros não tem o direito de realizar essa greve, a greve é um crime",
    "eu não posso mais estudar devido a essa greve, o governo precisa tomar uma providência",
    "Os alimentos estão acabando, não tem mais comida por causa da greve dos caminhoneiros",
    "Corcordo com ela, mas com essa greve só tenho em mente agora: 1. Quem está pra dar luz a filho e não tem gasolina ou está parado em algum lugar. 2. Quem precisa de sangue ou remédios em postos e hospitais/UTI. 3. Pessoas precisando de ambulância e não tem.",
    "Devem liberar os animais que estão nos caminhões. Pobres bixanos.",
    "A greve dos caminhoneiros mostrou como somos dependentes de profissões menosprezadas e esquecidas pela sociedade. Ter um diploma não te faz melhor que ninguém.",
    "Tenho uma amiga cujo marido está internado no IBCC em tratamento de um câncer. A situação lá já é crítica. Faltam vários artigos, inclusive oxigênio. Estou muito p com essa greve. Canalhas!",
    "Comida do super luna tá acabando , eu super apoio mais já to surtando em não ter comida",
    "A última vez que vi todo mundo contra uma mesma coisa foi em 2013. Foi muito emocionante. Mas se seguiram tempos sombrios, derivados disso. É o único motivo pra eu me incomodar (psicologicamente) com essa mobilização social dessa semana.",
    "E prossigo opinando da mesma forma. Já deu caminhoneiros. Voltem porque todos já sabem o tamanho do problema quando vcs param. Tem gente correndo risco de vida já."
]
#Classificações
classe_treino=[
    "Positivo","Negativo","Neutro","Positivo","Positivo","Positivo","Positivo","Neutro","Positivo","Positivo","Positivo","Neutro",
    "Positivo","Positivo","Positivo","Positivo","Negativo","Negativo","Negativo","Negativo","Negativo","Neutro","Neutro","Positivo",
    "Negativo","Neutro","Neutro","Neutro"
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
arquivo_copia = open('Base de dados tweets - Caminhao copia.csv','w+')
arquivo_copia.write('Nome,Texto,Classificacao,Data e Hora,Aparelho,Qntd. RTs,Qntd. Favs,Localizacao,Verificado\n')

for i in range(len(classifica)):
    arquivo_copia.write(dados["Nome"][i]+','+dados["Texto"][i]+ ','+str(classifica[i])+','+ str(dados["Data e Hora"][i])+','+str(dados["Aparelho"][i])+','+str(dados["Qntd. RTs"][i])+','+str(dados["Qntd. Favs"][i])+','+str(dados["Localizacao"][i])+','+str(dados["Verificado"][i])+'\n')

# FILTRAGEM

dados_copia = pd.read_csv('Base de dados tweets - Caminhao copia.csv')

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
