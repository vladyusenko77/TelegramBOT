import mysql.connector
import requests
# if __name__ == "__main__":
#     db_manager


class db_manager():

    def __init__(self, host, user, passwd, url, token):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.__URL = url
        self.__db = mysql.connector.connect(
            host=self.host, user=self.user, passwd=self.passwd)
        self.__cursor = self.__db.cursor()

    def __del__(self):
        self.__db.close()

    def get_all_data(self):
        response = requests.get(self.__URL)
        return response.json()

    def save_all_data(self, data):
        # print("save_all_data => ", data)
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS COVID_19;")
        self.__cursor.execute("USE COVID_19;")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS CORON (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255),CountryCode VARCHAR(255), Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10),NewDeaths INT(10),TotalDeaths INT(10),NewRecovered INT(10),TotalRecovered INT(10))")

    def add_corona(self, Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered):
        sql = "INSERT INTO CORON (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed,
               NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)
        self.__cursor.execute(sql, val)
        self.__db.commit()

    def dell_corona(self):
        sql = "DELETE FROM `coron`"
        self.__cursor.execute(sql)
        self.__db.commit()

    def vyvid_corona(self):
        sql = "SELECT * FROM `coron` "
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()
        # for item in self.__cursor.fetchall():
        #     print(item)

    def show_country(self, countr):
        sql = ("SELECT * FROM CORON WHERE Country = '" + countr + "'")
        self.__cursor.execute(sql)
        coun = self.__cursor.fetchall()
        print(coun)
        return coun

    def show_country_CountryCode(self, countr):
        sql = ("SELECT * FROM CORON WHERE CountryCode = '" + countr + "'")
        self.__cursor.execute(sql)
        coun = self.__cursor.fetchall()
        print(coun)
        return coun
