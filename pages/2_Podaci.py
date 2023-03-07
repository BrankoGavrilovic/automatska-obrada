from asyncio.windows_events import NULL
from distutils.command.upload import upload
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#import plotly.express as px
st.header("Podaci o saobraćajnim nezgodama")
st.write("Na ovoj strani možete analizirati podatke o saobraćajnim nesrećama u Republici Srbiji.")
st.write("Da bi ispravno koristili aplikaciju neophodno je da preuzmete podatke sa portala otvorenih podataka data.gov.")
st.write("Kada preuzmete podatke na lokalni računar prevlačenjem postavljate u aplikaciju")
st.write("Aplikacija je prilagođena da obradi sve podatke vezane za saobraćajne nesreće dostupne na portalu.")
st.warning(" Aplikacija se može koristiti samo za podatke o saobraćajnim nesrećama")
upload_file=st.file_uploader("Izaberite fajl")
if upload_file is not NULL:
    df= pd.read_excel(upload_file)
    tabela=pd.DataFrame(df)
    tabela.columns=["ID broj neznode","Policijka uprava","Opština","Datum i vreme","lat","lon", "Vrsta","Tip","Opis"]  
    #data = tabela.drop(labels=0, axis=0)
    tabela
broj_saobraćajnih=len(tabela)
st.write("Ukupan broj saobraćajnih nezgoda na teritoriji Republike Srbije iznosi, ",broj_saobraćajnih)
st.write()
st.info("Na sledećem grafikonu prikazana je struktura saobraćajnih nesreća  po vrsti")
mat_steta=len(tabela[tabela["Vrsta"] == "Sa mat.stetom"])
povredjeni=len(tabela[tabela["Vrsta"] == "Sa povredjenim"])
poginuli=len(tabela[tabela["Vrsta"] == "Sa poginulim"])
vrstastete=("materijalna_steta","Sa_povređenim","Sa_poginulim")
broj=(mat_steta,povredjeni,poginuli)
Podaci_tabela=pd.DataFrame(broj,vrstastete)
st.bar_chart(Podaci_tabela)
#plt.title("Broj saobraćajnih nesreća po kategorijama")

lista=tabela["Policijka uprava"].unique().tolist()
lista1=tabela["Vrsta"].unique().tolist()
st.write("Izaberite upravu i vrstu prekršaja za koje želite da vidite podatke.")
opcija1=st.selectbox("Izaberi policijsku upravu", lista)
opcija2=st.selectbox("Izaberi vrstu prekršaja", lista1)
#opcija1,opcija2
tabela[(tabela["Policijka uprava"] == opcija1) & (tabela["Vrsta"] == opcija2)]
st.write("U policijskoj upravi",opcija1, "registrovano je ukupno",len(tabela[(tabela["Policijka uprava"] == opcija1) & (tabela["Vrsta"] == opcija2)]),"prekršaja", opcija2 )
tabela1=tabela[(tabela["Policijka uprava"] == opcija1) & (tabela["Vrsta"] == opcija2)]
lista2=tabela1["lat"].tolist()
lista3=tabela1["lon"].tolist()
lista4=tabela1["Datum i vreme"].tolist()
data = {"Datum_i_vreme":lista4,
        "lat":lista3,
        "lon":lista2
        }       
df = pd.DataFrame(data)
st.write("Tabela ispod daje tabelarni pregled datuma i vremena kada se dogodila nezgoda, kao i geografskih podataka gde se dogodila za izabrani kriterijum ")
df[["Datum","Vreme"]]=df.Datum_i_vreme.str.split(",",expand=True)
df
st.info("Ispod se može pogledati GEOLOKACIJA gde su se dogodile nesreće.")
st.map(data=df)





