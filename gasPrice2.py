import matplotlib.pyplot as plt
import pandas as pd

def main() -> None:
    import_path = './files/'
    export_path = './plots/'

    #gas_data = pd.read_csv('C:/Users/KSTrv/Desktop/matplotlib/data/gasPrices.csv') # We specify the ABSOLUTE path of our data
    gas = pd.read_csv(import_path + 'gasPrices.csv') # We specify the RELATIVE path of our data (meaning relative to our current position)

    plt.title('Gas Price in USD')

    # Here, we specify a list of the countries that we want to plot the prices for
    countries_to_plot = {'USA': 'blue', 'Canada': 'yellow', 'South Korea': 'red', 'Australia': 'purple', 'Germany': 'green'}

    # We iterate through the list specified above with a simple for loop
    for country, myColor in countries_to_plot.items():
        plt.plot(gas.Year, gas[country], marker = '.', label = country, color = myColor)

    # We can use our pd frame either as an object or as a list
    #plt.plot(gas['Year'], gas.USA, label = 'USA', marker = '^', color = 'blue')
    #plt.plot(gas.Year, gas.Canada, label = 'Canada', marker = '^', color = 'red')
    #plt.plot(gas.Year, gas['South Korea'], label = 'South Korea', marker = '^', color = 'green')
    #plt.plot(gas.Year, gas['Australia'], label = 'Australia', marker = '^', color = 'purple')

    plt.xlabel('Year')
    plt.ylabel('US Dollars')

    plt.xticks(gas.Year[::3].to_list() + [2011]) # [1998, 2001, ..., 2008] + [2011]
    # in general: plt.xticks([])

    plt.legend() # this is mandatory so that a legend is created with the specified labels above
    plt.savefig(export_path + 'gas_prices_plot.png')

    plt.show()

if __name__ == "__main__":
    main()
