from django.db import models
import pandas as pd

# Create your models here.
class Styles(models.Model):
    def __str__(self):
        return self.name

    objects = models.Manager()

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
                "classes": data[['subCategory']].set_index(['subCategory']),
                "ibu": data[['subCategory','IBUMin','IBUMax']].rename(columns={'IBUMin':'min','IBUMax':'max'}),
                "srm": data[['subCategory','SRMMin','SRMMax']].rename(columns={'SRMMin':'min','SRMMax':'max'}),
                "og": data[['subCategory','OGMin','OGMax']].rename(columns={'OGMin':'min','OGMax':'max'}),
                "fg": data[['subCategory','FGMin','FGMax']].rename(columns={'FGMin':'min','FGMax':'max'}),
                "abv": data[['subCategory','ABVMin','ABVMax']].rename(columns={'ABVMin':'min','ABVMax':'max'})
            }
            
        def getVariable(self, variable):
            return self.variables[variable]
        
        def setVariable(self, variable, value):
            self.variables[variable] = value
            
        def getVariablePossibilities(self, variable):
            return self.dfs[variable][
                    (self.dfs[variable]['min'] <= self.getVariable(variable))
                & (self.dfs[variable]['max'] >= self.getVariable(variable))
            ]['subCategory']
            
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
                .rename(columns={'classes': 'frequency', 'index':'subCategory'})[[
                'subCategory',
                'frequency'
            ]]
            
            allPossibilities['probability'] = allPossibilities['frequency'] / len(self.variables.keys())
            
            if json:
                return allPossibilities.to_json(orient="records")
            else:
                return allPossibilities

