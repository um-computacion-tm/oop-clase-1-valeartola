import unittest
from materia import Materia, Profesor, Alumno

class TestMateria(unittest.TestCase):
    def test_materia(self):
        nombre = "Redes de datos"
        profesores = "Pablo"
        alumno1 = Alumno("Valentina", "62080", "20", "mv.artola")
        alumno2 = Alumno("Celina", "62146", "20", "celi.gd")
        alumnos = [alumno1,alumno2]
        materia = Materia(nombre, profesores,alumnos)
        self.assertEqual(materia.__nombre__, nombre)
        self.assertEqual(materia.__profesores__, profesores)
        self.assertEqual(materia.__alumnos__, alumnos)

    def test_obtener(self):
        profesores = "Pablo"
        alumno1 = Alumno("Valentina", "62080", "20", "mv.artola")
        alumno2 = Alumno("Celina", "62146", "20", "celi.gd")
        alumnos = [alumno1,alumno2]
        materia = Materia("Redes de datos", profesores,alumnos)

        self.assertEqual(materia.obtener_profesores(), profesores)

    def test_cambiar(self):
        nombre = "Redes de datos"
        alumno1 = Alumno("Valentina", "62080", "20", "mv.artola")
        alumno2 = Alumno("Celina", "62146", "20", "celi.gd")
        alumnos = [alumno1,alumno2]
        materia = Materia(nombre, "Pablo",alumnos)
        materia.cambiar_nombre("Bases de datos")

        self.assertEqual(materia.__nombre__, "Bases de datos")

    def test_obtener_alumnos(self):
        alumno1 = Alumno("Valentina", "62080", "20", "mv.artola")
        alumno2 = Alumno("Celina", "62146", "20", "celi.gd")
        alumno3 = Alumno('Victoria','62725','20','mvb.torres')
        alumnos = [alumno1,alumno2,alumno3]
        
        materia = Materia('Computacion','Daniel',alumnos)
        self.assertEqual(materia.obtener_alumnos(),alumnos)

class TestProfesor(unittest.TestCase):
    def test_profesor(self):
        profesores = Profesor("Pablo", "Jefe de tp", "55556")
        self.assertEqual(profesores.__nombre__, "Pablo")
        self.assertEqual(profesores.__cargo__, "Jefe de tp")
        self.assertEqual(profesores.__legajo__, "55556")

    def test_obtener_nomnbre(self):
        profesores = Profesor("Pablo", "Jefe de tp", "55556")
        self.assertEqual(profesores.obtener_nombre(), "Pablo")

    def test_obtener_cargo(self):
        profesores = Profesor("Pablo", "Jefe de tp", "55556")
        self.assertEqual(profesores.obtener_cargo(), "Jefe de tp")

    def test_obtener_legajo(self):
        profesores = Profesor("Pablo", "Jefe de tp", "55556")
        self.assertEqual(profesores.obtener_legajo(), "55556")

class TestAlumno(unittest.TestCase):
    def test_alumno(self):
        alumno = Alumno("Valentina", "62080", "20", "mv.artola")
        self.assertEqual(alumno.__nombre__, "Valentina")
        self.assertEqual(alumno.__legajo__, "62080")
        self.assertEqual(alumno.__edad__, "20")
        self.assertEqual(alumno.__mail__, "mv.artola") 

    def test_obtener_nombre(self):
        alumno = Alumno("Valentina", "62080", "20", "mv.artola")
        self.assertEqual(alumno.obtener_nombre(), "Valentina")

    def test_cambiar_mail(self):
        mail = "mv.artola"
        alumno = Alumno("Valentina", "62080", "20", mail)
        alumno.cambiar_mail("v.artola")
        self.assertEqual(alumno.__mail__, "v.artola")

    
       





if __name__ == "__main__":
    unittest.main()