<!-- antes de enviar a versão final, solicitamos que todos os comentários, colocados para orientação ao aluno, sejam removidos do arquivo -->

# Pré-analisador de logs de sistemas computacionais utilizando redes neurais e Sentence Transformer

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
humana imediata caso julgue relevante.

  A partir de um arquivo de registros que foi manualmente rotulado [1] , o programa usa uma rede neural treinada para inferir se determinado registro que
 ocorrer no sistema merecerá ter a atenção dos administradores.
 
 
 [1] Loghub (https://github.com/logpai/loghub)
 
 
---

Matrícula: 192.110.190

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
