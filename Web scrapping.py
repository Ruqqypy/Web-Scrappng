#This library allows you to download historical market data from yahoo finance.
import yfinance as yf

#This library is used for data manipulation and analysis.
import pandas as pd

#This library is used to send HTTP requests to a web server.
import requests 

#A library for parsing HTML and XML documents.
import bs4

#Imported Beautifulsoup from beautifulsoup4(bs4) to navigate,search, and modify HTML documents in a way
#that is easy to understand and manipulate.
from bs4 import BeautifulSoup

#html5lib is a parser that follows the HTML5 specification,but can't be imported directly.
#e.gsoup = BeautifulSoup(response.text,'html5lib')

#A libraray for creating interactive and visually appealing plots and ccharts.
import plotly.graph_objects as go

#A submodule within plotly used for creating subplot layouts.
from plotly.subplots import make_subplots

#The function make_graph
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing =  .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

#Question 1:Use yfinance to Extract Stock Data 
# Using the Ticker function enter the ticker symbol of the stock we want to extract data 
# on to create a ticker object. The stock is Tesla and its ticker symbol is TSLA.

#Using the ticker object and the function history extract stock information and save it in a dataframe 
# named tesla_data. Set the period parameter to "max" so we get information for the maximum amount of time.

#Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame and display 
# the first five rows of the tesla_data dataframe using the head function. Take a screenshot of the 
# results and code from the beginning of Question 1 to the results below.

# Create a ticker object for Tesla
ticker = 'TSLA'
tesla = yf.Ticker(ticker)

# Fetch historical stock data
tesla_data = tesla.history(period='max')


# Reset the index to get the 'Date' column
tesla_data.reset_index(inplace=True)

# Display the first five rows of the dataframe
print(tesla_data.head())



#Question 2:Use Webscraping to Extract Tesla Revenue Data
# Use the requests library to download the webpage 
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-
# SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named html_data.

#Parse the html data using beautiful_soup using parser i.e html5lib or html.parser. 
# Make sure to use the html_data with the content parameter as follow html_data.content .

#Using BeautifulSoup or the read_html function extract the table with Tesla Revenue and store it into a 
# dataframe named tesla_revenue. The dataframe should have columns Date and Revenue.

#Step 1: Download the webpage
url = "http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
response = requests.get(url)
html_data = response.content

#Step 2: Parse the HTML data
soup = BeautifulSoup(html_data,'html5lib')

#Step 3: Extract the Tesla Revenue table using pandas
tables = pd.read_html(html_data)
tesla_revenue = tables[0]
tesla_revenue.columns = ['Date', 'Revenue']

#Step 4: Display the first few rows
print(tesla_revenue.head())


#Question 3: Use yfinance to Extract Stock Data¶
#Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object.
# the stock is GameStop and its ticker symbol is GME.

#Using the ticker object and the function history extract stock information and save it in a dataframe 
#named gme_data. Set the period parameter to "max" so we get information for the maximum amount of time.

#Reset the index using the reset_index(inplace=True) function on the gme_data DataFrame and display the first
#five rows of the gme_data dataframe using the head function. Take a screenshot of the results and code 
#from the beginning of Question 3 to the results below.

# Step 1: Create a ticker object for GameStop
gme = yf.Ticker('GME')

#Step 2: Fetch historical stock data for Gametop
gme_data = gme.history(period = 'max')

#Reset the index to get the Date column as a seperate column.
gme_data.reset_index(inplace=True)

#Display the first five rows of the dataframe
print(gme_data.head())


#Qustion 4:Use Webscraping to Extract GME Revenue Data.
#Use the requests library to download the webpage
#  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN
# -SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named html_data_2.

#Parse the html data using beautiful_soup using parser i.e html5lib or html.parser.

#Using BeautifulSoup or the read_html function extract the table with GameStop Revenue and store it into a
#dataframe named gme_revenue. The dataframe should have columns Date and Revenue. Make sure the comma and 
#dollar sign is removed from the Revenue column.

#Step 1: Download the webpage.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2 = requests.get(url).text

#Parse the HTML data.
soup = BeautifulSoup(html_data_2,"html.parser")

#Extract tables from the parsed HTML.
tables = pd.read_html(str(soup))

#Assuming the table with GameStop revenue is the first one (you may need to adjust the index)
gme_revenue = tables[0]

#Rename the columns to 'Date' and 'Revenue'
gme_revenue.columns = ['Date', 'Revenue'] 

#Display the first few rows
print(gme_revenue.head())


#Remove commas and dollar signs, and convert to numeric.
gme_revenue['Revenue'] = gme_revenue['Revenue'].replace({'\$': '',',': ''}, regex=True)
gme_revenue['Revenue'] = pd.to_numeric(gme_revenue['Revenue'])


#Step 6: Dispaly the cleaned dataframe
print(gme_revenue.head())

#Question 5: Plot Tesla Stock Graph
#Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph. 
#Note the graph will only show data upto June 2021.

#Plot the Tesla stock and revenue data.


