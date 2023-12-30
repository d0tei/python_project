from Models.Model import Model
class Models:
 class Climbers(Models):
    __nameTable = 'Climbers'
    __name = 'name'
    __address = 'address'
    def get(self):
        return super(). get(self.__nameTable)
    
    def getOneFild(self, field):
        return  super().getOneField(self.__nameTable, field)
    
    def add(self):
        name = input("Введите имя: ")
        address = input("Введите адрес")
        str = f"{self.__name},{self.__address}"
        super().add(self.__nameTable,str,*values:name,address)
        
    def delete(self, id):
        super().delete(self.__nameTable,id)

    def update(self, id, field, values):
        id = input("Введите id записи, которую хотите изменить  ")
        field = input("Введите название поля")
        values = input("Введите новое значение")
        super().update(self.__nameTable,id,field,values)




