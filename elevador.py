#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Elevador(object):
    '''  Algoritmo de escalonamento do braco do disco que simula um elevador para atender as requisicoes. '''

    def __init__(self, sectors, initial_sector):
        self.sectors = sectors
        self.initial_sector = initial_sector
        self.current_position = initial_sector
        self.sum_distance = 0

    def execute(self, inputs):
        ''' Metodo que executa o algoritmo do elevador. '''

        inputs.sort() # Ordena a lista de entradas
        inputs_lower = [] # Cria uma lista para receber os elementos menores que o setor inicial

        for value in inputs: # Percorre a lista de setores para fazer o somatorio das distancias dos setores superiores ao inicial
            if (value > self.initial_sector): # Verifica se a o setor atual e menor que o setor inicial
                self.sum_distance += (value - self.current_position) # Faz o somatorio da distancia
                self.current_position = value # Setor inicial torna-se o setor atual
            else:
                inputs_lower.append(value) # Armazena os setores menores que o atual em uma lista

        inputs_lower.reverse() # Reverte a lista de valores menores que o setor inicial

        for value in inputs_lower: # Percorre a lista de setores menores que o setor inicial
            self.sum_distance += (self.current_position - value) # Faz o somatorio dos setores
            self.current_position = value

        print("ELEVADOR " + str(self.sum_distance))
