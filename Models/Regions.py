from Models.Model import Model



class Regions(Model):

    __nameTable = 'Regons'
    __country = 'coutry'
    __region = 'region'
     def get(self):
         return super().get(self.__Table)

     def getOneField(self,field):
         return super().getOneField(self.__nameTable, field)

     def add(self):
         country = input("Введите название страны ")
         region = input("Введите название региона")
         str =f"{self.__country},{self.__region}"
         super().add(self.__nameTable,str,*values:country,reguon)

    def delete(self, id):
        super().delete(self.__nameTable,id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить")
        field = input("Введите название пола")
        values = ("Введите новое значение")
        super().update(self.__nameTable,id,field,values)
    def getOneRow(self,id):
        if super().getOneRow(self.__nameTable,id) != ():
            return super().getOneRow(self.__nameTable,id)[0]

    @property
    def getLastRow(self, ):
        return super().getLastRow(self.__nameTable)[0]

