# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 08:26:27 2022

@author: jorda
"""

import streamlit as st

import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

import pandas as pd
import streamlit as st

st.title("Welcome to Streamlit!")

st.write("Our first DataFrame")

st.write(
  pd.DataFrame({
      'A': [1, 2, 3, 4],
      'B': [5, 6, 7, 8]
    })
)

import pandas as pd
import streamlit as st

st.title("Welcome to Streamlit!")

st.write("Line Chart in Streamlit")
# 10 * 2 dimensional data
chart_data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)
