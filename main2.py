# import pandas and rpy2 library and r packages
import pandas as pd
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr 
igraph = importr('igraph')
spreadr = importr('spreadr')

# opens file with list of words and saves column of words as df
# CHANGE NAME OF DIRECTORY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
data = pd.read_csv (r'C:\Users\zckul\Desktop\Vitevitch Research\Vitevitch-Research-Simulations\Words_Aphasia-Aging_Gavin.csv')
df = pd.DataFrame(data, columns = ['Test_word']) 

#converts .net file to matrix for spreadr CHANGE NAME OF DIRECTORY AND LEXICON FILE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
robjects.r("hml <- read_graph('C:/Users/zckul/Desktop/Vitevitch Research/Vitevitch-Research-Simulations/HML_lexicon90.net', format = c('pajek'))")

# sets starting word
wordnum = 0

# runs the three r commands (outputs file in end), inserts word where needed as df.iat, running backward for now so it'll meet up with how much gavin has done
while wordnum <= 164:
    robjects.r("initial_df <- data.frame(node = '" + df.iat[wordnum, 0] + "', activation = 20, stringsAsFactors = F)")
    print("1 " + df.iat[wordnum, 0])
    robjects.r(df.iat[wordnum, 0] + "  <- spreadr::spreadr(start_run = initial_df, decay = 0, retention = 0.5, suppress = 0, network = hml, time = 5)")
    print("2 " + df.iat[wordnum, 0])

    # CHANGE OUTPUT FILE NAME TO MATCH .NET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!HERE
    robjects.r("write.csv(" + df.iat[wordnum, 0] + ", file = '" + df.iat[wordnum, 0] + "_" + "0.9" +".csv')")   
    print("3 " + df.iat[wordnum, 0])    
    wordnum = wordnum + 1
