import matplotlib.pyplot as plt
import pandas as pd

def main() -> None:
    gas = pd.read_csv('./files/gasPrices.csv') # gas is our dataframe object

    plt.figure(figsize = (8,5))

    plt.title('Gas Price in USD')

    #for country in gas: # check all of the countries in the dataframe
    #    if country != 'Year': # Year is also a column of the gas dataframe
    #        plt.plot(gas.Year, gas[country], marker = '^', label = country)

    countries_to_check = ['USA', 'Canada', 'South Korea', 'Australia']

    for country in countries_to_check:
        plt.plot(gas.Year, gas[country], marker = '^', label = country)

    #plt.plot(gas.Year, gas.USA, label = 'USA', marker = '.', color = 'blue')
    #plt.plot(gas.Year, gas.Canada, label = 'Canada', marker = '.', color = 'red')
    #plt.plot(gas.Year, gas['South Korea'],  'g.-', label = 'South Corea') # shorthand format (before label attribute)
    #plt.plot(gas['Year'], gas['Australia'], 'y.-')

    #plt.xticks(gas.Year[::3])
    plt.xticks(gas.Year[::3].to_list()+[2011])

    plt.xlabel('Year')
    plt.ylabel('US Dollars')

    #plt.legend()
    #plt.legend(loc = 'center left', bbox_to_anchor = (1,0.5))
    plt.legend(loc = 'upper center', bbox_to_anchor = (0.5, -0.05), fancybox = True, shadow = True, ncol = 4)

    plt.savefig('./plots/gas_price_plot.png', dpi=300) # dpi controls resolution of the exported image
    plt.show()

if __name__ == "__main__":
    main()
