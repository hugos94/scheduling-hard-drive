#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class SSTF(object):
    '''  Algoritmo de escalonamento do braco do disco que utiliza a politica "Shortest Seek Time First" para atender as requisicoes. '''


    def execute(self, sectors , initial_sector, inputs):
        ''' Metodo que executa o algoritmo do elevador. '''

        current_position = initial_sector # Inicializa o setor atual como o setor inicial

        sum_distance = 0

        requisitions = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        requisitions.sort() # Ordena a lista de entradas

        while requisitions: # Iteracao na lista de entrada até a lista ficar vazia

            best_choice = -1 # Inicializa a variavel best_choice com -1
            best_distance = sectors+1 # Inicializa a variavel best_distance com a maior distacia permitida + 1

            for value in requisitions: # Percorre a lista de entrada
                distance = abs(current_position - value) # Calcula a distancia da posicao atual para a proxima
                if (distance < best_distance): # Se a distancia for menor que a melhor distancia
                    best_distance = distance # Armazena a melhor distancia
                    best_choice = value # Armazena a posicao do setor

            current_position = best_choice # Posicao atual recebe a melhor escolha
            requisitions.remove(best_choice) # A melhor escolha e removida da lista de entradas
            sum_distance += best_distance # A melhor distancia e somada as outras melhores distancias

        print("SSTF " + str(sum_distance)) # Imprime o resultado final
