import pandas as pd 

df = pd.read_csv("./wikivoyage-listings-en.csv")

print(df.shape)
print(df.columns)

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

print(len(cities.keys()))
print(distribution)

def get_data_by_city(city):
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

ny = get_data_by_city('new york city')

print(ny.head)