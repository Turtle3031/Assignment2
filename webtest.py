# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 08:26:27 2022

@author: jorda
"""


import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
#C:/Users/jorda/OneDrive/Desktop/Assignment 2(3)/Webapp.csv
# C:/Users/jorda/OneDrive/Desktop/Assignment 2(3)/1280px-Coffee_beans2.jpg

st.write(""""Vision Tea and Coffee""")        
#url = "https://github.com/Turtle3031/Assignment2/blob/82ff5674a743aba5930faa9020d3c424051ae888/1280px-Coffee_beans2.png"
#html = pd.read_html(url, header = 0)
#image = Image.open('C:/Users/jorda/OneDrive/Desktop/Assignment 2(3)/1280px-Coffee_beans2.jpg',"rb")
#st.image(image, caption= 'ML', use_column_width=True)

#url2 = "https://github.com/Turtle3031/Assignment2/blob/a53b46cdf7fd704d7323e39da0397ccf2e4bb3d9/Webapp.csv"
#html2 = pd.read_html(url2, header = 0)
df= pd.read_csv('C:/Users/jorda/OneDrive/Desktop/Assignment 2(3)/Webapp.csv', "rb")

st.subheader("The raw data table, no weighting")
st.dataframe(df)
st.write(df.describe())
st.bar_chart(df)



st.text("Disclaimer: This app cannot fix/help someone in terminally ill state, particularly if taking different medication treatments. It may slow the process of diseases slowly assuming no medical interactions, if that is the case this AI does not cover that (chemical interactions in pharamaceuticals). Spatial (global) time series (1960-2026) large scale Data Problem is accurate mostly to 90-95% of population, exact genetic biomarking with functional mutagenesis changes and family trees, is not factored in, its believed to have a 2-5% impact compared to the environment, mutagenesis has big impacts on the terminally ill and end of life, generally not those under 60-70 in most cases except the severely disabled. This App does not take any responsibility for those in a terminally ill state, its designed to prevent it happening or slow the progression of disease, if in a bad disease or terminally ill state, consult your doctor or medical professional. This App may slow the disease in those states (assuming no drug or surgical interactions) but the doctors may recommend pharmaceutical or surgical treatments that are not tested in these models and may significantly change outcomes. The app is not a replacement for medical treatment, just natural healthcare advice.")
st.text("""Prevention Data
	CANT USE AT ALL DUE  TO  ONLY NON COMMERCIAL AGREEMENTS ONLY, NO NEGOTIATION CLAUSE'
'	Global  Innovation Index 2022,  Analysis, viewed 13/01/2022,< https://www.globalinnovationindex.org/analysis-indicator/>.'
'   Commercial Lock Fees'
'	IHME 2022, GBD Compare, viewed 13/01/2022, <https://vizhub.healthdata.org/gbd-compare/>.'
'	Commercial Lock Recognition and Permission'
'	Australian Food and Safety 2022, Is it safe for children to drink coffee, viewed  13/01/2022,  https://www.foodsafety.com.au/blog/is-it-safe-for-children-to-drink-coffee'
'	OECD 2022, OECD better life index, viewed 13/01/2022, <https://www.oecdbetterlifeindex.org/#/50000000000>.'
'	Statista 2022, Sugar Consumption Worldwide, viewed 13/01/2022,< https://www.statista.com/statistics/496002/sugar-consumption-worldwide/>.'
'	Vision of Humanity 2022, 2021 Global Peace Index, viewed 13/01/2022, <https://www.visionofhumanity.org/maps/#/>.'
'	World Economic Forum 2022, Which Countries Get the Most Sleep and how much do we really need, viewed 13/01/2022, <https://www.weforum.org/agenda/2019/04/which-countries-get-the-most-sleep-and-how-much-do-we-really-need/>.'
'	World Health Organisation 2022, Exposure to solar ultraviolet UV radiation globally, viewed 13/01/2022,< https://www.who.int/about/policies/publishing/copyright>.'
'	Free with recognition '
'	Caffeine Informer 2022, Caffeine  Consumption by Country, viewed 13/01/2021, https://www.caffeineinformer.com/caffeine-what-the-world-drinks'
'	Google Trends 2022, Google Trends, viewed 13/01/2022, https://trends.google.com/trends/?geo=AU..'
'	John Hopkins Medicine 2022, Newsroom, viewed 13/01/2022, https://www.hopkinsallchildrens.org/ACH-News/General-News/Is-Coffee-Bad-for-Kids'
'	Klepeis, N.E., Nelson, W.C., Ott, W.R., Robinson, J.P., Tsang, A.M., Switzer, P., Behar, J.V., Hern, S.C. and Engelmann, W.H., 2001, ‘The National Human Activity Pattern Survey (NHAPS): a resource for assessing exposure to environmental pollutants’, Journal of Exposure Science & Environmental Epidemiology,  vol11, no.3,  pp.231-252.'
'	Lieberman, H.R., Agarwal, S. and Fulgoni III, V.L., 2019, ‘Daily patterns of caffeine intake and the association of intake with multiple sociodemographic and lifestyle factors in US adults based on the NHANES 2007–2012 surveys’, Journal of the Academy of Nutrition and Dietetics, vol. 119, no 1, pp.106-114.'
'	LMC International 2022, Global Markets for Decaffinated Coffee, viewed 13/01/2022, https://www.lmc.co.uk/wp-content/uploads/2019/04/LMC-Global-Markets-for-Decaffeinated-Coffee.pdf'
'	Our World In Data 2022a, Coronavirus (Covid 19) Vaccinations, viewed 13/01/2022, <https://ourworldindata.org/covid-vaccinations>.'
'	Our World In Data 2022b, Vaccinations, viewed 13/01/2022, <https://ourworldindata.org/vaccination>.'
'	Our World  In Data 2022c,  Happiness and Life Satisfaction, viewed 13/01/2022, https://ourworldindata.org/happiness-and-life-satisfaction'
'	Our World In Data  2022d, Meat and Dairy Production, viewed 13/01/2022, https://ourworldindata.org/meat-production'
'	Our World In Data 2022e, Crop Yeilds, viewed 13/01/2022, <https://ourworldindata.org/crop-yields>.'
'	Our World In Data 2022f, Vegetable Consumption Per Capita, viewed 13/01/2021, https://ourworldindata.org/grapher/vegetable-consumption-per-capita'
'	Our World  In Data 2022g, Fruit Consumption Per Capita, viewed 13/01/2021, <https://ourworldindata.org/grapher/fruit-consumption-per-capita>.'
'	Our World In Data 2022h, Food supply, viewed 13/01/2021, https://ourworldindata.org/food-supply'
'	The World Bank 2022b,  Unemployment Total (% total labor force)(modelled ISO estimate), viewed 13/01/2021, https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?view=map'
'	The World Bank 2022c,  GDP Growth Annual Percentage, viewed 13/01/2022, <https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?view=map&year=2020>.'
'	Yale 2022,  Environmental Performance Index, viewed 13/02/2022, <https://epi.yale.edu/epi-results/2020/component/epi>.'
""")
