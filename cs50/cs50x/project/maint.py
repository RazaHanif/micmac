"""
Temp logic for maintance page -- don't wanna pay for the carMD api yet
using the refrence responses as a basecase to build the app logic, will extend in webpage
then test proper once I pay for the api

plan is to display upcoming maintenance items and the remaining kms till the service is needed
 """


odo = 50000


# Temp implementation of CarMD Api
response = {
  "message":{...},
  "data":
  [
      {
            "desc":"Inspect For Fluid Leaks",
            "due_mileage":52500,
            "due_km":0,
            "is_oem":True,
            "repair":
            {
                "repair_difficulty":2,
                "repair_hours":0.0,
                "labor_rate_per_hour":106.38,
                "part_cost":6.15,
                "labor_cost":0.0,
                "misc_cost":0.0,
                "total_cost":6.15
            },
            "parts":
            [
                {
                    "desc":"Engine Oil",
                    "manufacturer":"",
                    "price":"6.15",
                    "qty":"1"
                }
            ]
        },
        {
            "desc":"Oil Change",
            "due_mileage":52000,
            "due_km":0,
            "is_oem":True,
            "repair":
            {
                "repair_difficulty":2,
                "repair_hours":0.0,
                "labor_rate_per_hour":106.38,
                "part_cost":6.15,
                "labor_cost":0.0,
                "misc_cost":0.0,
                "total_cost":6.15
            },
            "parts":
            [
                {
                    "desc":"Engine Oil",
                    "manufacturer":"",
                    "price":"6.15",
                    "qty":"1"
                }
            ]
        },
        {
            "desc":"Tire Rotation",
            "due_mileage":53000,
            "due_km":0,
            "is_oem":True,
            "repair":
            {
                "repair_difficulty":2,
                "repair_hours":0.0,
                "labor_rate_per_hour":106.38,
                "part_cost":6.15,
                "labor_cost":0.0,
                "misc_cost":0.0,
                "total_cost":6.15
            },
            "parts":
            [
                {
                    "desc":"Engine Oil",
                    "manufacturer":"",
                    "price":"6.15",
                    "qty":"1"
                }
            ]
        }
    ]
}


for x in range(len(response["data"])):
    print(f"{response["data"][x]["desc"]} in {response["data"][x]["due_mileage"] - odo}kms")
