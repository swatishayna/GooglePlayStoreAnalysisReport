import streamlit as st
from src import transformtraindata
import gzip, pickle, pickletools
import numpy as np


def run():
    st.subheader("Google Play Store Rating Prediction App")



    #['Category NUM', 'Reviews', 'Size', 'Installs', 'Price', 'Content Rating NUM']
    data = transformtraindata.get_data('transform')
    dict_category = transformtraindata.generate_dictionary(data)[0]
    dict_content_rating =transformtraindata.generate_dictionary(data)[1]

    # inputs
    Category = st.selectbox("Input the category of the Android Application", dict_category.keys())
    Reviews = st.number_input("Input the number of Reviews recieved", min_value=0,max_value=128)
    Size = st.number_input("Input the size of the application", min_value=8.5, max_value=100000.0)
    Installs = st.number_input("Input the number of Insatllations of the application", min_value=0, max_value=1000000000)
    Price = st.number_input("Input the Price of the application in $", min_value=0, max_value=123)
    Content_Rating = st.selectbox("Input the Content Rating of the android application",dict_content_rating.keys())
    submit = st.button('Predict')
    if submit:
        input_list = [dict_category[Category],Reviews,Size,Installs,Price,dict_content_rating[Content_Rating]]
        input_list = np.array(input_list).reshape(1, -1)
        #load model
        # loading the stored model for prediction
        with gzip.open('random_forest.pkl', 'rb') as f:
            p = pickle.Unpickler(f)
            model = p.load()
        output = model.predict(input_list)
        if output:
            st.write("The predicted rating for this android application is")
            st.header(output)