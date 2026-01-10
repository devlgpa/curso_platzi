
import matplotlib.pyplot as plt

# generara un grafico de barras
def generate_bar_chart(labbels, values):
    fig, ax = plt.subplots()
    ax.bar(labbels, values)
    plt.show()

# generara un grafico de torta
def generate_pie_chart(labbels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labbels)
    ax.axis('equal') 
    plt.show()

if __name__ == "__main__":

    labbels = ['A', 'B', 'C']
    values = [10, 20, 150]

    #generate_bar_chart(labbels, values)
    generate_pie_chart(labbels, values)