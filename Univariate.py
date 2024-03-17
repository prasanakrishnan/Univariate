class Univariate():
    def QualQuan(dataset):
        Qual=[]
        Quan=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=="O"):
                #print('Qual')
                Qual.append(columnName)
            else:
                #print('Quan')
                Quan.append(columnName)
        return Qual,Quan
