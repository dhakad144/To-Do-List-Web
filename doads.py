import pandas as pd
import datetime

class DOADS:
    def __init__(self, url):
        self.df = pd.read_csv(url)
        self.now = datetime.datetime.now()
        self.path = 'data.csv'

    def tickcomplete(self, id):
        self.df.loc[self.df['id'] == int(id), 'status'] = 'complete'
        self.save()  

    def untickcomplete(self, id):
        self.df.loc[self.df['id'] == int(id), 'status'] = 'uncomplete'
        self.save() 

    def appendrow(self,description):
        temp_df = pd.DataFrame({'id':[len(self.df)],'status':['uncomplete'],'description':[f'{description}'],'date':[f'{self.now.date()}']})
        self.df = pd.concat([self.df,temp_df],ignore_index=True) 
        self.save() 

    def updatedescrip(self, id, description):
        self.df.loc[self.df['id'] == int(id), 'description'] = description
        self.df.loc[self.df['id'] == int(id), 'date'] = str(self.now.date())
        self.save() 

    def save(self):
        self.df.to_csv(self.path, index=False)

    def givelists(self):
        complete = self.df[self.df['status'] == 'complete']
        uncomplete = self.df[self.df['status'] == 'uncomplete']
        return [complete, uncomplete]

