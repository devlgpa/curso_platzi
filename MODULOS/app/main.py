import utils
import read_csv
import charts

def run():

    data = read_csv.read_csv('./MODULOS/app/data.csv')

    names, values = utils.world_population_percentage(data)

    charts.generate_pie_chart(names, values)

    """countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))

    charts.generate_pie_chart(countries, percentages)"""

    """country = input("Type the country name: ")

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        
        country = result[0]

        keys, values = utils.get_population(country)
        charts.generate_bar_chart(keys, values)
    else:
        print("Country not found")

    print(result)"""

#si el main es ejecutado desde la terminal y se ejecuta el run
if __name__ == "__main__":
    run()