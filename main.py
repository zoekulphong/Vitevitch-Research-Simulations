import pandas as pd
import rpy2
import rpy2.robjects as robjects

from rpy2.robjects.packages import importr
igraph = importr('igraph')
spreadr = importr('spreadr')

data = pd.read_csv (r'C:\Users\zckul\Desktop\Vitevitch Research\Words_Aphasia-Aging.csv')    # opens target file
df = pd.DataFrame(data, columns = ['Test_word'])    # defines df as the target column 

decaynum = 1
wordnum = 111

while decaynum < 10:
    robjects.r("hml <- read_graph('C:/Users/zckul/Desktop/Vitevitch Research/HML_lexicon.net', format = c('pajek'))")
    print("1 " + df.iat[wordnum, 0])
    robjects.r("initial_df <- data.frame(node = '" + df.iat[wordnum, 0] + "', activation = 20, stringsAsFactors = F)")
    print("2 " + df.iat[wordnum, 0])
    robjects.r(df.iat[wordnum, 0] + " <- spreadr::spreadr(start_run = initial_df, decay = 0." + str(decaynum) + ", retention = 0.5, suppress = 0, network = hml, time = 5)")
    print("3 " + df.iat[wordnum, 0])
    robjects.r("write.csv(" + df.iat[wordnum, 0] + ", file = '" + df.iat[wordnum, 0] + "_0." + str(decaynum) + ".csv')")       
    print("4 " + df.iat[wordnum, 0])
    decaynum = decaynum + 2 

""" start from middle program
decaynum = 7
wordnum = 120

while decaynum < 10:
    while wordnum < 175:
        robjects.r("hml <- read_graph('C:/Users/zckul/Desktop/Vitevitch Research/HML_lexicon.net', format = c('pajek'))")
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

""" original program
decaynum = 1
wordnum = 0

while decaynum < 10:
    while wordnum < 175:
        robjects.r("hml <- read_graph('C:/Users/zckul/Desktop/Vitevitch Research/HML_lexicon.net', format = c('pajek'))")
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