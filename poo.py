 #!/usr/bin/python3


class Alumno:
	
	def __init__ (self, nombre):
		self.name = nombre


	def saluda (self):
		print("ola k ase " + self.name)


if __name__ == "__main__":
	john = Alumno("John")
	john.saluda();

	adri = Alumno("Adri")
	adri.saluda();

	alumnos = [Alumno("Lluc"), Alumno("Marcel"), Alumno("Pablo")]


	for alumno in alumnos:
		alumno.saluda();

	alumnos[1].saluda();



