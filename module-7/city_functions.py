

def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f" - language {language}"
    return result

print(city_country("london", "england",))
print(city_country("paris", "france", 200000))
print(city_country("tokyo", "japan", 400000, "japanese"))