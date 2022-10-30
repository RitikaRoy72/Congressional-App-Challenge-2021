import csv

class data_type:
  def print_crime_types():
		#Give what types of crime data this program will give
    print(f"\nHere are the types of crimes statistics collected")
		#Get the state names and print them
    with open('US_violent_crime.csv') as C:
      reader = csv.reader(C)
      header_column = next(reader)
      for column_header in (header_column):
        print(column_header)

  def print_state_names():
		#Give what states this data was collected for
    print(f"\nHere are the states for which statistics are collected:")
		#Get the state names and print them
    with open('US_violent_crime.csv') as C:
      reader = csv.reader(C)
      state_names = []
      for row in reader:
        state_name = row[0]
        state_names.append(state_name)
      print(*state_names, sep = ", ")
