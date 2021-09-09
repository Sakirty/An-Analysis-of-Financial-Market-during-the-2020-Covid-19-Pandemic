import yfinance as yf
from datetime import date
#https://pypi.org/project/yfinance/
#https://algotrading101.com/learn/yfinance-guide/
import sys
import pandas as pd
#file.to_csv(r'/content/drive/My Drive/5523/Proj1/E5/titanic/MendieWoAlive1.csv',index=False)

file_f = open("clean_500.csv", "r") # open the cleaned Sp500 list, note all in here are uppercase
for lines in file_f: #str
    try:
        lines = lines.strip("\n")
        stock = yf.Ticker(lines)
        addr = "stocks/"+str(lines)+".csv"
        #output = open("stocks/"+str(lines)+".csv", "a")
        #print(stock.history(start="2020-01-01",end = "2020-01-07"))
        #print(type(stock.history(start="2020-01-01",end = "2020-01-07")))
        output_file = stock.history(start="2020-01-01",end = "2020-01-03")
        output_file.to_csv(addr)
    except:
        missing = open("missing.csv", "a")
        file_f.write(lines)
        file_f.write("\n")
        
#msft = yf.Ticker("MSFT")
#print(msft.history(start="2020-01-01",end = "2020-01-07")) #get from date between, does not include these 2 dates
'''try:
    print(msft.info)
except:
    print("nodata")'''