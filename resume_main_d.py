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


sideb = st.sidebar
st.sidebar.image("https://drive.google.com/uc?export=view&id=1udI3U3LLKbZBKp4LLh-dRteKGP6C-lpp",width=50)

st.sidebar.markdown('<p class="big-font">Agnes McFarlin</p>',unsafe_allow_html=True)
st.sidebar.write("Enjoyer of science in all forms.")

st.sidebar.link_button("Github", "https://github.com/oohtmeel1")
check1 = sideb.button('Introduction')
check2 = sideb.button('Projects')
check3 = sideb.link_button("Resume", "https://drive.google.com/file/d/1i3PxOibjfFDwH6j4DgPT7Och_3SMi2Q0/view?usp=sharing")

if check1:
	st.header("""About : """)
	st.markdown('''<img src="https://drive.google.com/uc?export=view&id=1VNyLiC2GQSonzXvbmRL7KO_mfuBQZP3S"
 	alt="foo" width=300, height=300 /> <p class="little-big">While my career started out with me working in wet labs as a Chemist, 
	performing various chemical and biochemical tests, and working with a 
	variety of instruments.
  	I always enjoyed poring over the massive amounts of data that
   	were generated during the course of some interval by work processes. From tracking protein concentration changes over time, 
	and communicating those changes during meetings, or tracking samples sent for outside 
	testing to ensure timelines were being met, the Data Science portion 
	of my various jobs has always interested me. So, in pursuit of furthering my career 
	interest with such activities, I have been diligently self-studying programming 
	and am nearing completion of a Master’s program in Data Science at the 
	University of Colorado.I have gained experience using Python and R with a 
	variety of tasks. Cleaning, parsing, otherwise working with numerical and text data. 
	Visualizing said data using various libraries and techniques and even some machine 
	learning using Scikit learn, Tensorflow and Hugging Face. I am excited to apply my skills and 
	knowledge with new opportunities.</p>''',unsafe_allow_html=True)	
	
  
  
if check2:

	st.title('Projects:bar_chart:')
	st.markdown('''<p class="little-big"> Some Python, some R, a lot of data.</p>''',unsafe_allow_html=True)
	col1, col2, col3 = st.columns(3)
	with col1:
		expander = st.expander("Statistical analysis of PLACES datasets")
		expander.image('''https://drive.google.com/uc?export=view&id=1P8axquXzPg4ixflLtHXs69GZQb5dygUZ''')
		expander.write('''
				 Used python, scipy stats, performed distribution fitting,correlation analysis, outlier analysis parametric and non parametric testing and discussed results.''')
		expander.write("[Project Link](https://github.com/oohtmeel1/Data_Mining_complete/)")
	with col2:
		expander = st.expander("Python Project Performing Text classification of twitter data to create networks")
		expander.image('''https://drive.google.com/uc?export=view&id=1ftTe2PDoBL0OkSt7y4jKNvH_Lrl61Vfi''')
		expander.write('''
				 Used Python, NLTK, Seaborn and NetworkX to create directed and undirected graphs of text data''')
		expander.write("[Project Link](https://colab.research.google.com/drive/15An1jxoNVKclHzFsV58FiIrUrW3nS47T?usp=sharing/)")
	with col3:
		expander = st.expander("Python Project Visualizing Budgetary and Geospatial Data")
		
		expander.image('''https://drive.google.com/uc?export=view&id=13A2rY23cm1q8_AAOPf_1CYDVruJbNITp''')
		expander.write('''
				 Used Python, Folium, Branca and other libraries in order to display and visualize Geospatial and finanacial data. Deployed app in streamlit''')
		expander.write("[Project Link](https://oohtmeel1-coloradobouldervisalizations-my-app-final-j5ndhy.streamlit.app/)")
	

	

  

	col4,col5,col6 = st.columns(3)
	with col4:
		expander = st.expander("Python Project for species categorization using Kmeans clustering.")
		expander.image('''https://drive.google.com/uc?export=view&id=1V9JVQvpRM32CueFh3TR1kRuZyIsnOvTu''')
		expander.write("""A project using Python and K-means Unsupervised 
				 learning in order to categorize bird species based on skeletal structure.""")		
		expander.write("[Repo link](https://github.com/oohtmeel1/Unsup2/tree/main)")
		expander.write("[Final Notebook](https://github.com/oohtmeel1/Unsup2/blob/main/Kmeans_Report.ipynb/)")
	with col5:
		expander = st.expander("Implementing a Bidirectional LSTM for tweet classification.")
		expander.image('''https://drive.google.com/uc?export=view&id=14tvQGTj3ZJT_70Fbv7Zyxz1Fs4z7wW0G''')
		expander.write("""Text categorization using Python, and a Bidirectional LSTM, to categorize tweets into Disaster or Not Disaster categories .""")
		expander.write("[Final Notebook](https://github.com/oohtmeel1/Disaster_tweets/blob/main/notebooke20b826a34%20(4).ipynb)")
		expander.write("[Repo link](https://github.com/oohtmeel1/Disaster_tweets/tree/main)") 
	with col6:
		expander = st.expander("Cancer detection using a Convolutional Neural Network")
		expander.write("[Repo link](https://github.com/oohtmeel1/Week3DeepLearning)")
		expander.image('''https://drive.google.com/uc?export=view&id=1lbHl86hb7wLYRN4KA4lCC_6j-mQpQP_7''')
		expander.write("""In python used Keras and tensorflow to classify medical images as being malignant or benign using a CNN. """)
 
	col7,col8,col9 = st.columns(3)
	with col7:
		expander = st.expander("Text categorization using news data and a variety of models")
		expander.write("[Notebook link](https://github.com/oohtmeel1/Unsup_learning/blob/main/Report_A.ipynb)")
		expander.image('''https://drive.google.com/uc?export=view&id=1fzRKB3-st7p44RwW6xvvXCXu73B8BEis''')
		expander.write("""In python compared unsupervised and supervised learning using different model types. """)   
	with col8:
		expander = st.expander("Project using Machine learning for Image classification")
		expander.image('''https://drive.google.com/uc?export=view&id=18FfgN71yMiFlZBapGRIQjbb9RLH-lqU0''')
		expander.write("[Repo link](https://github.com/oohtmeel1/Deep_Learning_Final)")
		expander.write("""Using a CNN model to perform image classification in Python using tensorflow and Keras. """)	
	with col9:
		expander = st.expander("Supervised learning sentiment analysis on text data")
		expander.image('''https://drive.google.com/uc?export=view&id=1PYBIaIQIwdzfEVBwvQxpxdpkeVm4bfEB''')
		expander.write("[Repo link](https://github.com/oohtmeel1/Supervised_learning_project)")
		expander.write(""" Cleaned and manually labelled enron email dataset in order to perform sentiment analysis in Python using Vader  sentiment analysis and SVM.""")
	
	col10,col11,col12 = st.columns(3)
	with col10:
		expander = st.expander("Text Classification with distilroberta-base")
		expander.image('''https://drive.google.com/uc?export=view&id=1peKSc20h87VDg220_y5PxeFuiVjmlxfb''')
		expander.write("[Repo link](https://colab.research.google.com/drive/1galDfsylNzf5CRqxZU-0UWgF0FYcsJDf?usp=sharing)")
		expander.write(""" Used hugging face models for text classification. Image credit to blog.tensorflow.org """)
	
	with col11:
		expander = st.expander("Early coding practice")
		expander.image('''https://drive.google.com/uc?export=view&id=1R9ssAVKkZQh1YzwHAWhJysGFYXrzxKfM''')
		expander.write("[Repo link](https://github.com/oohtmeel1/University-of-Michigan-Data-science)")
		expander.write(""" Practiced modeling, recursion, using libraries such as Seaborn and Pandas.""")
	with col12:
		expander = st.expander("A project analyzing Covid 19 data")
		expander.write("[Report link](https://github.com/oohtmeel1/Covid19report/blob/main/covid19datafinalreport.pdf)")
		expander.write(""" Analyzed covid 19 data in R and tested relevant hypotheses, practiced applying linear modeling and visualization techniques""")	
	col13,col14,col15 = st.columns(3)
	with col13:
		expander = st.expander("Review, analysis and recomendations for data")
		expander.image('''https://drive.google.com/uc?export=view&id=1j-MYyXLK26zsCcoLRd6SqOF1V_Sr23zY''')
		expander.write("[Repo link](https://github.com/oohtmeel1/Review_NYC_data_project)")
		expander.write(""" Reviewed previously performed project and made reccomendations for improvements in R. Image credit to capturetheatlas.com""") 
 
	with col14:
		expander = st.expander("Project analyzing a large amount of population data in R")
		expander.image('''https://drive.google.com/uc?export=view&id=1UFI90bKoiFgJah3_EZTL3DwSM8Rlpu65''')
		expander.write("[Repo link](https://github.com/oohtmeel1/Project_For_Data_Visualization)")
		expander.write("""In R worked with a large data file consiting of mixed data types, interpreted and visualized results. """)	

if  check1 or check2 or check3:
    st.markdown("Stuff goes here")
  


	

		



# %%
