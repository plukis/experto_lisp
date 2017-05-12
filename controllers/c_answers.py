# -*- coding: utf-8 -*-
import os
import hy
from models import test
#from  pyswip.prolog import Prolog

class Answers:
    def __init__(self):
        self._list_answer = []
        self._limit_questions = 0
        self._root = ''

        # Files,NOTA !!!!! cambiar las rutas de los archivos, si es necesario ....  !!!! 
        self.__my_file = ''
        self.__pas_path = '/models/pas.txt'
        self.__esquizoide_path = '/models/esquizoide.txt'
        self.__emocional_path = '/models/emocional.txt'
        self.__sociopata_path = '/models/sociopata.txt'
        self.__toc_path = '/models/toc.txt'
        self.__estable_path = '/models/estable.txt'
        self.__default_path = '/models/default.txt'
        # direccion donde se guardara el archivo resultante
        self.__last_path = '/models/result.txt'

        # totales de percepcion, comprension y regulacion
        self._total_percepcion = 0
        self._total_comprension = 0
        self._total_regulacion = 0

        # Resultados primera face
        self.__nivel_percepcion = ''
        self.__nivel_comprension = ''
        self.__nivel_regulacion = ''
        # Resultado de segunda face, posible trastorno
        self.__your_desorder = ''

        # resultados en texto de la segunda face
        self.__text_percepcion = ''
        self.__text_comprension = ''
        self.__text_regulacion = ''
        self.__text_estado = ''
        self.__estado = ''

    def _solve_total_percepcion(self):
        total = 0
        for i in range(1, 9):
            acum = total
            total = acum + int(self._list_answer[i])
        self._total_percepcion = total

    def _solve_total_comprension(self):
        total = 0
        for i in range(9, 17):
            acum = total
            total = acum + int(self._list_answer[i])
        self._total_comprension = total

    def _solve_total_regulacion(self):
        total = 0
        for i in range(16, 25):
            acum = total
            total = acum + int(self._list_answer[i])
        self._total_regulacion = total

    def _result_percepcion(self):
        # chequeo en lisp de la percepcion, crear globales antes
        test.crear_globales()
        self.__nivel_percepcion = test.percepcion(self._total_percepcion)

    def _result_comprension(self):
        # chequeo en lisp de la comprension
        self.__nivel_comprension = test.comprension(self._total_comprension)

    def _result_regulacion(self):
        # chequeo en lisp de la regulacion
        self.__nivel_regulacion = test.regulacion(self._total_regulacion)

    def _get_type_desorder(self):
        resultado = ''
        percepcion = self.__nivel_percepcion
        comprension = self.__nivel_comprension
        regulacion = self.__nivel_regulacion
        resultado = test.verifica_primero(percepcion, comprension, regulacion)
        self.__your_desorder = resultado

    def impresion_final(self):
        print '\nnivel de tu percepcion emocional ...'
        print self.__nivel_percepcion
        print '\nnivel de tu comprension emocional ...'
        print self.__nivel_comprension
        print '\nnivel de tu regulacion emocional ...'
        print self.__nivel_regulacion
        print '\nposible tendencia de transtorno ...'
        print self.__your_desorder

    def __create_file(self):
        self.__my_file = open(self.__last_path, 'w')
        self.__my_file.write('\t\t\t<<< resultado de test emocional >>>\n\n')
        self.__my_file.write(self.__text_percepcion)
        self.__my_file.write(self.__text_comprension)
        self.__my_file.write(self.__text_regulacion + '\n')
        self.__my_file.write(self.__text_estado)
        self.__my_file.close()
        # abrimos el archivo en mouse path
        os.system('mousepad ' + self.__last_path)

    def __generate_text(self, path):
        text = ''
        self.__my_file = open(path, 'r')
        for line in self.__my_file:
            text += line
        self.__my_file.close()
        return text

    def _go_results(self):
        percepcion = self.__nivel_percepcion
        comprension = self.__nivel_comprension
        regulacion = self.__nivel_regulacion
        estado= self.__your_desorder

        # Verificacion dependiendo del resultado
        if percepcion == 'poca_percepcion':
            self.__text_percepcion = '\nSu nivel de percepcion de sentimientos:\n\tpoca, requiere mejorar percepcion.'
        elif percepcion == 'adecuada_percepcion':
            self.__text_percepcion = '\n\nSu nivel de percepcion de sentimientos:\n\tadecuada.'
        elif percepcion == 'demasiada_percepcion':
            self.__text_percepcion = '\n\nSu nivel de percepcion de sentimientos:\n\tdemasiada, relaje su percepcion.'

        # Resultados de comprension
        if comprension == 'poca_comprension':
            self.__text_comprension = '\n\nNivel comprension de edos emocionales:\n\tpoca, debe mejorar su comprension.'
        elif comprension == 'adecuada_comprension':
            self.__text_comprension = '\n\nNivel comprension de edos emocionales:\n\tadecuada, puede mejorar su comprension.'
        elif comprension == 'excelente_comprension':
            self.__text_comprension = '\n\nNivel comprension de edos emocionales:\n\texcelente.'

        # Resultados de regulacion
        if regulacion == 'poca_regulacion':
            self.__text_regulacion = '\n\nNivel regulacion de edos emocionales:\n\tpoca, debe mejorar su regulacion.'
        elif regulacion == 'adecuada_regulacion':
            self.__text_regulacion = '\n\nNivel regulacion de edos emocionales:\n\tadecuada, puede mejorar su regulacion.'
        elif regulacion == 'excelente_regulacion':
            self.__text_regulacion = '\n\nNivel regulacion de edos emocionales:\n\texcelente.'

        if estado == 'pas_positivo':
            self.__text_estado = self.__generate_text(self.__pas_path)
        elif estado == 'ezquizoide_positivo':
            self.__text_estado = self.__generate_text(self.__esquizoide_path)
        elif estado == 'emocional_positivo':
            self.__text_estado = self.__generate_text(self.__emocional_path)
        elif estado == 'toc_positivo':
            self.__text_estado = self.__generate_text(self.__toc_path)
        elif estado == 'sociopata_positivo':
            self.__text_estado = self.__generate_text(self.__sociopata_path)
        elif estado == 'estable_positivo':
            self.__text_estado = self.__generate_text(self.__estable_path)
        else :
            self.__text_estado = self.__generate_text(self.__default_path)

    def _first_move(self):
        # metodos por orden de ejecucion
        self._solve_total_percepcion()
        self._solve_total_comprension()
        self._solve_total_regulacion()
        # obteniendo el nivel de cada uno de los tres aspectos, percepcion, comprension y regulacion
        self._result_percepcion()
        self._result_comprension()
        self._result_regulacion()
        # Obteniendo la segunda face, es el tipo de posible trastorno
        self._get_type_desorder()
        self.impresion_final()
        self._go_results()
        self.__create_file()

class RunAnswer:
    @staticmethod
    def _construir(list_answers):
        print 'ok, pasando a lo ultimo'
        print list_answers
        machine_answer = Answers()
        machine_answer._list_answer = list_answers
        machine_answer._first_move()