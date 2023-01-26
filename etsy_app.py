import requests
from bs4 import BeautifulSoup
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import streamlit as st
import time
import datetime
from datetime import date



st.set_page_config(
    page_title = 'Etsy Spy',
    page_icon = '✅',
    layout = 'wide'
)

#interval = st.sidebar.selectbox("The Interval :" , ('5m','15m','1h','12h'))
#depth1 = st.sidebar.number_input("Enter The depth in heurs :", min_value=1, max_value=200, step=1)
#depth = str(depth1)

#ticker_txt = st.sidebar.text_input("Enter The Ticker :" , "")
store = st.sidebar.text_input("Etsy Store Name :" , "")

d1 = st.sidebar.date_input("Last Seen Date :",datetime.date.today())
d2 = st.sidebar.date_input("Today :",datetime.date.today())
delta = d2 - d1

if store != '':
    #etsy page store

    link = 'https://www.etsy.com/shop/'+ store
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    s = soup.find('span', class_='wt-text-caption wt-no-wrap').text.strip()
    sales = s.replace('Sales', '')
    
    
    #etsy cached store
    link = 'http://webcache.googleusercontent.com/search?q=cache:' + link
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    #l_s = soup.find('div', class_='pt-xs-3').text.strip()
    l_s = soup.find('span', class_='wt-text-caption wt-no-wrap').text.strip()
    l_sales = l_s.replace('Sales', '')
    
    cache_date = soup.find('div', id='bN015htcoyT__google-cache-hdr')
    date_ = cache_date.div.get_text()



    with st.spinner('Wait for it...'):
        time.sleep(0.5)
    st.success('Done!')



    st.markdown("**Last Seen**")
    date_ = date_.replace("This is Google's cache of https://www.etsy.com/shop/"+store+".", '')
    date_ = date_.replace('It is a snapshot of the page as it appeared on ', '')
    date_ = date_.replace("The current page could have changed in the meantime.", '')
    date_ = date_.replace("Learn more.", '')
    number1 = date_
    st.markdown(f"<h5 style='text-align: left; color: black;'>{number1}</h5>", unsafe_allow_html=True)


    kpi02, kpi03, kpi04, kpi05 = st.columns(4)
    with kpi02:
        st.markdown("**Last Sales**")
        number2 = l_sales
        st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

    with kpi03:
        st.markdown("**Actual Sales**")
        number3 = sales
        st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

    with kpi04:
        st.markdown("**Total Sales**")
        number4 = int(sales.replace(',', ''))- int(l_sales.replace(',', ''))
        st.markdown(f"<h1 style='text-align: center; color: red;'>{number4}</h1>", unsafe_allow_html=True)

    with kpi05:
        st.markdown("**Sales/Day**")
        if delta.days != 0:
            number5 = number4/int(delta.days)
        else:
            number5 = str(number4)+' today'
        st.markdown(f"<h1 style='text-align: center; color: red;'>{number5}</h1>", unsafe_allow_html=True)
