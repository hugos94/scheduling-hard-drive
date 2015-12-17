#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

        for sector in inputs:
            if (sector > current_position):
                sum_distance += sector - current_position
            else:
                sum_distance += current_position - sector

            current_position = sector

        print("FCFS " + str(sum_distance))
