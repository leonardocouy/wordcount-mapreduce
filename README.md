# Wordcount using MapReduce in Python
------

**Este trabalho faz parte como avaliação parcial da matéria Soluções para processamento paralelo e distribuído de dados**

**Aluno:** Leonardo Flores

**PUC MINAS**

## Como rodar?

1. Clone o repositório
2. Vá até o diretório e rode o seguinte comando:
    `python server.py`
    1. Caso queira que mostre o resultado de autores específicos digite:
    `python server.py --authors "nome do autor 1 completo" "nome do autor 2 completo"`
        1. Exemplo: `python server.py --authors "Grzegorz Rozenberg" "Philip S. Yu"`
    
3. Agora, abra outra aba e excute:
    `python2 mincemeat.py -p changeme 127.0.0.1`
4. Espere rodar o MapReduce.
5. Veja o resultado em `authors_most_frequently_words.csv` e pesquise pelo autor desejado.


## SOLUÇÃO DO EXERCÍCIO

Result:
```
Grzegorz Rozenberg: 

- systems: 10 vezes
- grammars: 9 vezes

---
Philip S. Yu:

- web: 7 vezes
- data: 7 vezes
```

## Feito por

**LEONARDO FLORES**