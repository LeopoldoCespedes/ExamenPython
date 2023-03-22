def read_data(fichero):
 f = open(fichero, mode="rb")
 linea = f.readline()
 while linea != "" :
     print("he leído: " + linea)
     linea = f.readline()
 f.close()
read_data("winequality.csv")