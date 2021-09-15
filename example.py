from searchdata import SearchdataLocations, SearchdataGoogleSearch

searchdataGoogleSearch = SearchdataGoogleSearch('YOUR_API_KEY')
locationsAPI = SearchdataLocations()

response = locationsAPI.execute("Austin", 1)
locations = response.json()
location = locationsAPI.process_location(locations[0])
searchdataGoogleSearch.set_q("Test")
searchdataGoogleSearch.set_location(location)
searchdataGoogleSearch.set_lr('lang_en|lang_ar')
response = searchdataGoogleSearch.execute()

# print(response.status_code)
# print(response.headers);
print(response.json());