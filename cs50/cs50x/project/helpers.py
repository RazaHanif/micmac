""" use this for the api stuff and any functions i gotta make to keep it kinda hidden i guess """


import requests, json, time


# Default vin number for testing
def vinDecode(v="2T1BURHE1FC382765"):

    # using the nhtsa extended vin decoder
    decodeVinExtended = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINExtended/"
    vin = v
    url = decodeVinExtended + vin + "?format=json"

    # Just combined all these lines into 1 below, leaving it for myself to look back and refrence later
    # vinERes = requests.get(url)
    # vinJson = vinERes.json()
    # make = vinJson["Results"]
    vinDetail = requests.get(url).json()["Results"]

    # Alittle logic so it only prints out valid api responses
    # if its an invalid reponse prints out the error
    if vinDetail[1]["Value"] == "0":
        print(vinDetail[10]["Value"],
            vinDetail[7]["Value"].title(),
            vinDetail[9]["Value"].title(),
            vinDetail[13]["Value"])
    else:
        print(vinDetail[4]["Value"])

    # used for developing to save the json data into a txt file
    # with open('SampleJsonCorolla.txt', 'w') as vinText:
    #   json.dump(vinERes.text, vinText, ensure_ascii=False)

# main logic for the temp cli interface
def main():
    print("********************")
    print("Vin Decoder")

    while True:

        print("********************")
        vin = input("Please Enter a VIN: ")

        vinDecode(vin)
        time.sleep(1)

        run = input("Exit - 0 | Continue - Any Key: ")

        if run == "0":
            break

    print("********************")
    print("---Thank you for using Vin Decoder---")
    print("********************")

# bruh 
main()
