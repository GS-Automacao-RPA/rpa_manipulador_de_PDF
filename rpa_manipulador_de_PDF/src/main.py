from src.utils.check_update import check_update
from src.controller.controller import run
from src.utils.constants import VERSION,NOME
import ctypes
import os
import sys






if __name__ == '__main__':
    try:
        print(NOME) # mostra o nome da automação
        print(VERSION) # mostra a versão da automação
        check_update(VERSION) # verifica a se há algum update dessa automação
        run()
    except Exception as e:
        print(e)
        input()
