class Product:
    price = None
    name = None

    def __repr__(self):
        return str(self.__dict__)