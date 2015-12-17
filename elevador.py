#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class Elevador(object):
    '''  Algoritmo de escalonamento do braco do disco que simula um elevador para atender as requisicoes. '''

    def __init__(self, sectors, initial_sector):
        ''' Inicializa o algoritmo do elevador com a quantidade de setores e o setor inicial. '''
        self.sectors = sectors
        self.initial_sector = initial_sector


    def execute(self, inputs):
        ''' Metodo que executa o algoritmo do elevador. '''

        current_position = self.initial_sector # Inicializa o setor atual como o setor inicial

        sum_distance = 0

        inputs.sort() # Ordena a lista de entradas
        inputs_lower = [] # Cria uma lista para receber os elementos menores que o setor inicial

        self.inputs = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        for value in self.inputs: # Percorre a lista de setores para fazer o somatorio das distancias dos setores superiores ao inicial
            if (value > self.initial_sector): # Verifica se a o setor atual e menor que o setor inicial
                sum_distance += abs(current_position - value) # Faz o somatorio da distancia
                current_position = value # Setor inicial torna-se o setor atual
            else:
                inputs_lower.append(value) # Armazena os setores menores que o atual em uma lista

        inputs_lower.reverse() # Reverte a lista de valores menores que o setor inicial

        for value in inputs_lower: # Percorre a lista de setores menores que o setor inicial
            sum_distance += abs(current_position - value) # Faz o somatorio dos setores
            current_position = value # Setor atual torna-se o proximo setor

        print("ELEVADOR " + str(sum_distance)) # Imprime o resultado final
