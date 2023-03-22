import csv
def read_data(fichero):
 """_summary_

Args:
        fichero (_type_): _description_

Raises:
        RuntimeError: _description_

Returns:
        _type_: _description_
"""
 #se lee el fichero
 with open(fichero, 'r') as file:
    reader = csv.reader(file)

    #diccionario base
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
    #se empieza a leer cada linea representada
    #por suma, linea 1 suma = 1
    suma = 1
    for row in reader:
      
      #si la linea tiene todos los atributos
      if(len(row)>=9):
          #se actualiza un diccionario creado a partir del base
          dic1 = dic[suma]
          dic1.update({'type' : row[0],'fixed acidity':row[1],'volatile acidity':row[2]})
          dic1.update({'residual sugar':row[3],'chlorides':row[4],'free sulfur dioxide':row[5]})
          dic1.update({'total sulfur dioxide':row[6],'PH':row[5],'sulphates':row[6]})
          dic1.update({'sulphates':row[7],'alcohol':row[8],'quality':row[9]})
          suma = suma+1
          #se anyade al diccionario base el diccionario creado
          dic.update({suma:dic1}) 
      
      if (len(row)<10):
        print("ha habido un error")
        raise RuntimeError      
    #se devuelve el diccionario 
    return dic 
def split(diccionario):
  whiteDict = {}
  redDict = {}
  suma = 0
  for i in diccionario:
     res1 = diccionario.get(i)
     res = res1.get('type')
     if(res == 'white'):
       whiteDict.update({suma:i})
       

     if(res == 'red'):
       redDict.update({suma:i})
       
     suma = suma+1
  whiteAndRed = [whiteDict,redDict]
  print(whiteAndRed)
  return whiteAndRed

 
 
