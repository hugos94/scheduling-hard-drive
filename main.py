#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from file_manager import *
from fcfs import *
from sstf import *
from elevador import *


def main():

    filename = sys.argv[-1] # Recebe o nome do arquivo do console

    if(filename == sys.argv[0]): # Verifica se algum arquivo foi recebido
        print("Arquivo não informado!")

    else:
        fm = FileManager() # Inicializa o gerenciador de arquivos

        inputs = fm.read_input(filename) # Le o arquivo e retorna em forma de lista

        sectors = inputs.pop(0) # Retira a quantidade de setores da lista e armazena na variavel sectors

        initial_sector = inputs.pop(0) # Retira a posicao inicial do cilidro e armazena na variavel initial_sector

        fcfs = FCFS() # Inicializa o algoritmo FCFS
        fcfs.execute(sectors, initial_sector, inputs) # Executa o algoritmo FCFS

        sstf = SSTF() # Inicializa o algoritmo SSTF
        sstf.execute(sectors, initial_sector, inputs) # Executa o algoritmo SSTF

        elevador = Elevador() # Inicializa o algoritmo Elevador
        elevador.execute(sectors, initial_sector, inputs) # Executa o algoritmo Elevador


if __name__ == '__main__':
    main()
