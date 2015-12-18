#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class FCFS(object):
    '''  Algoritmo de escalonamento do braco do disco que utiliza a politica "First Come, First Serve" para atender as requisicoes. '''

    def __init__(self, sectors, initial_sector):
        ''' Inicializa o algoritmo FCFS com a quantidade de setores e o setor inicial. '''

        self.sectors = sectors
        self.initial_sector = initial_sector


    def execute(self, inputs):
        ''' Metodo que executa o algoritmo de escalonamento com a politica "First Come, First Serve". '''

        current_position = self.initial_sector # Inicializa o setor atual como o setor inicial

        sum_distance = 0

        self.inputs = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        for sector in self.inputs: # Percorre as entradas
            sum_distance += abs(current_position - sector) # Realiza o somatorio da distancia da entrada
            current_position = sector # Modifica o setor atual para o setor escolhido

        print("FCFS " + str(sum_distance)) # Imprime o resultado final
