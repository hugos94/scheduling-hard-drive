#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path

class FileManager(object):
    """FileManager e a classe responsavel por ler e escrever em arquivos"""

    def read_input(self, input_file):
        """ Retorna o conteudo do arquivo de entrada na forma de lista. """
        if(os.path.exists(input_file) and os.path.isfile(input_file)):
            try:
                # Le o arquivo e armazena em uma lista, usando a separacao pelo fim de linha
                data = [line.strip() for line in open(input_file, 'r')]
                return data
            except Exception as e:
                print("Nao foi possivel abrir o arquivo: %s" % input_file)
                raise e
