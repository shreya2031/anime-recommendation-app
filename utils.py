import streamlit as st
import base64
from streamlit.components.v1 import html

from PATHS import NAVBAR_PATHS
import base64

def add_bg_from_local():
    image_file = 'assets/images/background.png'
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
  
    

def inject_custom_css():
    with open('assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def get_current_route():
    try:
        return st.experimental_get_query_params()['nav'][0]
    except:
        return None


def navbar_component():
    with open("assets/images/logo.png", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())

    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += (f'<a class="navitem" href="/?nav={value}">{key}</a>')



    component = rf'''
            <nav class="container navbar" id="navbar">
                <ul class="navlist">
                {navbar_items}
                </ul>
                <div class="dropdown">
                    <img class="dropbtn" src="data:image/png;base64, {image_as_base64.decode("utf-8")}"/></img>
                </div>
            </nav>
            '''

    st.markdown(component, unsafe_allow_html=True)
    js = '''
    <script>
        // navbar elements
        var navigationTabs = window.parent.document.getElementsByClassName("navitem");
        var cleanNavbar = function(navigation_element) {
            navigation_element.removeAttribute('target')
        }
        
        for (var i = 0; i < navigationTabs.length; i++) {
            cleanNavbar(navigationTabs[i]);
        }
        
        
    </script>
    '''
    html(js)
