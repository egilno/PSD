import csv

def read_cars_file () :

    with open ("cars.csv ", mode ="r") as file :
        csv_reader = csv . reader ( file )
        next ( csv_reader ) # Skip the header row

        for row in csv_reader :
            print ( row )

read_cars_file ()