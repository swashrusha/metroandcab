import streamlit as st
import pandas as pd

st.title("METRO TICKET AND CAB BOOKING SYSTEM")
stations=["Ameerpet","Miyapur","LB Nagar","KPHB","JNTU"]
name=st.text_input("Passenger Name")
source=st.selectbox("From Station",stations)
destination=st.selectbox("To Station",stations)
ticket=st.selectbox("Number of Tickets",[1,2,3,4,5,6,7,8,9])

cab=st.radio("Do You Need a Cab?",["YES","NO"])

if cab=="NO":
    st.success("Metro Ticket Booked Successfully")
    st.write(f"Hi!! {name}")
    st.write("Ticket Details")
    st.write(f"Passenger:{name}")
    st.write(f"From Station:{source}")
    st.write(f"To Station:{destination}")
    st.write(f"Tickets:{ticket}")


elif cab=="YES":
    loc=st.text_input("Enter Drop Location")
    if st.button("BOOK"):
        st.success("Metro Ticket and Cab are Booked Successfully")
        st.write(f"Hi!! {name}")
        st.write("TICKET DETAILS")
        st.write(f"Passenger:{name}")
        st.write(f"From Station:{source}")
        st.write(f"To Station:{destination}")
        st.write(f"Tickets:{ticket}")
        st.write("CAB DETAILS")
        st.write(f"Pickup Point:{destination}")
        st.write(f"Drop:{loc}")
