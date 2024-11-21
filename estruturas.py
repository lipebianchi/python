import random
import time

# PARTE DE CRIAÇÃO DAS FUNÇÕES

def randomArray(t):
    array = []
    for i in range(t):
        n = random.randint(0, 1000000)
        array.append(n)
    return array

def bubble_sort(l):
    t = len(l)

    for i in range(t):
        for j in range(0, t - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

def selection_sort(l):
    t = len(l)
    for i in range(t):
        min_Idx = i
        for j in range(i + 1, t):
            if l[j] < l[min_Idx]:
                min_Idx = j
        l[i], l[min_Idx] = l[min_Idx], l[i]
    return l

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l

def shell_sort(l):
    n = len(l)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = l[i]
            j = i
            while j >= gap and l[j - gap] > temp:
                l[j] = l[j - gap]
                j -= gap
            l[j] = temp
        gap //= 2
    return l

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort(l):
    """Ordena a lista utilizando o algoritmo Merge Sort."""
    if len(l) <= 1:
        return l
    
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    
    return merge(left, right)

def quick_sort(l):
    if len(l) <= 1:
        return l  
    
    pivô = l[-1]
    
    minors = [x for x in l[:-1] if x <= pivô]
    biggers = [x for x in l[:-1] if x > pivô]
    
    return quick_sort(minors) + [pivô] + quick_sort(biggers)

def timeSpend(f, l):
    start_time = time.time()
    f(list(l))
    return time.time() - start_time

def compare(chooses, t):
    methods = {
        1: bubble_sort,
        2: selection_sort,
        3: insertion_sort,
        4: shell_sort,
        5: merge_sort,
        6: quick_sort
    }

    arr = randomArray(t)

    print(f"comparando: {methods[chooses[0]].__name__} com {methods[chooses[1]].__name__}")

    t1 = timeSpend(methods[chooses[0]], arr)
    t2 = timeSpend(methods[chooses[1]], arr)

    print(f"metodo: {methods[chooses[0]].__name__} levou {t1:.6f} segundos")
    print(f"metodo: {methods[chooses[1]].__name__} levou {t2:.6f} segundos")

    if t1 > t2:
        print(f"{methods[chooses[1]].__name__} foi mais rápido")
    elif t1 < t2:
        print(f"{methods[chooses[0]].__name__} foi mais rápido")
    else:
        print("os métodos levaram o mesmo tempo.")

def menu(chooses, count = 0):
    if count == 2:
        t = int(input("Qual tamanho de array você deseja?"))
        return compare(chooses, t)

    print("Escolha qual método deseja comparar: \n1 - Bubble\n2 - Select\n3 - Insertion\n4 - Shell\n5 - Merge\n6 - Quick\n")

    c = int(input())

    chooses.append(c)
    return menu(chooses, count + 1)

# FIM DA CRIAÇÃO DAS FUNÇÕES


# MAIN:

chooses = []
menu(chooses)

# FIM DA MAIN