from Model.Persona import Persona
from Model.Curso import Curso
#CREANDO LA INSTANCIA DE PERSONA EN EL OBJETO OBJPERSONA
objPersona= Persona(" Luis",
                    "Salvatierra",
                    "122345678",
                    "Lsalvatierra@gmail.com")

objPersona.saludar()
objCurso=Curso("C001", "EPOO 1", 5)
objCurso.set_credito(4)
objCurso.bienvenido()
objCurso.set_nombre("Base de datos")
objCurso.bienvenido()
