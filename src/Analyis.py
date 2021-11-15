import pandas as pd
import numpy as np
from src.data_cleaning import rawdatacleaning
import plotly.express as px
from apps.config import Config
import os
from app_logger.logger import applogger


filename = os.path.basename(__file__)


class VisualisationAnalysis(rawdatacleaning):
    def __init__(self):
        self.classname = self.__class__.__name__
        self.file_object = open("logs/operations.txt", 'a+')
        self.logger_object = applogger()

        self.logger_object.log(self.file_object, f'Current Script: {filename}')
        self.logger_object.log(self.file_object, f'Entered the class: {self.classname}')
    #data = pd.read_csv("Data_given\gpscleaned.csv")
    path = os.path.join(Config.DATA_PATH, "gpscleaned.csv")
    data = pd.read_csv(path)

    x_val = data['Installs_New'].groupby(by=data['Category']).sum().sort_values(ascending=False)
    x_rat_cat = data['Rating'].groupby(by=data['Category']).mean().sort_values(ascending=False)
    x_cat_rev = data['Reviews'].groupby(by=data['Category']).sum().sort_values(ascending=False)
    paid_data = data[data.Type == 'Paid']
    paid_cat_install = paid_data['Installs_New'].groupby(by=paid_data['Category']).sum().sort_values(ascending=False)
    paid_rev_cat = paid_data['Reviews'].groupby(by=paid_data['Category']).sum().sort_values(ascending=False)
    install_cr = data['Installs_New'].groupby(by=data['Content Rating']).count().sort_values(ascending=False)

    ## only for generate_label_correlation and generate_matrix_graph functions
    path1 = os.path.join(Config.DATA_PATH, "gpsfinal.csv")
    data1 = pd.read_csv(path1)


    def missing_values(self):
       self.logger_object.log(self.file_object, 'Entered missing_value function') 
       return  np.round(self.data.isnull().mean(), 2)

    def datatype(self):
       self.logger_object.log(self.file_object, 'Entered datatype function')  
       return super().datatype(self.data)

    def categoricalanalysis(self):
        self.logger_object.log(self.file_object, 'Entered categoricalanalysis function')  
        # number of class in each categorical feature
        categorical_feature = [feature for feature in self.data.columns if self.data[feature].dtypes == 'object' and feature not in ['LastUpdated_New', 'Size_New','AndroidVersion_New']]
        d = {}
        for feature in categorical_feature:
            key = "total number of categories in " + feature
            d[key] = self.data[feature].nunique()
        return d
    def highestinstallations(self):
        self.logger_object.log(self.file_object, 'Entered highestinstallations function')  
        fig = px.bar(self.data,x = self.x_val.index,y = self.x_val, color=self.x_val.index)
        return fig
    def avg_CategoryRating(self):
        self.logger_object.log(self.file_object, 'Entered avg_CategoryRating function')  
        #x_rat_cat = self.data['Rating'].groupby(by=self.data['Category']).mean().sort_values(ascending=False)
        fig1 = px.bar(self.data, x=self.x_rat_cat.index, y=self.x_rat_cat.values, color=self.x_rat_cat)
        fig2 = px.bar(self.data, x=self.x_val.head(10).index, y=self.x_rat_cat[self.x_val.head(10).index], color=self.x_val.head(10).index)
        return fig1,fig2
    def max_reviews(self):
        self.logger_object.log(self.file_object, 'Entered max_reviews function')  
        #self.x_cat_rev = self.data['Reviews'].groupby(by=self.data['Category']).sum().sort_values(ascending=False)
        fig = px.bar(self.data, x=self.x_cat_rev.index, y=self.x_cat_rev.values, color=self.x_cat_rev.index)
        return fig
    def highestinstalled_highestreviews(self):
        self.logger_object.log(self.file_object, 'Entered highestinstalled_highestreviews function')  
        fig = px.bar(self.data, x=self.x_cat_rev[self.x_val.head(10).index].index, y=self.x_cat_rev[self.x_val.head(10).index].values,
               color=self.x_cat_rev[self.x_val.head(10).index].index)
        return fig
    def paid_categories(self):
        self.logger_object.log(self.file_object, 'Entered paid_categories function')  
        #self.paid_data = self.data[self.data.Type == 'Paid']
        fig = px.bar( self.paid_data, x= self.paid_data['Category'].value_counts().index, y= self.paid_data['Category'].value_counts().values,
               color= self.paid_data['Category'].value_counts().index)
        return fig
    def highest_paid_installed(self):
        self.logger_object.log(self.file_object, 'Entered highest_paid_installed function')
        #paid_cat_install = self.paid_data['Installs_New'].groupby(by=self.paid_data['Category']).sum().sort_values(ascending=False)
        fig = px.bar(self.paid_data, x=self.paid_cat_install.index, y=self.paid_cat_install.values, color=self.paid_cat_install)
        return fig
    def paid_highestrating(self):
        self.logger_object.log(self.file_object, 'Entered paid_highestrating function')
        fig = px.bar(self.paid_data, x=self.paid_data['Rating'].groupby(by=self.paid_data['Category']).mean().sort_values().dropna().index,
               y=self.paid_data['Rating'].groupby(by=self.paid_data['Category']).mean().sort_values().dropna().values,
               color=self.paid_data['Rating'].groupby(by=self.paid_data['Category']).mean().sort_values().dropna().index)
        return fig
    def highestReviews_paid(self):
        self.logger_object.log(self.file_object, 'Entered highestReviews_paid function')
        #paid_rev_cat = self.paid_data['Reviews'].groupby(by=self.paid_data['Category']).sum().sort_values(ascending=False)
        fig = px.bar(self.paid_data, x=self.paid_rev_cat.index, y=self.paid_rev_cat.values, color=self.paid_rev_cat.index, text=self.paid_cat_install)
        return fig
    def contentrating_highestinstall(self):
        self.logger_object.log(self.file_object, 'Entered contentrating_highestinstall function')
        #install_cr = self.data['Installs_New'].groupby(by=self.data['Content Rating']).count().sort_values(ascending=False)
        fig = px.bar(self.data, x=self.install_cr.index, y=self.install_cr.values, color=self.install_cr.index)
        return fig

    def temp_df(self):
        self.logger_object.log(self.file_object, 'Entered temp_df function')
        self.data_fixedSize = self.data[self.data['Size_New'] != 'Varies with device']
        self.data_fixedSize['Size_New'] = self.data_fixedSize['Size_New'].astype(float)
        return self.data_fixedSize['Size_New'].min(),self.data_fixedSize['Size_New'].max()
    def size_apps(self,app_size=67000):
        self.logger_object.log(self.file_object, 'Entered size_apps function')
        app_number = self.data_fixedSize[self.data_fixedSize['Size_New'] > app_size]['Size_New'].groupby(by=self.data_fixedSize['Category']).count().sort_values(ascending=False)
        fig = px.bar(self.data_fixedSize, x=app_number.index, y=app_number.values, color=app_number.index)
        return fig

    def generate_matrix_graph(self,chosen_method, graph_matrix):
        self.logger_object.log(self.file_object, 'Entered generate_matrix_graph function')
        if graph_matrix == 'Matrix':
            try:
                matrix = self.data1.corr(method=chosen_method)
            except Exception as e:
                matrix = "Matrix cant be generated"
            finally:
                return matrix
        else:
            fig = px.imshow(self.data1.corr(method=chosen_method))
            return fig

    def generate_label_correlation(self,chosen_method,label):
        self.logger_object.log(self.file_object, 'Entered generate_label_correlation function')
        matrix = self.data1.corr(method=chosen_method)[label]
        write =  self.data1.corr(method=chosen_method)[[label]].sort_values(by=label, ascending=False)
        fig = px.imshow(write)
        return matrix,fig




