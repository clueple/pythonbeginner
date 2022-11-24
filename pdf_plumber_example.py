"""step 1 import related packages"""
import re
import pdfplumber as pp 
import requests
from io import BytesIO
import pandas as pd

"""specify target url that contains the table(s) you wanna fetch"""


"""trial print """


"""create function to fetch individual table from target url"""
def fetch_table(url:str):
	pass

"""define the fields / column heads of each table"""
column_head = "field"
"""define the data (rows of data) for each table"""
data = "row data"

"""In each table, create a DataFrame object (this is a table) to store the column heads and data; name it the table 1, 2, 3, and so on"""
table1 = 'table1'
table2 = 'table2'
table3 = 'table3'


"""a smarter approach to get multiple tables"""



"""save individual tables to csv"""
