#Programa que le os logs do servidor e aplica a rede neural
# para determinar se a mensagem salva no log merece atencao
#
# Exemplo de verificacao do arquivo auth.log  
# tail -f /var/log/auth.log | cut -d' ' -f6- | CUDA_VISIBLE_DEVICES=3 python analisador.py
# Rodando no ambiente miniconda
#
import sys
import os
#import pandas
#import keras
#os.system('conda install keras')
from sentence_transformers import SentenceTransformer
from tensorflow import keras

# Carrega a rede neural com parametros salvos
RN=keras.models.load_model('Rede neural salva')

# Loop de leitura do arquivo de logs
while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break

    if not line:
        break

    listline=[line]
    print (type(listline), listline)

    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    sentence_embeddings = model.encode(listline)

#    for sentence, embedding in zip(listline, sentence_embeddings):
#      print("Sentence:", sentence)
#      print("Embedding:", embedding)
#      print("")
#
# Faz a inferencia e mostra o resultado
    previsao = RN.predict(sentence_embeddings, batch_size=384, verbose=0)

    classe = previsao[0,0]
#    classe=0
    print(classe)
    if(classe > 0.5):
        print("Problema - ", classe)
    else:
        print("Normal - ",classe)
