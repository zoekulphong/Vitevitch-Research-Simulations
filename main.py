# import pandas and rpy2 library and r packages
import pandas as pd
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr 
igraph = importr('igraph')
spreadr = importr('spreadr')

# opens file with list of words and saves column of words as df
data = pd.read_csv (r'C:\Users\zckul\Desktop\Vitevitch Research\Vitevitch-Research-Simulations\Words_Aphasia-Aging.csv')    
df = pd.DataFrame(data, columns = ['Test_word'])    

# sets starting decay value and word
decaynum = 1
wordnum = 0

# runs the four r commands (outputs file in end), inserts word where needed as df.iat (runs through entire list)
while decaynum < 10:
    while wordnum < 175:
        robjects.r("hml <- read_graph('C:/Users/zckul/Desktop/Vitevitch Research/Vitevitch-Research-Simulations/HML_lexicon_Aging.net', format = c('pajek'))")
        print("1 " + df.iat[wordnum, 0])
        robjects.r("initial_df <- data.frame(node = '" + df.iat[wordnum, 0] + "', activation = 20, stringsAsFactors = F)")
        print("2 " + df.iat[wordnum, 0])
        robjects.r(df.iat[wordnum, 0] + " <- spreadr::spreadr(start_run = initial_df, decay = 0." + str(decaynum) + ", retention = 0.5, suppress = 0, network = hml, time = 5)")
        print("3 " + df.iat[wordnum, 0])
        robjects.r("write.csv(" + df.iat[wordnum, 0] + ", file = '" + df.iat[wordnum, 0] + "_0." + str(decaynum) + ".csv')")       
        print("4 " + df.iat[wordnum, 0])
        wordnum = wordnum + 1
    wordnum = 0
    decaynum = decaynum + 2 




""" starts from middle of list
decaynum = 7
wordnum = 120

while decaynum < 10:
    while wordnum < 175:
        robjects.r("hml <- read_graph('C:/Users/zckul/Desktop/Vitevitch Research/Vitevitch-Research-Simulations/HML_lexicon_Aging.net', format = c('pajek'))")
        print("1 " + df.iat[wordnum, 0])
        robjects.r("initial_df <- data.frame(node = '" + df.iat[wordnum, 0] + "', activation = 20, stringsAsFactors = F)")
        print("2 " + df.iat[wordnum, 0])
        robjects.r(df.iat[wordnum, 0] + " <- spreadr::spreadr(start_run = initial_df, decay = 0." + str(decaynum) + ", retention = 0.5, suppress = 0, network = hml, time = 5)")
        print("3 " + df.iat[wordnum, 0])
        robjects.r("write.csv(" + df.iat[wordnum, 0] + ", file = '" + df.iat[wordnum, 0] + "_0." + str(decaynum) + ".csv')")       
        print("4 " + df.iat[wordnum, 0])
        wordnum = wordnum + 1
    wordnum = 0
    decaynum = decaynum + 2 
"""

