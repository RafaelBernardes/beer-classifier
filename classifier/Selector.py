import pandas as pd
df = pd.read_excel("dados.xlsx")
class Selector:
    def __init__(self, data):

        self.variables = {
            "ibu": None,
            "srm": None,
            "og": None,
            "fg": None,
            "abv": None            
        }
        
        self.dfs = {
            "classes": df[['cod', 'category', 'subCategory']].set_index(['cod']),
            "ibu": df[['cod','IBUMin','IBUMax']].rename(columns={'IBUMin':'min','IBUMax':'max'}),
            "srm": df[['cod','SRMMin','SRMMax']].rename(columns={'SRMMin':'min','SRMMax':'max'}),
            "og": df[['cod','OGMin','OGMax']].rename(columns={'OGMin':'min','OGMax':'max'}),
            "fg": df[['cod','FGMin','FGMax']].rename(columns={'FGMin':'min','FGMax':'max'}),
            "abv": df[['cod','ABVMin','ABVMax']].rename(columns={'ABVMin':'min','ABVMax':'max'})
        }
        
    def getVariable(self, variable):
        return self.variables[variable]
    
    def setVariable(self, variable, value):
        self.variables[variable] = value
        
    def getVariablePossibilities(self, variable):
        return self.dfs[variable][
                (self.dfs[variable]['min'] <= self.getVariable(variable))
            & (self.dfs[variable]['max'] >= self.getVariable(variable))
        ]['cod']
        
    def getPossibilities(self, json=False):
        allPossibilities = []
        for variable in self.variables.keys():
            if self.variables[variable] is None:
                raise TypeError("O valor da variável {variavel} não poder ser 'Vazio'.".format(variavel=variable))
            
            allPossibilities.extend(
                self.getVariablePossibilities(variable).to_list()
            )
            
        allPossibilities = pd.DataFrame(allPossibilities, columns=['classes'])['classes'] \
            .value_counts() \
            .to_frame() \
            .join(
                self.dfs['classes']
            ) \
            .reset_index() \
            .rename(columns={'classes': 'frequency', 'index':'code'})[[
            'code',
            'category',
            'subCategory',
            'frequency'
        ]]
        
        allPossibilities['probability'] = allPossibilities['frequency'] / len(self.variables.keys())
        
        if json:
            return allPossibilities.to_json(orient="records")
        else:
            return allPossibilities

# Exemple
## Create Object
myBeer = Selector(df)

# Define variable values
myBeer.setVariable('ibu',10)
myBeer.setVariable('srm',15)
myBeer.setVariable('og',1030)
myBeer.setVariable('fg',1011)
myBeer.setVariable('abv',5.1)

# Get Possible Classes and its Proabilities and Frequencies
# Run -> myBeer.getPossibilities(True) to get JSON Response
myBeer.getPossibilities()