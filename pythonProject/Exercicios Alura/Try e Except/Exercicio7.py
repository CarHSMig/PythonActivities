def calcular_media(lista):
    try:
        media = sum(lista) / len(lista)
        return media
    except ZeroDivisionError:
        print("A lista está vazia.")
        return None

lista_valores = [10, 20, 30, 40, 50]
media = calcular_media(lista_valores)
if media is not None:
    print("A média dos valores na lista é:", media)