"""
Temp logic to find close by mechanic/dealers shops for your car

use geocoder to get location of ip

then use serpapi api to get local results for shops to go to

"search_parameters":{
    "engine":"google_maps",
    "type":"search",
    "q":"{make} mechanic",
    "ll":"@43.73126608994001, -79.76642082976853,14z",
    "google_domain":"google.com",
    "hl":"en"
},

https://serpapi.com/search.json?
engine=google_maps
&q=bmw+mechanic
&ll=%4043.73126608994001%2C+-79.76642082976853%2C14z
&google_domain=google.com
&hl=en
&type=search

"""

# from serpapi import GoogleSearch
import geocoder


g = geocoder.ip('me')
print(f"@{g.latlng[0]},{g.latlng[1]},14z")


# Api request
"""
    search_q = make + "mechanic"
    params = {
    "engine": "google_maps",
    "q": search_q,
    "ll": f"@{g.latlng[0]},{g.latlng[1]},14z",
    "type": "search",
    "api_key": "b5f82c259820b48147c2336bfa9548aed8656cdb474307391320f67fa6e747ec"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    local_results = results["local_results"]
"""


# Sample repsonse from serpapi api to get local results for BMW mechanics
response = {
    "search_metadata":
    {
        "id":"656415877690dcb655e95c15",
        "status":"Success",
        "json_endpoint":"https://serpapi.com/searches/f3245eba43eb16f1/656415877690dcb655e95c15.json",
        "created_at":"2023-11-27 04:05:27 UTC",
        "processed_at":"2023-11-27 04:05:27 UTC",
        "google_maps_url":"https://www.google.com/maps/search/bmw+mechanic/@43.73126608994001,-79.76642082976853,14z?hl=en",
        "raw_html_file":"https://serpapi.com/searches/f3245eba43eb16f1/656415877690dcb655e95c15.html",
        "total_time_taken":0.88
    },
    "search_parameters":
    {
        "engine":"google_maps",
        "type":"search",
        "q":"bmw mechanic",
        "ll":"@43.73126608994001, -79.76642082976853,14z",
        "google_domain":"google.com",
        "hl":"en"
    },
    "search_information":
    {
        "local_results_state":"Results for exact spelling",
        "query_displayed":"bmw mechanic"
    },
    "local_results":
    [
        {
            "position":1,
            "title":"Policaro BMW Service",
            "place_id":"ChIJaYTFiWoXK4gRUg87AnzdvI0",
            "data_id":"0x882b176a89c58469:0x8dbcdd7c023b0f52",
            "data_cid":"10213281579652550482",
            "reviews_link":"https://serpapi.com/search.json?data_id=0x882b176a89c58469%3A0x8dbcdd7c023b0f52&engine=google_maps_reviews&hl=en",
            "photos_link":"https://serpapi.com/search.json?data_id=0x882b176a89c58469%3A0x8dbcdd7c023b0f52&engine=google_maps_photos&hl=en",
            "gps_coordinates":
            {
                "latitude":43.7587858,
                "longitude":-79.7934602
            },
            "place_id_search":"https://serpapi.com/search.json?engine=google_maps&google_domain=google.com&hl=en&place_id=ChIJaYTFiWoXK4gRUg87AnzdvI0",
            "provider_id":"/g/11r8ydz246",
            "rating":3.7,
            "reviews":13,
            "type":"Auto repair shop",
            "types":
            [
                "Auto repair shop",
                "Auto restoration service",
                "BMW dealer"
            ],
            "address":"5 Coachworks Cres, Brampton, ON L6R 3Y2, Canada",
            "open_state":"Closed ⋅ Opens 8 AM Mon",
            "hours":"Closed ⋅ Opens 8 AM Mon",
            "operating_hours":
            {
                "sunday":
                "Closed",
                "monday":
                "8 AM–5 PM",
                "tuesday":
                "8 AM–5 PM",
                "wednesday":
                "8 AM–5 PM",
                "thursday":
                "8 AM–5 PM",
                "friday":
                "8 AM–5 PM",
                "saturday":
                "8 AM–4 PM"
            },
            "phone":"+1 416-981-9400",
            "website":"https://www.policarobmw.ca/",
            "thumbnail":"https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=jlFxYogJTgu82sw0HpE-7g&cb_client=search.gws-prod.gps&w=80&h=92&yaw=151.03592&pitch=0&thumbfov=100"
        },
        {
            "position":2,
            "title":"Bimmersport Automotive Inc",
            "place_id":"ChIJkY1Laxs_K4gRkBgSv6Xxnk0",
            "data_id":"0x882b3f1b6b4b8d91:0x4d9ef1a5bf121890",
            "data_cid":"5593173481418266768",
            "reviews_link":"https://serpapi.com/search.json?data_id=0x882b3f1b6b4b8d91%3A0x4d9ef1a5bf121890&engine=google_maps_reviews&hl=en",
            "photos_link":"https://serpapi.com/search.json?data_id=0x882b3f1b6b4b8d91%3A0x4d9ef1a5bf121890&engine=google_maps_photos&hl=en",
            "gps_coordinates":
            {
                "latitude":43.659698399999996,
                "longitude":-79.6806411
            },
            "place_id_search":"https://serpapi.com/search.json?engine=google_maps&google_domain=google.com&hl=en&place_id=ChIJkY1Laxs_K4gRkBgSv6Xxnk0",
            "provider_id":"/g/1tdylvl3",
            "rating":4.4,
            "reviews":138,
            "type":"Auto repair shop",
            "types":
            [
                "Auto repair shop"
            ],
            "address":"6780 Pacific Cir Unit #3, Mississauga, ON L5T 1N8, Canada",
            "open_state":"Closed ⋅ Opens 9 AM Mon",
            "hours":"Closed ⋅ Opens 9 AM Mon",
            "operating_hours":
            {
                "sunday":
                "Closed",
                "monday":
                "9 AM–5:30 PM",
                "tuesday":
                "9 AM–5:30 PM",
                "wednesday":
                "9 AM–5:30 PM",
                "thursday":
                "9 AM–5:30 PM",
                "friday":
                "9 AM–5:30 PM",
                "saturday":
                "Closed"
            },
            "phone":"+1 905-670-9200",
            "website":"http://www.bimmersport.ca/",
            "thumbnail":"https://lh5.googleusercontent.com/p/AF1QipOZzyr2I0NidSiA_KG2xc2EC0ghAckSByAQviVX=w87-h92-k-no"
        },
        {
            "position":3,
            "title":"RMP Motors - BMW Specialists",
            "place_id":"ChIJQ_T0bhc7K4gR2PtTCoxdhKk",
            "data_id":"0x882b3b176ef4f443:0xa9845d8c0a53fbd8",
            "data_cid":"12214990945385708504",
            "reviews_link":"https://serpapi.com/search.json?data_id=0x882b3b176ef4f443%3A0xa9845d8c0a53fbd8&engine=google_maps_reviews&hl=en",
            "photos_link":"https://serpapi.com/search.json?data_id=0x882b3b176ef4f443%3A0xa9845d8c0a53fbd8&engine=google_maps_photos&hl=en",
            "gps_coordinates":
            {
                "latitude":43.753441099999996,
                "longitude":-79.6175571
            },
            "place_id_search":"https://serpapi.com/search.json?engine=google_maps&google_domain=google.com&hl=en&place_id=ChIJQ_T0bhc7K4gR2PtTCoxdhKk",
            "provider_id":"/g/1tcxdv9k",
            "rating":4.8,
            "reviews":306,
            "type":"Auto repair shop",
            "types":
            [
                "Auto repair shop",
                "Racing car parts store"
            ],
            "address":"12 Goodmark Pl #2, Etobicoke, ON M9W 6R1, Canada",
            "open_state":"Closed ⋅ Opens 8:30 AM Mon",
            "hours":"Closed ⋅ Opens 8:30 AM Mon",
            "operating_hours":
            {
                "sunday":
                "Closed",
                "monday":
                "8:30 AM–5 PM",
                "tuesday":
                "8:30 AM–5 PM",
                "wednesday":
                "8:30 AM–5 PM",
                "thursday":
                "8:30 AM–5 PM",
                "friday":
                "8:30 AM–4 PM",
                "saturday":
                "Closed"
            },
            "phone":"+1 416-679-0302",
            "website":"https://www.rmpmotors.com/",
            "thumbnail":"https://lh5.googleusercontent.com/p/AF1QipOjPmFz4yv6rZJtboE3EqtpKmBrVGtYR-NxkI7g=w122-h92-k-no"
        }
    ],
    "serpapi_pagination":
    {
    "next":"https://serpapi.com/search.json?engine=google_maps&google_domain=google.com&hl=en&ll=%4043.73126608994001%2C+-79.76642082976853%2C14z&q=bmw+mechanic&start=20&type=search"
    }
}

local_res = response["local_results"]

for n in range(len(local_res)):
    print(f"{local_res[n]["title"]} -- {local_res[n]["open_state"]}")
