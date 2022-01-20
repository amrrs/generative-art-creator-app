import streamlit as st # web app 

# disable the pyplot deprecation warning 
st.set_option('deprecation.showPyplotGlobalUse', False)

# matplotlib for showing chART 
import matplotlib.pyplot as plt


# samile for generative ART 
from samila import GenerativeImage
# projections
from samila import Projection
# valid colors 
from samila import VALID_COLORS

# random generation
import random 
# math function 
from math import sin,cos 


# title of the app 
st.title("Generative Art creator 🎨 ")

st.markdown("#  NFT in Python 🐍")

# the hyperlink for the samila repo 

st.markdown("More Details about the inner workings of samile  >>> [Click Here](https://github.com/sepandhaghighi/samila)")


# equation selection 

fn1 = st.sidebar.selectbox("First EQ", ['sin','cos'])
fn2 = st.sidebar.selectbox("Second EQ", ['sin','cos'])

# first function for art gen 
def f1(x, y):
    if fn1 == 'sin':
        result = random.uniform(-1,1) * x**2  -  sin(y**2) + abs(y-x)
    elif fn1 == 'cos':
        result = random.uniform(-1,1) * x**2  -  cos(y**2) + abs(y-x)
    return result

# second function 
def f2(x, y):
    if fn2 == 'cos':
        result = random.uniform(-1,1) * y**3 - cos(x**2) + 2*x
    elif fn2 == 'sin':
        result = random.uniform(-1,1) * y**3 - sin(x**2) + 2*x
    return result

# projections  user input as radio button 

projections = st.sidebar.radio("Select the ART Projection here:", 
                options=["RECTILINEAR","POLAR", 'AITOFF', 'HAMMER', 'LAMBERT', 'MOLLWEIDE'],
                )



st.sidebar.markdown("**Color Selection**")

color = st.sidebar.selectbox("Art Color:",VALID_COLORS, index = 30)

bgcolor = st.sidebar.selectbox("Background Color:",VALID_COLORS, index = 15)

# progress bar or waiting spinner 
with st.spinner("Greatness is coming.....🪄"):
    g = GenerativeImage(f1, f2)
    g.generate()
    st.pyplot(g.plot(color = color, bgcolor = bgcolor, projection = eval("Projection."+projections)))
    st.caption("seed value to regenerate this image is : " + str (g.seed))