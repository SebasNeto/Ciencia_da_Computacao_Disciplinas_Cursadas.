def count_sort(lista): #derfindo a função cout sort
    n = len(lista) # lê os elementos dentro da lista
    for c in range(n): #verifica se há um menor elemento na lista onde c assume esse valor
        minimo = c
        for j in range(c,n): #verifica se o próximo valor é menor que os restantes dos elementos, em afirmativo j assume o valor de minimo
            if lista[j] < lista[minimo]:
                minimo = j
        if lista[c] > lista[minimo]: #criação de uma variavel auxiliar para armazenar o maior elemento e não prejudicar o metodo
            auxiliar = lista[c]
            lista[c] = lista[minimo]
            lista[minimo] = auxiliar
lista = [1,4,6,7,3,43,0]
count_sort(lista) #chamando a função definida 
print(lista) #lista ordenada
