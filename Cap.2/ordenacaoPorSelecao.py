def buscaMenor(arr):
    menor = arr[0]
    indiceMenor = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            indiceMenor = i
    return indiceMenor

def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        indiceMenor = buscaMenor(arr)
        novoArr.append(arr.pop(indiceMenor))
    return novoArr

print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))