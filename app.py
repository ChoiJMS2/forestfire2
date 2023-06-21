# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu
from home_app import run_home
from model.dl_app import run_model
from service.service_app import run_service

def main():
    """
        Main function to run the Streamlit app.
    """
    st.set_page_config(page_title="Minimize forest fire damage", page_icon=":🔥:",
                            layout = "wide", initial_sidebar_state="expanded")

    st.header(":fire: 산불 피해 최소화 :firefighter:")
    # Streamlit 앱 실행
    with st.sidebar:
        selected = option_menu("Main Menu", ['Home', 'Deep Learning', 'Service'],
                               icons=['house', 'clipboard-data', 'gear'],
                               menu_icon="app-indicator", default_index=0, orientation = 'vertical', key='main_option',
                               styles={
                                   "container": {"padding": "5!important", "background-color": "#fafafa"},
                                   "icon": {"color": "orange", "font-size": "25px"},
                                   "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                                "--hover-color": "#eee"},
                                   "nav-link-selected": {"background-color": "#02ab21"},
                                   }
                               )
    if selected == 'Home':
        run_home()
    elif selected == 'Deep Learning':
        run_model()
    elif selected == 'Service':
        run_service()
    else:
        print('error..')


if __name__ == "__main__":
    main()