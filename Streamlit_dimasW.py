import streamlit as st
from PIL import Image
import pandas as pd
st.title('HI! My Name Is Dimas Wibisono')
st.header('This Is My Portofolio as Data Science📊')


Page = st.sidebar.radio('SELECT PAGE',['About Me', 'Project 1', 'Project 2', 'Project 3'])

if Page == 'About Me' :
    import About
    About.aboutme()

if Page == 'Project 1' :
    import project_1
    project_1.projek1()

if Page == 'Project 2' :
    import project_2
    project_2.projek2()   

if Page == 'Project 3' :
    import project_3
    project_3.projek3()    
        