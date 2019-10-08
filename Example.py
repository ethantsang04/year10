import requests

def writeHTML(data):
    myfile = open("myapi.html","w")
    myfile.write("<h1>JSON file returned by API call</h1>")
    myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
    myfile.write(data)
    myfile.close()

def main():
    response = requests.get("https://api.openaq.org/v1/countries")
    if (response.status_code == 200):
        data = response.content
        data_as_str = data.decode()
        writeHTML(data_as_str)

        datajson = response.json()
        countries = datajson['location_country']
        for country in countries:
            print(country)

    else:
        data = "Error has occured"
        writeHTML(data)

main()
