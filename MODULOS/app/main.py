import utils

data = [
        {
        "Country": "Colombia", 
        "Population": 500
        },
        {
        "Country": "Bolivia", 
        "Population": 300
        },
    ]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input("Type the country name: ")

    result = utils.population_by_country(data, country)

    print(result)

#si el main es ejecutado desde la terminal y se ejecuta el run
if __name__ == "__main__":
    run()