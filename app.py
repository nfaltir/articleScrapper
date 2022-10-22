import streamlit as st
import json
import requests
from bs4 import BeautifulSoup as bs


st.set_page_config(page_title="Web Scraper", page_icon="📜")
st.markdown("<h1 style='text-align: center; color: #4C4C6D;'> Article Scrapper </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4C4C6D;'>Scrape any news article from the web 🔐</h3>", unsafe_allow_html=True)
st.write("<hr><br>", unsafe_allow_html=True)


url = st.text_input("Enter or Paste news article url: ")

st.button("scrape")

if len(url) > 0:
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    page_data = [json.loads(x.string)for x in soup.find_all('script', type='application/ld+json')]
    for x in page_data:
        try:
            html_str = f"""
                <style>
                p {{
                text-align: justify;
                line-height: 1.75;
                font-size: 17px;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
                padding: 15px;
                margin-top:20px;
                margin-bottom:20px;
                }}
                </style>
                <p class="a">{x['articleBody']}</p>"""

            st.write(html_str, unsafe_allow_html=True)
        except KeyError:
            pass

