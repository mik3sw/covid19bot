import requests
import datetime
from datetime import date

class Vaccines:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.json"
        
    
    def get_data_tot(self):
        r = requests.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.json")
        data = r.json()
        f = self.process_data_tot(data['data'])
        return f
    
    def process_data_tot(self, data):
        tot_somm = 0
        tot_cons = 0
        final = {}
        for region in data:
            tot_somm = tot_somm + int(region['dosi_somministrate'])
            tot_cons = tot_cons + int(region['dosi_consegnate'])
            final["{}_somministrate".format(region["area"])] = region['dosi_somministrate']
            final["{}_consegnate".format(region['area'])] = region['dosi_consegnate']

            #print(region)
        
        final["totale_somministrazioni"] = tot_somm
        final["totale_consegnate"] = tot_cons
        return final
    
    def get_data_age(self):
        r = requests.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.json")
        data = r.json()
        f = self.process_data_age(data['data'])
        return f

    def process_data_age(self, data):
        final = {}
        for age in data:
            final["{}".format(age["fascia_anagrafica"])] = age["totale"]
        return final
    
    def get_percentuale_somministrazioni(self):
        totale = self.get_data_tot()
        return round(float(totale["totale_somministrazioni"]/totale["totale_consegnate"]*100), 2)
    
    def get_percentuale_popolazione(self):
        popolazione = 60360000
        totale = self.get_data_tot()
        return round(float(totale["totale_somministrazioni"]/popolazione*100), 2)
    
    def get_media_giornaliera(self):
        totale = self.get_data_tot()
        today = date.today()
        d0 = date(2020, 12, 31)
        delta = today - d0
        giorni_passati = delta.days
        return round(totale["totale_somministrazioni"]/giorni_passati, 2)
    
    def calcolo_pazzerello(self):
        media_giorno = self.get_media_giornaliera()
        immunita_gregge = 42252000
        d0 = date(2020, 12, 31)
        giorni_necessari = 0
        tmp = 0
        while(tmp<immunita_gregge):
            giorni_necessari += 1
            tmp = tmp + media_giorno

        days_n = datetime.timedelta(giorni_necessari)
        new_date = d0 + days_n

        return giorni_necessari, new_date