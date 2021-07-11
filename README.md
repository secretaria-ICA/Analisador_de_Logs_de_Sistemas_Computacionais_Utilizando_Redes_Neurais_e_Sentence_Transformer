<!-- antes de enviar a versão final, solicitamos que todos os comentários, colocados para orientação ao aluno, sejam removidos do arquivo -->

# Analisador de logs de sistemas computacionais utilizando redes neurais e Sentence Transformer

#### Alun(o/a): [Luís Fernando V Gomes](https://github.com/lfvgomes).
#### Orientadores:[Felipe Borges](https://github.com/FelipeBorgesC)  e [Manoela Kohler](https://github.com/manoelakohler).
<!-- #### Co-orientador(/a/es/as): [Felipe Borges] (https://github.com/link_do_github). <! -- caso não aplicável, remover esta linha -->

---

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".


---

### Resumo

   Sistemas computacionais de todos os tipos geram em tempo real uma quantidade enorme de registros (logs) com informações sobre as suas atividades,
funcionamento dos seus componentes (temperatura, dispositivos de memória interna, dispositivos de entrada e saída, etc.) ou eventos provocados por 
ações externas (tráfego de rede, solicitações de serviços, etc.). Em funcionamento normal, a grande maioria destes registros não requer cuidados por 
parte dos administradores do sistema, mesmo que o registro seja para informar algum tipo de erro. Por exemplo, se um usuário errar a sua senha uma 
vez, isto não deve ser motivo de intervenção. Por estes e outros motivos, é impraticável ter um ser humano com a incumbência de ficar analisando estes 
registros, que podem chegar em dezenas a cada segundo.

   O objetivo deste trabalho é gerar uma ferramenta que seja capaz de analisar estes registros em um tempo bastante curto e somente recomendar a inspeção
humana imediata caso julgue relevante. É composta por duas partes: a primeira pega um arquivo de logs rotulado e gera a rede neural treinada; a segunda usa 
a rede treinada para analisar os logs.

  A partir de um arquivo de registros para o cluster Thunderbird que foi manualmente rotulado [1] , o programa usa uma rede neural treinada para inferir se determinado registro que ocorrer no sistema merecerá ter a atenção dos administradores.
  
   Foram escolhidos 1000 registros sem anomalias e 1022 com anomalias, que, combinados, geraram o arquivo Thunderbird_1000.log. Este foi usado para treinamento
e teste da rede neural.

### Aplicabilidade
   Usando a rede treinada, um programa analisador varre o arquivo de logs e gera uma saída de acordo com a inferência da classificação da linha do arquivo
   de logs. Se for relevante, o programa pode enviar a linha e um alerta, por exemplo, através de email para o administrador do sistema.
   
   São sugeridas duas formas de usar o programa:
   
   Análise em tempo real:
      
   A chamada no formato
         
         tail -n1 -f /var/log/arquivo.log | cut -d' ' -f6- | python analisador.py
   lê continuamente o arquivo de logs e pode gerar um alerta caso detecte uma classe de erro, anexado dos dados da mensagem e informando os administradores do sistema.
      Esta opção só é possível se o servidor a ser analisado tiver velocidade suficiente para processar as linhas de logs em tempo real.
      
   Análise do passado:
   
   A chamada no formato
      
      
         tail -1000 /var/log/arquivo.log | cut -d' ' -f6- | python analisador.py
   lê as últimas 1000 linhas do arquivo de log e pode gerar o mesmo tipo de alerta, só que sob demanda do administrador do sistema,
        
 
 
 
 
 [1] Loghub (https://github.com/logpai/loghub)
 
 
---

Matrícula: 192.110.190

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
