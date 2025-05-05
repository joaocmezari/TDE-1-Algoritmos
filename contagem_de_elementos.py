
#Escreva o código em Python que:
#1. Receba os dois conjuntos de funcionalidades (versao1 e versao2).
#. Calcule e exiba o número de funcionalidades exclusivas de cada versão e o número
#de funcionalidades compartilhadas.
#Dica: Use operações de conjunto em Python:
#● Diferença (-): Para encontrar funcionalidades exclusivas de uma versão.
#● Interseção (&): Para encontrar funcionalidades compartilhadas entre as duas
#versões.
#Use a função len() para contar o número de funcionalidades.


A = {"login", "registro", "perfil", "mensagens", "notificações",
"relatórios"}
B = {"login", "registro", "perfil", "pagamentos", "notificações", "ajuda",
"relatórios", "backup"}
# Contagem dos elementos
apenas_A = len(A - B)
apenas_B = len(B - A)
intersecção = len(A & B)
# Exibindo os resultados
print("Apenas A:", apenas_A, "elementos")
print("Apenas B:", apenas_B, "elementos")
print("Intersecção:", intersecção, "elementos")