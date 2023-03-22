from functions import read_data
from functions import split
from functions import reduce
#llamada a read_data
read_data('winequality.csv')

split(read_data('winequality.csv'))

reduce(split(read_data('winequality.csv')),'PH')