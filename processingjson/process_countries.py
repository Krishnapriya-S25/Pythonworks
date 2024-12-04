from json import load

f=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\countries.json",encoding="utf-8")

data=load(f)

#print number of countries
# print(len(data))

all_countries_names=[country.get("name")for country in data]

# print(all_countries_names)

#print all regions

all_regions=[country.get("region")for country in data]
# print(set(all_regions))

region_count={region:all_regions.count(region)for region in all_regions}
# print(region_count)


max_region_count=max(region_count,key=lambda k:region_count.get(k))
# print(max_region_count)

#capital of a india
capital=[country.get("capital")for country in data if country.get("name")=="India"]
# print(capital)

#countries with most number of borders



country_border_count={country.get("name"):len(country.get("borders",[ ])) for country in data}
# print(country_border_count)

#most population

most_population=max(data,key=lambda country:country.get("populaion",0)).get("name")
# print(most_population)

#name of the countries border in which sharing with india

# countries_border=[country.get("borders") for country in data if country.get("name")=="India"]

# for border in country_borders:

aplfa_three_codes=[country.get("borders") for country in data if country.get("name")=="India"][0]
for code in aplfa_three_codes:
    for country in data:
        if country.get("alpha3Code")==code:
            print(country.get("name"))










