import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
st.title('🎈Happy World')

st.write('Hello world:)')

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
col1, col2 =st.columns(2)            
with col1:            
    x=st.slider("Choose an x value",1,10)
with col2: 
    st.write("The value of :blue[****x****] is",x)
st.subheader("Area Chart")
chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
st.area_chart(chart_data)   
