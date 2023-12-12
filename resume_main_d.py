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
st.sidebar.image("https://drive.google.com/uc?export=view&id=1udI3U3LLKbZBKp4LLh-dRteKGP6C-lpp",width=50)

st.sidebar.markdown('<p class="big-font">Agnes McFarlin</p>',unsafe_allow_html=True)
st.sidebar.write("Enjoyer of science in all forms.")
st.sidebar.link_button("Github", "https://github.com/oohtmeel1")
check1 = sideb.button('Introduction')
check2 = sideb.button('Projects')
check3 = sideb.link_button("Resume", "https://drive.google.com/file/d/1i3PxOibjfFDwH6j4DgPT7Och_3SMi2Q0/view?usp=sharing")


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
		cola, colb, colc,cold = st.columns(4)
		with cola:
			st.markdown('Python')
			st.image("""https://drive.google.com/uc?export=view&id=1dMATOGMzG4V6T0PPUCA0WmW7WQD5Vval""")
			st.markdown("- loading and cleaning structured and unstructured data.")
			st.markdown("- statistical analyis")
			st.markdown("- Machine Learning")
			st.markdown("- visualization of results")
		with colb:
			st.markdown('R-Studio')
			st.image('''https://drive.google.com/uc?export=view&id=1V_S8xJOXOzG-ohNvtUFiK635gpyXrj8X''')
			st.markdown("- loading and cleaning structured data")
			st.markdown("- statistical analyis")
			st.markdown("- Machine Learning")
			st.markdown("- visualization of results")
		with colc:
			st.markdown('MySQL')
			st.image('''https://drive.google.com/uc?export=view&id=1yO38loXOza6YyjDjWH0pQ-EeuVC59Yvp''')
			st.markdown("- querying data")
			st.markdown("- performing basic data manipulation functions")
		with cold:
			st.markdown('MySQL')
			st.image('''https://drive.google.com/uc?export=view&id=1yO38loXOza6YyjDjWH0pQ-EeuVC59Yvp''')
			st.markdown("- querying data")
			st.markdown("- performing basic data manipulation functions")
  
  
if check2:
	placeholder.empty()
	st.title('Projects:bar_chart:')
	st.markdown('''<p class="little-big"> Some Python, some R, a lot of data.</p>''',unsafe_allow_html=True)
	col1, col2, col3 = st.columns(3)
	with col1:
		with st.container():
			st.header("Statistical analysis ")
			st.image('''https://drive.google.com/uc?export=view&id=1P8axquXzPg4ixflLtHXs69GZQb5dygUZ''')
			st.write('''
					Used PLACES data from the CDC. Analyzed in Python, performed distribution fitting,correlation analysis, outlier analysis 
	 				parametric and non parametric testing and discussed results. Libraries of note: scipy stats, distfit.''')
			st.write("[Project Link](https://github.com/oohtmeel1/Data_Mining_complete/)")
	with col2:
		with st.container():
			st.header("Text classification")
			st.image('''https://drive.google.com/uc?export=view&id=1ftTe2PDoBL0OkSt7y4jKNvH_Lrl61Vfi''')
			st.write('''
					Analyzed Twitter data in Python,  using NLTK, Seaborn and NetworkX to create directed and undirected graphs of text data.''')
			st.write("[Project Link](https://colab.research.google.com/drive/15An1jxoNVKclHzFsV58FiIrUrW3nS47T?usp=sharing/)")
	with col3:
		with st.container():
			st.header("Visualizaton and analysis")
			st.image('''https://drive.google.com/uc?export=view&id=13A2rY23cm1q8_AAOPf_1CYDVruJbNITp''')
			st.write('''
				 Used Python, Folium, Branca and other libraries in order to display and visualize Geospatial and finanacial data.''')
			st.write("[Project Link](https://oohtmeel1-coloradobouldervisalizations-my-app-final-j5ndhy.streamlit.app/)")
	col4,col5,col6 = st.columns(3)
	with col4:
		with st.container():
			st.header("Machine Learning")
			st.image('''https://drive.google.com/uc?export=view&id=1V9JVQvpRM32CueFh3TR1kRuZyIsnOvTu''')
			st.write(""" Used Python and machine learning (K-means)
					in order to categorize bird species based on skeletal structure.""")		
			st.write("[Repo link](https://github.com/oohtmeel1/Unsup2/tree/main)")
			st.write("[Final Notebook](https://github.com/oohtmeel1/Unsup2/blob/main/Kmeans_Report.ipynb/)")
	with col5:
		with st.container():
			st.header("Machine Learning")
			st.image('''https://drive.google.com/uc?export=view&id=14tvQGTj3ZJT_70Fbv7Zyxz1Fs4z7wW0G''')
			st.write("""Text categorization using Python, and a Bidirectional LSTM(RNN), to categorize tweets into Disaster or Not Disaster categories .""")
			st.write("[Repo link](https://github.com/oohtmeel1/Disaster_tweets/tree/main)")
			st.write("[Final Notebook](https://github.com/oohtmeel1/Disaster_tweets/blob/main/notebooke20b826a34%20(4).ipynb)")
	with col6:
		with st.container():
			st.header("Machine Learning")
			st.image('''https://drive.google.com/uc?export=view&id=1lbHl86hb7wLYRN4KA4lCC_6j-mQpQP_7''')
			st.write("""In python used Keras and tensorflow to classify medical images as being malignant or benign using a CNN. """)
			st.write("[Repo link](https://github.com/oohtmeel1/Week3DeepLearning)")
	col7,col8,col9 = st.columns(3)
	with col7:
		with st.container():
			st.header("Machine Learning")
			st.image('''https://drive.google.com/uc?export=view&id=1fzRKB3-st7p44RwW6xvvXCXu73B8BEis''')
			st.write("""In python compared unsupervised and supervised learning using different model types. """)
			st.write("[Notebook link](https://github.com/oohtmeel1/Unsup_learning/blob/main/Report_A.ipynb)")
	with col8:
		with st.container():
			st.header("Machine Learning")
			st.image('''https://drive.google.com/uc?export=view&id=18FfgN71yMiFlZBapGRIQjbb9RLH-lqU0''')
			
			st.write("""In Python used a CNN model to perform image classification on pets. Libraries of note, Tensorflow and Keras """)
			st.write("[Repo link](https://github.com/oohtmeel1/Deep_Learning_Final)")
	with col9:
		with st.container():
			st.header("Machine Learning")
			st.expander("Supervised learning sentiment analysis on text data")
			st.image('''https://drive.google.com/uc?export=view&id=1PYBIaIQIwdzfEVBwvQxpxdpkeVm4bfEB''')
			
			st.write(""" Cleaned and manually labelled enron email dataset in order to perform sentiment analysis in Python using Vader  sentiment analysis and SVM.""")
			st.write("[Repo link](https://github.com/oohtmeel1/Supervised_learning_project)")
	col10,col11,col12 = st.columns(3)
	with col10:
		with st.container():
			st.header("Machine Learning")
			st.image('''https://drive.google.com/uc?export=view&id=1peKSc20h87VDg220_y5PxeFuiVjmlxfb''')
			st.write("""Used Python and Hugging Face models for text-classification. Image credit to blog.tensorflow.org """)
			st.write("[Repo link](https://colab.research.google.com/drive/1galDfsylNzf5CRqxZU-0UWgF0FYcsJDf?usp=sharing)")
	with col11:
		with st.container():
			with col11:
				st.header("Visualization")
				st.image('''https://drive.google.com/uc?export=view&id=1j-MYyXLK26zsCcoLRd6SqOF1V_Sr23zY''')
				st.write(""" Analyzed covid 19 data in R and tested relevant hypotheses, practiced applying linear modeling and visualization techniques""")
				
				st.write("[Report link](https://github.com/oohtmeel1/Covid19report/blob/main/covid19datafinalreport.pdf)")
	

		



# %%
