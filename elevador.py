#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Elevador(object):
    ''' '''

    def __init__(self, sectors, initial_sector):
        self.sectors = sectors
        self.initial_sector = initial_sector
        self.sum_distance = 0

    def execute(self, inputs):
        # Ordena a lista de entradas
        inputs.sort()
        position = 0
        while (self.initial_sector >= inputs[position]):
            print(position)
            print(str(self.initial_sector) + " > " + str(inputs[position]))
            position+=1
