import csv
def read_data(fichero):
 with open(fichero, 'r') as file:
    reader = csv.reader(file)
    dic = {
            1 : {'type': white, 
            'fixed acidity': '7', 
            }
    }
    suma = 1
    for row in reader:
        dic.update({suma:{'type' = row[0],'fixed acidity' = row[1]}})
        print(row)
        suma = suma+1
read_data('winequality.csv')