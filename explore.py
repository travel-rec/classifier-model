import pandas as pd 

df = pd.read_csv("./wikivoyage-listings-en.csv")

cities = {}

for a in df['article']:
	if a in cities.keys():
		continue
	cities[a] = 1

distribution = {}
for t in df['type']:
	if t not in distribution.keys():
		distribution[t] = 1
	distribution[t] += 1

def get_data_by_city(city, df):
	start_index = 0
	end_index = 0
	found = False
	for i,a in enumerate(df['article']):
		if city.lower() in a.lower() and not found:
			start_index = i
			found = True
		if found and city.lower() not in a.lower():
			end_index = i
			break
	return df[start_index:end_index]

def slice_by_type(place_type, df):
	type_df = df[df['type'] == place_type]
	return type_df

print(distribution)
ny = get_data_by_city('detroit', df)
print(ny.shape)
ne = slice_by_type('drink', ny)
print(ne.shape)
