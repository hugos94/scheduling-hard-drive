#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class FCFS(object):
    '''  Algoritmo de escalonamento do braco do disco que utiliza a politica "First Come, First Serve" para atender as requisicoes. '''

    def __init__(self, sectors, initial_sector):
        ''' Inicializa o algoritmo do elevador com a quantidade de setores e o setor inicial. '''

        self.sectors = sectors
        self.initial_sector = initial_sector


    def execute(self, inputs):
        ''' Metodo que executa o algoritmo de escalonamento com a politica "First Come, First Serve". '''

        current_position = self.initial_sector

        sum_distance = 0

        self.inputs = copy.deepcopy(inputs)

        for sector in self.inputs:
            sum_distance += abs(current_position - sector)
            current_position = sector

        print("FCFS " + str(sum_distance))
