# LAB_6 Kevin Duffy CISC 215 E31
# Program creates a menu of queries for the StockDb database

#imports
import MySQLdb
buffer = "true"

# Python-MySQL Query Company_Profile Query 1

def CompanyList():
    db = MySQLdb.connect(host="localhost",user="root",passwd="KbdRoot&11",db="StockDb")
    db.query("""SELECT CompanyID,CompanyName,Industry,StockSymbol FROM Company_Profile;""")
    r = db.store_result()
    nR = r.num_rows()
    while(nR > 0):
        print(r.fetch_row())
        nR = nR - 1
db.close()	

# Python-MySQL Query Stock_Ratings Query 1 - Stock Ratings

def StockRatings():
    db = MySQLdb.connect(host="localhost",user="root",passwd="KbdRoot&11",db="StockDb")
    db.query("""SELECT analysts_LastName,InstitutionName,Recommendation FROM Stock_Ratings WHERE StockSymbol = 'PFE';""")
    r = db.store_result()
    nR = r.num_rows()
    while(nR > 0):
        print(r.fetch_row())
        nR = nR - 1
db.close()


# Python-MySQL Query Price_History Query 1 - Closing_Price Volume
def PriceVolume():
    db = MySQLdb.connect(host="localhost",user="root",passwd="KbdRoot&11",db="StockDb")
    db.query("""SELECT CompanyName,Company_Profile.StockSymbol,Closing_Price,Volume,AverageVolume FROM Company_Profile JOIN Price_History ON Company_Profile.StockSymbol = Price_History.StockSymbol;""")
    r = db.store_result()
    nR = r.num_rows()
    while(nR > 0):
        print(r.fetch_row())
        nR = nR - 1
db.close()

while buffer:
    print("""
	0. EXIT
	1. View Company List
	2. View Analyst Recommendations for Pfizer
	3. View Closing Prices and Volume
	""")
	buffer=input("Choose a menu item")
	if buffer == 1:
	    CompanyList()
	if buffer == 2:	
	    StockRatings()
    if buffer == 3:	
        PriceVolume()	
	    
	    