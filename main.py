#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from file_manager import *
from fcfs import *
from sstf import *
from elevador import *

def main():
    # Recebe o nome do arquivo do console
    filename = sys.argv[-1]

    # Inicializa o gerenciador de arquivos
    fm = FileManager()
    # Le o arquivo e retorna em forma de lista
    inputs = fm.read_input(filename)
    # Retira a quantidade de setores da lista e armazena na variavel sectors
    sectors = inputs.pop(0)
    # Retira a posicao inicial do cilidro e armazena na variavel initial_sector
    initial_sector = inputs.pop(0)

    fcfs = FCFS(sectors, initial_sector)

    sstf = SSTF(sectors, initial_sector)

    elevador = Elevador(sectors, initial_sector)
    
    elevador.execute(inputs)



if __name__ == '__main__':
    main()
