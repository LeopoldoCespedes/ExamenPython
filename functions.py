import csv
def read_data(fichero):
 with open(fichero, 'r') as file:
    reader = csv.reader(file)
    dic = {1:{}}
    for row in reader:
        
        print(row)
read_data('winequality.csv')