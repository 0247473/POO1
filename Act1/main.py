class Empleado:
    nombre: str
    puesto : str
    antiguedad: int
    extra: int

    def __init__(self, nombre, puesto, antiguedad):
      self.nombre= nombre
      self.puesto= puesto
      self.antiguedad= antiguedad
      self.extra = 345
      if puesto == "Gerente":
        self.salario = 50000
      if puesto == "Secretaria":
        self.salario = 15000
      if puesto == "Programador":
        self.salario = 25000
      if puesto != "Gerente":
       if antiguedad >= 1:
        self.salario = self.salario + (1000*self.antiguedad) + self.extra 
    def __repr__(self):
      return "("+ str(self.nombre)+ "," + str(self.salario) + ")"

class Gerente:
    def __init__(self, nombre, puesto, antiguedad):
      self.nombre= nombre
      self.puesto= puesto
      self.antiguedad= antiguedad
      print(Empleado(self.nombre,self.puesto,self.antiguedad))
      
class Secretaria:
    def __init__(self, nombre, puesto, antiguedad):
      self.nombre= nombre
      self.puesto= puesto
      self.antiguedad= antiguedad
      print(Empleado(self.nombre,self.puesto,self.antiguedad))
      
class Programador:
    def __init__(self, nombre, puesto, antiguedad):
      self.nombre= nombre
      self.puesto= puesto
      self.antiguedad= antiguedad
      print(Empleado(self.nombre,self.puesto,self.antiguedad))

print(Gerente("Miguel Perez", "Gerente", 3), Secretaria("Maria Gutierrez", "Secretaria", 4), Programador("Enrique Gutierrez", "Programador", 1))
