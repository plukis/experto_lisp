# -*- coding: utf-8 -*-
import sys
from c_answers import RunAnswer
from kivy.app import App
# kivy.require("1.9.1")
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

# NOTA !!!! cambiar la ruta para llamara el archivo de la vista
dialog_question = Builder.load_file('/views/questions.kv')

class Controller(BoxLayout):

    # valores default de las vistas
    label_1 = 'Grado poco: 1 ,2, 3;\n'
    label_2 = 'Grado medio: 4;\n'
    label_3 = 'Grado mucho: 5, 6, 7;'
    label_leyenda = '[color=000000]' + label_1 + label_2 + label_3 +'[/color]'
    question_no = 1
    # solo puse el 25 por lo del ciclo, ya que el indice cero tiene la palabra cero
    last_question = 25
    __list_pregunta = []
    __list_answer = []
    __list_answer.append('nada')
    respuesta_1 = 'grado 1'
    respuesta_2 = 'grado 2'
    respuesta_3 = 'grado 3'
    respuesta_4 = 'grado 4'
    respuesta_5 = 'grado 5'
    botton_exit = 'Salir del programa'
    botton_siguiente = 'Enviar Respuesta'

    # lista de preguntas
    __list_pregunta.append('nada, pregunta cero no existe')
    __list_pregunta.append('1 >> Presto atencion al tema de los sentimientos ??')
    __list_pregunta.append('2 >> Me preocupo mucho por lo que siento o dejo de sentir ??')
    __list_pregunta.append('3 >> Normalmente dedico tiempo a pensar en mis emociones ?? ')
    __list_pregunta.append('4 >> Pienso que merece la pena prestar atencion\na mis emociones y estados de animo ??')
    __list_pregunta.append('5 >> Dejo que mis sentimientos afecten mis pensamientos ??')
    __list_pregunta.append('6 >> Pienso en mi estado de animo constantemente ??')
    __list_pregunta.append('7 >> A menudo pienso en mis sentimientos ??')
    __list_pregunta.append('8 >> Presto mucha atencion a como me siento ??')
    __list_pregunta.append('9 >> Tengo claros mis sentimientos ??')
    __list_pregunta.append('10 >> Frecuentemente puedo definir mis sentimientos ??')
    __list_pregunta.append('11 >> Casi siempre se como me siento ??')
    __list_pregunta.append('12 >> Normalmente conosco lo que siento sobre alguna persona ??')
    __list_pregunta.append('13 >> A menudo me doy cuenta de mis sentimientos en diferentes situaciones ??')
    __list_pregunta.append('14 >> Siempre puedo decir con honestidad el como me siento ??')
    __list_pregunta.append('15 >> A veces puedo decir cuales son mis emociones ??')
    __list_pregunta.append('16 >> Puedo llegar a comprender mis sentimientos ??')
    __list_pregunta.append('17 >> Aunque a veces me siento triste, suelo tener una vision optimista ??')
    __list_pregunta.append('18 >> Aunque me sienta mal, procuro pensar en cosas agradables ??')
    __list_pregunta.append('19 >> Cuando estoy triste pienso en todos los placeres de la vida ??')
    __list_pregunta.append('20 >> Hago el intento de tener pensamientos positivos aunque me sienta mal ??')
    __list_pregunta.append('21 >> Si doy demasiadas vueltas a las cosas, complicandolas.\nTrato de calmarme ??')
    __list_pregunta.append('22 >> Me preocupo por tener un buen estado de animo ??')
    __list_pregunta.append('23 >> Tengo mucha energia cuando me siento feliz ??')
    __list_pregunta.append('24 >> Cuando estoy enfadado intento cambiar mi estado de animo ??')
    # primera pregunta
    pregunta = __list_pregunta[1]
    answer = '0'
    _list_questions = []

    # objetos de tipo propiedad
    label_warning =  ObjectProperty()
    dinamic_question = ObjectProperty()

    def get_answer(self, grado):
        self.answer = grado
        if self.answer != '0':
            self.label_warning.text = ''

    def next_question(self):
        if self.answer == '0':
            self.label_warning.text = '[color=EFF552]Favor de elegir alguna de las opciones para continuar[/color]'
        else:
            # aumento el numero de la pregunta en la que vamos
            self.question_no += 1
            self.__list_answer.append(self.answer)
            if self.question_no < self.last_question:
                self.dinamic_question.text = self.__list_pregunta[self.question_no]
            else:
                print 'salimos de pantalla de preguntas ... '
                #RunAnswer._construir(self.__list_answer)
                salirPreguntas(self.__list_answer)
    def exit_program(self):
        sys.exit()

class SistemExpertoApp(App):
    def build(self):
        return Controller()

class Corre:
    def __init__(self):
        SistemExpertoApp().run()

def salirPreguntas(list_answer):
    RunAnswer._construir(list_answer)