import pandas as pd
import matplotlib.pyplot as plt

data_1 = pd.read_csv("11_S╠üLA╠ĘSKIE.csv")
print(data_1.head())

def print_hist(dataframe: pd.DataFrame,col:str,bins:int,title:str,xlabel:str,ylabel:str,alpha: float = 0.9, rwidth: float=0.5):
    fig, ax = plt.subplots(figsize= (15,10))
    n,bins,patches = ax.hist(dataframe[col],bins=bins,alpha=alpha,rwidth=rwidth)
    plt.title(title)
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel(ylabel, fontsize=15)
    plt.show()
print_hist(data_1,'Marka',9,"Liczba poszczegolnych pralek każdej firmy",'Marka','Liczba pralek')
print_hist(data_1,'Dni od zakupu',15,'Histogram dni wystawienia recenzji od zakupu','Poszczególne dni','Liczba recenzji')
print_hist(data_1,'Płeć kupującego',10,'Rozkład płci','Płeć','Liczba osób danej płci')
# print_hist(data_1,'Ocena')
# ax = data_1.plot.bar(subplots=True,rot=0)
