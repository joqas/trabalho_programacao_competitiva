# trabalho_programacao_competitiva
questões do trabalho de programação competitiva II
<img width="893" height="677" alt="image" src="https://github.com/user-attachments/assets/3f0d0af0-1fc4-49eb-809f-7df5189fa7df" />
Programação Competitiva II
Questão 1: O problema pede para identificar se vários números grandes (até 10¹²) são T-Primos. Tendo um limite estrito de 2 segundos de processamento. Ao analisar a forma como os números funcionam. Um número só tem um número ímpar de divisores se for um quadrado perfeito, para que o número tenha 3 divisores, ele obrigatoriamente tem que ser o quadrado de um número primo. Então, seria necessário checar os divisores de cada número com uma estrutura de repetição, porém, com essa força bruta, o (x) chega a 10¹² e o número de consultas (n) chega a 5², faríamos cerca de 10¹¹ operações, ultrapassando assim o limite de 2 segundos.
	Para isso, foi utilizado conceitos pré-computacionais com o algoritmo do Crivo de Eratóstenes (identificar os números primos, como uma espécie de “peneira”). Como o maior número possível é 10¹²,  sua raíz máxima é 10^6. Então basta criar um array booleano para identificar todos os números primos até 10^6 de uma vez. Com isso, o programa faz três checagens de tempo constante. 
Calcula a raíz quadrada de um número
Checa se a raiz multiplicada por ela mesma resulta no número original, garantindo assim que é um quadrado perfeito
Verifica no Crivo pré-computado se essa raíz é um número primo 
É correto afirmar que é matematicamente sólido para os limites de dados visto que toda a leitura do código ficou dentro do Crivo para ler e responder às consultas, rodando em uma fração de segundos.
