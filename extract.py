import pandas as pd

# declares target file as df_target
df_target = pd.read_csv(r'C:/Users/zckul/Desktop/Vitevitch Research/Words_Aphasia-Aging.csv')   

# creates empty data frame to store data points
df_alldatapts = pd.DataFrame()

decaynum = 0.1   
wordnum = 0

while decaynum < 1:
    while wordnum < 165:
        word = df_target.iat[wordnum,0] 

        # declares output file as df_data
        df_data = pd.read_csv(r'C:/Users/zckul/Desktop/Vitevitch Research/Auto Simulations/Outputs/decay = ' + str(round(decaynum, 2)) + '/' + word + '_' + str(round(decaynum, 2)) + '.csv')
       
        # saves rows where target word appears as df_positions
        search = word
        df_positions = (df_data.loc[df_data.isin([search]).any(axis=1)].index.to_frame())     
        
        # declares activation data point at fifth activation step as df_datapt
        datapt = df_data.iat[df_positions.iat[4, 0], 2]
    
        print (datapt)
        
        wordnum = wordnum + 1

    # ran out of time - in future make script write data to excel file 
    print("NEW DECAY VALUE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    wordnum = 0
    decaynum = decaynum + 0.2