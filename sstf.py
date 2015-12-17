#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class SSTF(object):
    '''  Algoritmo de escalonamento do braco do disco que utiliza a politica "Shortest Seek Time First" para atender as requisicoes. '''

    def __init__(self, sectors, initial_sector):
        ''' Inicializa o algoritmo SSTF com a quantidade de setores e o setor inicial. '''
        self.sectors = sectors
        self.initial_sector = initial_sector


    def execute(self, inputs):
        ''' Metodo que executa o algoritmo do elevador. '''

        current_position = self.initial_sector

        sum_distance = 0

        self.inputs = copy.deepcopy(inputs)

        self.inputs.sort() # Ordena a lista de entradas

        while self.inputs:

            best_choice = -1
            best_distance = self.sectors+1

            for value in self.inputs:
                distance = abs(current_position - value)
                if (distance < best_distance):
                    best_distance = distance
                    best_choice = value

            current_position = best_choice
            self.inputs.remove(best_choice)
            sum_distance += best_distance

        print("SSTF " + str(sum_distance))
