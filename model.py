import csv
class Cliente:
    objetos = []

    def __init__(self, **kwargs):
        self.id = int(kwargs['id'])
        self.nombre = kwargs['nombre']
        self.apellidos = kwargs['apellidos']
        self.sexo = kwargs['sexo']
        self.email = kwargs['email']
        self.telefono = kwargs['telefono']
        self.direccion = kwargs['direccion']
        self.ciudad = kwargs['ciudad']
        self.pais = kwargs['pais']
        Cliente.objetos.append(self)

    def __repr__(self):
        return f'Cliente(id={repr(self.id)}, nombre={repr(self.nombre)}, apellidos={repr(self.nombre)})'

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

    @classmethod
    def cargar_datos(cls, archivo):
        with open(archivo, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Cliente(**row)
                print(f"Cargando cliente: {row}")

    @classmethod
    def todos(cls):
        return cls.objetos

    @classmethod
    def buscar(cls, id):
        for cliente in cls.objetos:
            if cliente.id == id:
                return cliente
        return None

    @classmethod
    def filtrar(cls, **kwargs):
        resultado = []
        for cliente in cls.objetos:
            if all(getattr(cliente, k) == v for k, v in kwargs.items()):
                resultado.append(cliente)
        return resultado
