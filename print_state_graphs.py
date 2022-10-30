import csv
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
import pandas as pd

class print_state_data():
  """A class to print the data for the individual states"""

  def print_stats_for_Alabama():
    #Import the data, read the first row
    data = pd.read_csv('US_violent_crime.csv')
    print(data.iloc[1])
    #Prepare data for the X and Y axes
    get_data=pd.DataFrame(data)
    
    #THIS IS THE PROBLEM: PROGRAM RECONGIZES HEADER COLUMN ONLY, NOT OTHER ROWS
    Crime_type = list(get_data.iloc[3:4,:])
    print(Crime_type)
    Amount = list(get_data.iloc[1:2,:])
    print(f"{Amount} this is amount")
    #Amount = list(get_data.iloc[[1],[1,1]])
    
    #Plot the bar graph
    plt.bar(Crime_type, Amount, color='r')
    plt.title("Alabama's crime statistics")
    plt.xlabel("Crime Type")
    plt.ylabel("For every 100,000 people")
    plt.xticks(rotation = 90)
    plt.savefig("Alabama.png")
    plt.show()
