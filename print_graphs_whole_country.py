import csv
import matplotlib.pyplot as plt
import pandas as pd


#you can use just one function with an integer as input for which column to use because their code is so similar


class plot_stats_country:
  """create a class to print the crime statistics for the entir country"""
  
  def print_stats_for_murder():
    """Print the first column of data"""
    #Import the data, read the first row
    data = pd.read_csv('US_violent_crime.csv')
    #Prepare data  for the X and Y axes
    get_data = pd.DataFrame(data)
    Crime_type = list(get_data.iloc[:, 0])
    Amount = list(get_data.iloc[:, 1])
    #Plot the bar graph
    plt.bar(Crime_type, Amount, color='r')
    #Set titles
    plt.title("America murder stats")
    plt.xlabel("State")
    plt.xticks(rotation=90)
    plt.ylabel("For every 100,000 people")
    #COnfigure and save the plot
    plt.subplots_adjust(bottom = 0.4)
    plt.savefig("Murder.png")
    

  def print_stats_for_state_assault():
    """Print the second column of data"""
    #Import the data and title it
    data = pd.read_csv('US_violent_crime.csv')
    df = pd.DataFrame(data)
    #Print the values
    print(data.iloc[0:50, [0,2]])
    #Give values for the x and y axis
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 2])
    # Plot the data using a bar graph
    #Give the graph color
    plt.bar(X, Y, color='r')
    #Give the graph titel
    plt.title("Assault rates for states across America")
    plt.xlabel("States")
    plt.xticks(rotation=90)
    plt.ylabel("For every 100,000 people")
    #Configure and show the plot
    plt.subplots_adjust(bottom = 0.4)
    plt.savefig("Assault.png")
    

  def print_stats_state_sexual_assault():
    """Print the fourth column of data"""
    #Import the data and give it a title
    data = pd.read_csv('US_violent_crime.csv')
    df = pd.DataFrame(data)
    #Print the numerical data for this request
    print(data.iloc[0:50, [0,4]])
    #Intialize the X, and Y axis for the graphic form of the data
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 4])
    #Plot the data using a bar graph
    plt.bar(X, Y, color='r')
    #Give the graph titel
    plt.title("Sexual assault rates for states across America")
    plt.xlabel("States")
    plt.xticks(rotation=90)
    plt.ylabel("For every 100,000 people")
    # Configure and show the plot
    plt.subplots_adjust(bottom = 0.4)
    plt.savefig("SexualAssaultData.png")
    
