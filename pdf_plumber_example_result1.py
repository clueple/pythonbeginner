"""step 1 import related packages"""
import re
import pdfplumber as pp 
import requests
from io import BytesIO
import pandas as pd

"""specify target url that contains the table(s) you wanna fetch"""
target_url = r'https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2sch100/t2sch100-20e.pdf'

""" Get response from the target url  """
req = requests.get(target_url)
""" turn the req into source bytes for pdfplumber to read  """
source_byte = BytesIO(req.content)
""" Create a pdf object to read the source_byte   """
pdf = pp.open(source_byte)
""" specify the page that contains the table(s) we want to extract"""
page = pdf.pages[1]
""" create the table object to hold all the tables in that page  """
tables = page.extract_tables()

""" Let's say if we need to extract the first table """
table1 = tables[0]

"""  Define the column heads and data rows  for table1  """
column_heads = table1[1]
table1_data = table1[2:]

#create a dataframe, df, to
df = pd.DataFrame(table1_data, columns = column_heads)
df['Field code'] = df['Field code'].astype('int32')

output_file = r'g:/my_csv.csv'

#export table1 to csv
df.to_csv(output_file)

"""trial print """
print(df.dtypes)



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
