# -*- coding: utf-8 -*-
from pyswip.prolog import Prolog


class MainController:
    def __init__(self):

        # http://nullege.com/codes/search/pyswip.prolog.Prolog.query
        self.__root = ''
        self.__on_prolog = 'prolog'
        self.__of_prolog = 'halt.'

        # Preguntas
        self.__a_animal = 'animal(X).'
        self.__prolog = Prolog()
        self._probando()

    def _verifica_animal(self):
        self.__prolog.consult(self.__root)
        print '\nprolog dame ejemplos de animales: '
        for soln in self.__prolog.query(self.__a_animal):
            X = soln["X"]
            print X

    def _probando(self):
        Question().run()
