
import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader)
        data = []

        for row in reader:
            iterable = zip(headers, row)
            country_dict = {key: value for key, value in zip(headers, row)}
            data.append(country_dict)
        return data

if __name__ == "__main__":
    read_csv('./MODULOS/app/data.csv')
    data = read_csv('./MODULOS/app/data.csv')
    print(data[0])  # Imprime el primer registro para verificar