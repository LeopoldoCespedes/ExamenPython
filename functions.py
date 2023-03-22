import csv
def read_data(fichero):
 with open(fichero, 'r') as file:
    reader = csv.reader(file)
    dic = {
            1 : {'type': 'white', 
            'fixed acidity': '7', 
            'volatile acidity':'0.27',
            'citric acid' : '0.36',
            'residual sugar':'20.7',
            'chlorides':'0.045',
            'free sulfur dioxide' : '45',
            'total sulfur dioxide':'170',
            'PH': '3',
            'sulphates': '0.45',
            'alcohol':'8.8',
            'quality':'6'
            }
    }
    suma = 1
    for row in reader:
      if (len(reader)<10):
        print("ha habido un error")
        

      
      dic1 = dic[suma]
      dic1.update({'type' : row[0],'fixed acidity':row[1],'volatile acidity':row[2]})
      dic1.update({'residual sugar':row[3],'chlorides':row[4],'free sulfur dioxide':row[5]})
      dic1.update({'total sulfur dioxide':row[6],'PH':row[5],'sulphates':row[6]})
      dic1.update({'sulphates':row[7],'alcohol':row[8],'quality':row[9]})
      suma = suma+1
      dic.update({suma:dic1})       
      
    return dic 
print(read_data('winequality.csv'))