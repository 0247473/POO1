class Empleado:
    nombre: str
    puesto : str
    antiguedad: int

    def __init__(self, nombre, puesto, antiguedad):
      self.nombre= nombre
      self.puesto= puesto
      self.antiguedad= antiguedad
      if puesto == "Gerente":
        self.salario = 50000
      if puesto == "Secretaria":
        self.salario = 15000
      if puesto == "Programador":
        self.salario = 25000
      if puesto != "Gerente":
       if antiguedad >= 1:
         
        self.salario = self.salario + (1000*self.antiguedad)    

    def __repr__(self):
      return "("+ str(self.nombre)+ "," + str(self.salario) + ")"



class Gerente:
    def __init__(self, nombre, puesto, antiguedad):
      self.nombre= nombre
      self.puesto= puesto
      self.antiguedad= antiguedad
      print("Buenos dias jefe")
      print(Empleado(self.nombre,self.puesto,self.antiguedad))
      

      


class Secretaria:
    def __init__(self, nombre, puesto, antiguedad):
      self.nombre= nombre
      self.puesto= puesto
      self.antiguedad= antiguedad
      print("Buen trabajo, espero que el gerente no la perjudicara tanto :D")
      print(Empleado(self.nombre,self.puesto,self.antiguedad))
      

class Programador:
    def __init__(self, nombre, puesto, antiguedad):
      self.nombre= nombre
      self.puesto= puesto
      self.antiguedad= antiguedad
      print("Buen trabajo, espero que no se cansara :D")
      print(Empleado(self.nombre,self.puesto,self.antiguedad))




Gerente1 = Gerente("Miguel Perez", "Gerente", 3)
Secretaria1 = Secretaria("Maria Gutierrez", "Secretaria", 4)
Programa1 = Programador("Enrique Gutierrez", "Programador", 1)
  

print(Gerente1, Secretaria1, Programa1)