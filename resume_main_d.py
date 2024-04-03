#%%
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import base64
from pathlib import Path

import streamlit as st


#%%



st.set_page_config(layout="wide")	

st.markdown("""
<style>
.big-font {
	font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.little-big {
	font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.medium-font {
	font-size:24px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
	<style>
		[data-testid=stSidebar] {
			background-color: #586CDB;
		}
	</style>
	""", unsafe_allow_html=True)
placeholder = st.empty()
with placeholder.container():
	col1, col2 = st.columns([0.2,0.8])
	with col1:
		st.markdown('''<p class="little-big"> Agnes McFarlin
		</p>''',unsafe_allow_html=True)
	with col2:
		st.markdown('''<p class="little-big">
		</p>''',unsafe_allow_html=True)
	st.markdown(''' <p class="little-big"> Data Scientist | Data Analyst </p>''',unsafe_allow_html=True)


sideb = st.sidebar
st.sidebar.markdown('<p class="big-font">Agnes McFarlin</p>',unsafe_allow_html=True)
st.sidebar.write("Enjoyer of science in all forms.")
st.sidebar.link_button("Github", "https://github.com/oohtmeel1")
check1 = sideb.button('Introduction')
check2 = sideb.button('Projects')
check3 = sideb.link_button("Resume", "https://drive.google.com/file/d/1-BEx1uV0IxAlkJiUqkNrGW3AnzWQFZf2/view?usp=sharing")


if check1:
	st.header("""Introduction : """)
	placeholder.empty()
	st.markdown('''<p class="little-big">Chemist turned Data Scientist: Applying existing knowledge to new enviornments.
			</p>''',unsafe_allow_html=True)
	col1, col2 = st.columns([0.2,0.8])
	with col1:
		st.empty()
	with col2:
		st.empty()
		#st.image("https://drive.google.com/uc?export=view&id=1zjzykI1bShq50pu1gkcp962afitfw35n")
  
  
  
	st.markdown(''' <p class="little-big">Education: 
			 Master's of Science Data Science, From University of Colorado Boulder. 
			 GPA obtained 3.8
				</p> While undertaking the Master's Program I became familliar with statistical analysis in Python and R. 
				Applied machine learning to solve various problems. 
				Learned how to visualize and interpret results with said software.
				   I was also introduced to SQL, for database management. I learned to perform queries and other basic SQL functions.''',unsafe_allow_html=True)
	with st.container():
		st.header("Software experience:")
		cola, colb, colc = st.columns(3)
		with cola:
			st.markdown('Python')
			st.image("python.png")
			st.markdown("- loading and cleaning structured and unstructured data.")
			st.markdown("- statistical analyis")
			st.markdown("- Machine Learning")
			st.markdown("- visualization of results")
		with colb:
			st.markdown('R-Studio')
			st.image("r_studio.png")
			st.markdown("- loading and cleaning structured data")
			st.markdown("- statistical analyis")
			st.markdown("- Machine Learning")
			st.markdown("- visualization of results")
		with colc:
			st.markdown('MySQL')
			st.image("my_sql.png")
			st.markdown("- querying data")
			st.markdown("- performing basic data manipulation functions")

  
  
if check2:
	placeholder.empty()
	st.title('Projects:bar_chart:')
	st.markdown('''<p class="little-big"> Some Python, R, Tableu, and a lot of data.</p>''',unsafe_allow_html=True)
	colp, colq, colr,colm = st.columns(4)
	with colp:
		with st.container():
			st.header("Tableu Visualization ")
			st.image("snip_of_viz_salmon.png")
			st.write('''
					Used data from several sources, cleaning and combining it, creating a visualization in Tableu.''')
			st.write("[Project Link](https://public.tableau.com/views/Salmoninfographic/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link)")
		with colq:
			with st.container():
				st.header("Machine Learning ")
				st.image("eia_logo.png")
				st.write('''
						Used data from the U.S. Energy Information Administration to perform prediction using Machine learning in Python.''')
				st.write("[Github Repo](https://github.com/oohtmeel1/Machine-Learning-_-Prediction_Electricity_Data/tree/main)")
    	with colr:
			with st.container():
				st.header("Machine Learning ")
				st.image("eia_logo.png")
				st.write('''
						Used data from the U.S. Energy Information Administration to perform prediction using Machine learning in Python.''')
				st.write("[Github Repo](https://github.com/oohtmeel1/Machine-Learning-_-Prediction_Electricity_Data/tree/main)")
	col1, col2, col3,col15 = st.columns(4)
	with col1:
		with st.container():
			st.header("Statistical analysis ")
			st.image("places_data_logo.png")
			st.write('''
					Used PLACES data from the CDC. Analyzed in Python, performed distribution fitting,correlation analysis, outlier analysis 
					 parametric and non parametric testing and discussed results. Libraries of note: scipy stats, distfit.''')
			st.write("[Project Link](https://github.com/oohtmeel1/Data_Mining_complete/)")
	with col2:
		with st.container():
			st.header("Text classification")
			st.image("small_graph.png")
			st.write('''
					Analyzed Twitter data in Python,  using NLTK, Seaborn and NetworkX to create directed and undirected graphs of text data.''')
			st.write("[Project Link](https://colab.research.google.com/drive/15An1jxoNVKclHzFsV58FiIrUrW3nS47T?usp=sharing/)")
	with col3:
		with st.container():
			st.header("Visualizaton and analysis")
			st.image("map_image.jpg")
			st.write('''
				 Used Python, Folium, Branca and other libraries in order to display and visualize Geospatial and finanacial data.''')
			st.write("[Project Link](https://oohtmeel1-coloradobouldervisalizations-my-app-final-j5ndhy.streamlit.app/)")
	with col15:
		with st.container():
			st.header("Machine Learning")
			st.image('''machine_learning_r.png''')
			st.write('''
				 Used R and various Machine Learning models to categorize Biomes based on water consumption data.''')
			st.write("[Project Link](https://github.com/oohtmeel1/Machine_Learning_R/)")
   
	col4,col5,col6,col16 = st.columns(4)
	with col4:
		with st.container():
			st.header("Machine Learning")
			st.image("birds.jpg")
			st.write(""" Used Python and machine learning (K-means)
					in order to categorize bird species based on skeletal structure.""")		
			st.write("[Repo link](https://github.com/oohtmeel1/Unsup2/tree/main)")
			st.write("[Final Notebook](https://github.com/oohtmeel1/Unsup2/blob/main/Kmeans_Report.ipynb/)")
	with col5:
		with st.container():
			st.header("Machine Learning")
			st.image("word_cloud.jpg")
			st.write("""Text categorization using Python, and a Bidirectional LSTM(RNN), to categorize tweets into Disaster or Not Disaster categories .""")
			st.write("[Repo link](https://github.com/oohtmeel1/Disaster_tweets/tree/main)")
			st.write("[Final Notebook](https://github.com/oohtmeel1/Disaster_tweets/blob/main/notebooke20b826a34%20(4).ipynb)")
	with col6:
		with st.container():
			st.header("Machine Learning")
			st.image("cell_images.jpg")
			st.write("""In python used Keras and tensorflow to classify medical images as being malignant or benign using a CNN. """)
			st.write("[Repo link](https://github.com/oohtmeel1/Week3DeepLearning)")
	with col16:
		with st.container():
			st.header("Tableu Visualization")
			st.image("tableu.png")
			st.write("""Used mySQL for working with the data and Tableu for visualization """)
			st.write("[Tableu Public link](https://public.tableau.com/shared/XGG2F8JDN?:display_count=n&:origin=viz_share_link)")
	col7,col8,col9,col19 = st.columns(4)
	with col7:
		with st.container():
			st.header("Machine Learning")
			st.image("daily_news.jpg")
			st.write("""In python compared unsupervised and supervised learning using different model types. """)
			st.write("[Notebook link](https://github.com/oohtmeel1/Unsup_learning/blob/main/Report_A.ipynb)")
	with col8:
		with st.container():
			st.header("Machine Learning")
			st.image("cats_and_dogs.jpg")
			
			st.write("""In Python used a CNN model to perform image classification on pets. Libraries of note, Tensorflow and Keras """)
			st.write("[Repo link](https://github.com/oohtmeel1/Deep_Learning_Final)")
	with col9:
		with st.container():
			st.header("Machine Learning")
			st.expander("Supervised learning sentiment analysis on text data")
			st.image("confusion.png")
			st.write(""" Cleaned and manually labelled enron email dataset in order to perform sentiment analysis in Python using Vader  sentiment analysis and SVM.""")
			st.write("[Repo link](https://github.com/oohtmeel1/Supervised_learning_project)")
	with col19:
		with st.container():
			st.header("Tableu Visualization")
			st.expander("Visualization of Financial Data")
			st.image("fishies.png")
			st.write(""" Gathered, cleaned and combined data from many sources, creating one report in Tableu""")
			st.write("[Tableu Public link](https://public.tableau.com/views/FinancialSummaryDashboard_17067355428040/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link)")
	col10,col11,col12 = st.columns(3)
	with col10:
		with st.container():
			st.header("Machine Learning")
			st.image("hugging_face.jpg")
			st.write("""Used Python and Hugging Face models for text-classification. Image credit to blog.tensorflow.org """)
			st.write("[Repo link](https://colab.research.google.com/drive/1galDfsylNzf5CRqxZU-0UWgF0FYcsJDf?usp=sharing)")
	with col11:
		with st.container():
				st.header("Visualization")
				st.image("nyc_area.png")
				st.write(""" Analyzed covid 19 data in R and tested relevant hypotheses, practiced applying linear modeling and visualization techniques""")
				
				st.write("[Report link](https://github.com/oohtmeel1/Covid19report/blob/main/covid19datafinalreport.pdf)")
	with col12:
		with st.container():
				st.header("Machine Learning")
				st.image("Screenshot_101227.png")
				st.write("""Predicted Movie Gross using Machine learning, loaded, cleaned and visualized data. Used Scikit learn Linear modeling.""")
				
				st.write("[Report link](https://github.com/oohtmeel1/Competition)")
	

		



# %%
