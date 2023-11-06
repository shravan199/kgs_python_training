import numpy as np
import pandas as pd
import pymysql
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


connection = pymysql.connect("localhost", "nishant", "1234", "moviereviews")
ds = pd.read_sql_query("SELECT * from movies_movies", connection)

def getFrames(ds):
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 5),
                        min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(ds['title'])

    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    results = {}

    for idx, row in ds.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], ds['id'][i])
                        for i in similar_indices]

        results[row['id']] = similar_items[1:]
    return results


results=getFrames(ds)
print(results)





















# # import mysql.connector
# # 
# # mydb = mysql.connector.connect(
# #   host="localhost",
# #   user="root",
# #   passwd="1234"
# # )
# # 
# # print(mydb)
# # mycursor = mydb.cursor()
# import pymysql
# 
# mydb = pymysql.connect("localhost", "nishant", "1234", "moviereviews")
# mycursor = mydb.cursor()
# # mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
# # 
# # mycursor = mydb.cursor()
# # 
# mycursor.execute("SHOW DATABASES")
#  
# for x in mycursor:
#   print(x)