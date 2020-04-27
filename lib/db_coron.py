from lib.db_manager import db_manager
from lib.settings import *
__URL = "https://api.covid19api.com/summary"
db_object = db_manager(host, user, passwd, __URL, token)
covid_19_data = db_object.get_all_data()
db_object.save_all_data(covid_19_data)


class db_coron():
    def zap(self, covid_19_data):
        db_object.dell_corona()
        for item in covid_19_data["Countries"]:
            Country = item["Country"]
            CountryCode = item["CountryCode"]
            Slug = item["Slug"]
            NewConfirmed = item["NewConfirmed"]
            TotalConfirmed = item["TotalConfirmed"]
            NewDeaths = item["NewDeaths"]
            TotalDeaths = item["TotalDeaths"]
            NewRecovered = item["NewRecovered"]
            TotalRecovered = item["TotalRecovered"]
            db_object.add_corona(Country, CountryCode, Slug, NewConfirmed, TotalConfirmed,
                                 NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)

    def vyvid(self, vyb_Country, con, coc):
        cor = db_object.vyvid_corona()
        return cor
        # for item in cor:
        #     if vyb_Country == 0 and con == "0" and coc == "0":
        #         print("======================================================")
        #         print("Country => \t\t", item[1])
        #         print("CountryCode => \t\t", item[2])
        #         print("Slug => \t\t", item[3])
        #         print("NewConfirmed => \t", item[4])
        #         print("TotalConfirmed => \t", item[5])
        #         print("NewDeaths => \t\t", item[6])
        #         print("TotalDeaths => \t\t", item[7])
        #         print("NewRecovered => \t", item[8])
        #         print("TotalRecovered => \t", item[9])
        #         print("======================================================")
        #     elif vyb_Country == 1 and item[1] == con:
        #         print("======================================================")
        #         print("Country => \t\t", item[1])
        #         print("CountryCode => \t\t", item[2])
        #         print("Slug => \t\t", item[3])
        #         print("NewConfirmed => \t", item[4])
        #         print("TotalConfirmed => \t", item[5])
        #         print("NewDeaths => \t\t", item[6])
        #         print("TotalDeaths => \t\t", item[7])
        #         print("NewRecovered => \t", item[8])
        #         print("TotalRecovered => \t", item[9])
        #         print("======================================================")
        #     elif vyb_Country == 2 and item[2] == coc:
        #         print("======================================================")
        #         print("Country => \t\t", item[1])
        #         print("CountryCode => \t\t", item[2])
        #         print("Slug => \t\t", item[3])
        #         print("NewConfirmed => \t", item[4])
        #         print("TotalConfirmed => \t", item[5])
        #         print("NewDeaths => \t\t", item[6])
        #         print("TotalDeaths => \t\t", item[7])
        #         print("NewRecovered => \t", item[8])
        #         print("TotalRecovered => \t", item[9])
        #         print("======================================================")
