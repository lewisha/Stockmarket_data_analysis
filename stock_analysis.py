import matplotlib.pyplot as plt
import pandas as pd

def matplotlib_demo():
    """
    using matplotlib to plot the stock data
    :return: None
    """
    plt.figure(figsize=(20, 8), dpi=100)
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()

    return None

def read_csv_demo():
    """
    reading the stock data
    :return: None
    """
    stock_day = pd.read_csv("./stock_day/stock_day.csv")

    print(stock_day)
    return None


if __name__ == "__main__":
    
    matplotlib_demo()
    
    read_csv_demo()
