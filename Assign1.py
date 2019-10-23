import requests
from tkinter import *
import webbrowser
import json
try:
    import httplib
except:
    import http.client as httplib

def writeHTML(datajson,e1,variable):
	ofile = open("climatedata.html", "w")
	ofile.write("<html>")
	ofile.write("<head>")
	ofile.write("<title>Climate Change API</title>")
	ofile.write("<link rel='stylesheet' type='text/css' href='climatedata.css'>")
	ofile.write("</head>")
	ofile.write("<body>")
	ofile.write("<header>")
	ofile.write("<div class='topnav'>")
	ofile.write("<ul>")
	ofile.write("<li><a href='#'>Home</a></li>")
	ofile.write("<li><a href='#'>About</a></li>")
	ofile.write("<li><a href='#'>Cause and Effect</a></li>")
	ofile.write("<li><a href='#'>Solutions</a></li>")
	ofile.write("</ul>")
	ofile.write("</div>")
	ofile.write("<div class='title'")
	ofile.write("<h1><center>Climate Data</center></h1>")
	ofile.write("</div>")
	ofile.write("</header>")
	ofile.write("</body>")
	ofile.write("<br>")
	ofile.write("<h3>Below are the average annual temperatures found by 15 global climate models during the years " + str(e1) + " in " + str(variable) + ":")
	for i in range(15): #lists out all 15 variables for temperatures conducted by different GCMs
		ofile.write("<p>" + str(datajson[i]['annualData'][0]) + "</p>") #json data displayed on html file
	ofile.write("</html>")
	ofile.close()

def getAPI():
	#sends request to internet
	myrequest = requests.get("http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/tas/" + str(variable.get())+ "/" + e1.get() + ".json")
	if (myrequest.status_code == 400):
		print("Error 400", "Error 400 has occured. Client provided incorrect parameters for the request.")
		#error message if improper input
	elif (myrequest.status_code == 200):
		datajson = myrequest.json()
		annual_data = datajson[0]["annualData"] #parsing data
		writeHTML(datajson,variable.get(),e1.get())
		b2 = Button(win,text="view data",command=webbrowser.open("file:///Users/ethan.tsang/Documents/Design/climatedata.html"))
		#Opens html file ^^^
		b2.grid(row=6,column=1)

def internet_on():
        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            conn.close()
            return False	

#tests for wifi
if internet_on():
	#Starts by opening tkinter interface
	win = Tk()
	win.geometry('425x400')
	win.title('type a country code')

	#Heading
	Label_1 = Label(win, text="Enter country(ex//. CAN, USA, etc): ", font="Verdana 18 bold")
	Label_1.grid(row=1,column=2)

	#Entry box for countries
	e1 = Entry(win)
	e1.grid(row=2,column=2)

	Label_2 = Label(win, text="Choose a time interval:", font="Verdana 18 bold")
	Label_2.grid(row=3,column=2)

	#dropdown menu for selecting years
	variable = StringVar(win)
	variable.set("1940/1959")

	w = OptionMenu(win, variable, "1920/1939", "1940/1959", "1960/1979", "1980/1999")
	w.grid(row=4, column=2)

	b1 = Button(win,text="Generate Data!",command=getAPI)
	b1.grid(row=5,column=2)

	mainloop()
else:
	print("Uh oh! You are not connected to the internet.")

