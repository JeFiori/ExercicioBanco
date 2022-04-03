import time

def abrir_arquivo():
    try:
        arquivo = open('arquivo_nao_existe.txt')
        return True
    except Exception as erro:
        print('aconteceu algum erro: ',erro)
        return False

while not abrir_arquivo():
    print('tentando abrir')
    time.sleep(5)


