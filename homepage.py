import streamlit as st
st.title("Početna strana ")
st.markdown("Na ovoj stranici možete se upoznati sa problematikom koja je obrađena u ovom projektu a tiče se saobraćajnih nesreća u Srbiji")
st.markdown("Unesite vaše ime i kliknite dugme da bi pogledali dalji tekst")
st.sidebar.success("Izaberi stranicu")
if "my_input" not in st.session_state:
    st.session_state["my_input"]=""
my_input=st.text_input("Unesi ime",st.session_state["my_input"]) 
submit=st.button("Klikni")   
if submit:
    st.session_state["my_input"]=my_input
    st.write( my_input,", dobrodošli na stranicu na kojoj možete analizirati podatke vezane za saobraćajne nezgode u Srbiji")
    st.warning("Saobraćajna nesreća je događaj na putu ili drugom mestu otvorenom za javni saobraćaj ili koji je započeo na takvom mestu, u kome je učestvovalo najmanje jedno vozilo u pokretu i u kome je jedno ili više lica poginulo ili povređeno ili je nastala materijalna šteta.")
    st.write("Da bi se jedan događaj mogao okarakterisati kao saobraćajna nezgoda (nesreća) bitno je da se :")
    st.info("1.Dogodio na površini koja je namenjena za saobraćaj")
    st.info("2.Da je učestvovalo najmanje jedno motorno vozilo u pokretu")
    st.info("Da je u nezgodi nastala šteta, na licima (povrede zadobio pešak, putnik, vozač...) i/ili na stvarima (slupano je vozilo, oštećena bandera, ograda kuće itd, nekome su pri povredi polomljene naočare ili je u sudaru sa motociklistom motociklisti uništena kaciga ili motociklističko odelo).")
    st.write("Zahvaljujući portalu otvorenih podataka data.gov podaci o saobraćajnim nesrećama dostupni su za dalju obradu")
    st.write("Cilj je da predstavimo i analiziramo podatke kako bi prevnirali neželjene događaje u budućnosti")
    st.image("https://www.dnevno.rs/wp-content/uploads/2021/04/auto-crne-boje-havarisan.jpg")