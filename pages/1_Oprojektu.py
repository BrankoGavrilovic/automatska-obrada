from asyncore import write
from logging import warning
from sre_constants import SUCCESS
import streamlit as st
st.header("Analiza otvorenih podataka")
st.info("Otvoreni podaci jesu podaci koje svi mogu slobodno da koriste, ponovno koriste i distribiraju - pod uslovom da se navede autor i da se deli pod istim uslovima.")
st.video("https://youtu.be/8aNbRUc3hnM",format="video/mp4", start_time=0)
st.write("Osnovne karakteristike otvorenih podataka su:")
st.write("Dostupnost i pristupačnost: Podaci moraju biti dostupni u celosti i po ceni ne većoj od realne cene štampe, poželjno preuzimanjem sa interneta.")
st.write("Ponovna upotreba i redistribucija: Podaci se pružaju uz dozvolu za ponovno korišćenje i redistribuciju, uključujući mešanje sa drugim skupovima podataka.")
st.write("Globalna uključenost: Svi moraju imati pravo na korišćenje, ponovno korišćenje i redistribuciju")
st.warning("Osnovna karakteristika otvorenosti podataka je interoperabilnost.")
st.write("Interoperabilnost podrazumeva mogućnost različitih sistema i organizacija da rade zajedno (među-delovanje). U ovom slučaju, reč je o mogućnosti zajedničkog rada ili spajanja različitih skupova podataka.")
st.success("Nadamo se da smo uspeli da vas uvedemo u svet otvorenih podataka i njhove analize!")