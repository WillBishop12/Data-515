#Homework 2 - Data 515 - Will Bishop

import sqlite3
import pandas as pd

def create_dataframe(fp):
	#From https://www.dataquest.io/blog/python-pandas-databases/
	conn = sqlite3.connect(fp)
	#Query from HW 1
	return pd.read_sql_query("SELECT video_id, category_id, 'ca' AS language FROM CAvideos UNION SELECT video_id, category_id, 'de' AS language FROM DEvideos UNION SELECT video_id, category_id, 'fr' AS language FROM FRvideos UNION SELECT video_id, category_id, 'gb' AS language FROM GBvideos UNION SELECT video_id, category_id, 'us' AS language FROM USvideos;", conn)

def test_create_dataframe(df):
	assert len(df.columns) == 3
	assert all(x in df.columns for x in ['video_id', 'category_id', 'language'])
	assert len(df.groupby(['video_id', 'language']).count()) == len(df)
	assert len(df) > 9
	return True
	print("Test passed")