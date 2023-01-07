import pandas as pd
import numpy as np
import time

def get_data():
    print('Reading in sequences.fasta')
    start_time=time.time()
    data = pd.read_csv('sequences.fasta',header=None,sep="|",lineterminator=">",verbose=True) #returns Dataframe
    data.columns = ['Name','Published Date','Length','Genome']
    for i in range(data.shape[1]):
        genome = data['Genome'][i]
        data.loc[:,('Genome',i)]=genome.replace('\n','')
    print('Total time:',time.time()-start_time)
    return data

if __name__ == '__main__':
    data = get_data()
    print(data)
