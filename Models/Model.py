from Configuration.config import connection
class Model:
    def get(self, table):
        with connection().cursor() as cursor:
             select_all_rows = f"SELECT * FROM {table}"
             cursor.execute(select_all_rows)
             return cursor.fetchall()
        connection().close()

    def getOneField(self, table, field):
        with connection().cursor() as cursor:
             select_one_field = f"SELECT{field} FROM {table}"
             cursor.execute(select_one_field)
        connection().close()
        print(f"Новая запись в таблицу {table}добавлена")

    def delete(self, table, id):
        with connection().cursor() as cursor:
            query_delete = f"DELETE FROM{table} WHERE id = {id}"
            cursor.execute(query_delete)
            connection().commit()
        connection().close()
        print("Запись удалена")

    def update(self, table, id, field,values):
        with connection().cursor() as cursor:
           # print(f"UPDATE {table} set {field} = '{values}' where id = {id}")
            query_update = f"UPDATE {table} set {field} = '{values}' where id = {id}"
            cursor.execute(query_update)
            connection().commit()
        connection().close()
        print("Запись обновлена")


    def getOneRow(self, table,id):
        with connection().cursor() as cursor:
             query = f"SELECT * FROM {table} WHERE id = {id}"
             cursor.execute(query)
             return cursor.fetchall()
        connection().close()


    def getMountsClimbers(self):
        with connection().cursor() as cursor:
            query = ("select Climbers.name, Ascents.start_time,"
            +" (SELECT name from Mountaiins where id = Ascents.mountain,id AS Mountains"
            +"from Ascents_Climbers"
            +"JOIN Ascents"
            +"ON Ascents_Climbers.ascents_id = Ascents.id"
            +"JOIN Climbers"
            +"ON Ascents_Climbers.climbers-id = Climbers.id"
            +" ORDER BY Ascents.start_time")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close
    def getLastRow(self, tables):
        with connection().cursor()as cursor:
            query = f"SELECT * FROM Regions{table} ORDER BY id DESC LIMIT 1"
            cursor.execute(query)
            return  cursor.fetchall()
        connection().close()


    def getClimbersDate_Interval(self, first_date, lost_date):
        with connection().cursor() as cursor:


            query = (
                "SELECT Climbers.nmae, Ascents.start_time FROM Ascents_Climbers"
                +" JOIN Climbers ON Ascents_Climbers.climber_id = Climbers.id"
                +" JOIN Ascents ON Ascents_Climbers.ascent_id = Ascents"
                +f" WHERE Ascents.start_time BETWEEN'{first_date}' AND '{lost_date}'"
            )
            cursor.execute(query)
            return  cursor.fetchall()
        connection().close()

    def numberOfAscents(self):
        print(
         "SELECT"
         + " Climbers.name, Mountains.name, COUNT(*)"
         + " AscentsClimberscount"
         + " FROM"
         + " Ascents_Climbers, Climbers, Ascents, Mountains"
         + " WHERE"
         + " Ascents_Climbers.climber_id = Climbers.id"
         + " AND"
         + " Ascents_Climbers.ascent_id = Ascents.id"
         + " AND"
         + " Ascents.moutains_id = Mountains.id"
         + " GROUP"
         + " BY"
         + " Climbers.name, Mountains.name"
        )
        with connection().cursor() as cursor:
            query = (
                        "SELECT"
                        + " Climbers.name, Mountains.name, COUNT(*)"
                        + " AscentsClimberscount"
                        + " FROM"
                        + " Ascents_Climbers, Climbers, Ascents, Mountains"
                        + " WHERE"
                        + " Ascents_Climbers.climber_id = Climbers.id"
                        + " AND"
                        + " Ascents_Climbers.ascent_id = Ascents.id"
                        + " AND"
                        + " Ascents.moutains_id = Mountains.id"
                        + " GROUP"
                        + " BY"
                        + " Climbers.name, Mountains.name"
                )
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def getNumbersOfClimbers(self):
        print(
            "SELECT "
            +"Mountains.name, COUNT(*) "
            +"AS "
            +"countClimber "
            +"From "
            +"Mountains, Ascents, Ascents_Climbers, Climbers "
            +"WHERE "
            +"Mountains.id = Ascents.mountain_id "
            +"AND "
            +"Ascents.id = Ascents_Climbers.ascent_id "
            +"AND "
            +"Ascents_Climbers.climber_id = Climbers.id "
            +"GROUP "
            +"BY "
            +"Mountains.name "
            )
        with connection().cursor()as cursor:
            query = (
                "SELECT "
                +"Mountains.name, COUNT(*) "
                +"AS "
                +"countClimber "
                +"From "
                +"Mountains, Ascents, Ascents_Climbers, Climbers "
                +"WHERE "
                +"Mountains.id = Ascents.mountain_id "
                +"AND "
                +"Ascents.id = Ascents_Climbers.ascent_id "
                +"AND "
                +"Ascents_Climbers.climber_id = Climbers.id "
                +"GROUP "
                +"BY "
                +"Mountains.name "
                )
        cursor.execute(query)
        return cursor.fetchall()
    connection().close()







