import pandas as pd

x = {'Box' : ['Box1','Box1','Box1','Box2','Box2','Box2'],
     'Dimension' : ['Length','Width','Height','Length','Width','Height'],
     'Value' : [6,4,2,5,3,4]}

p = pd.DataFrame(x,columns = ['Box','Dimension','Value'])

m = p.pivot_table(index = 'Box',columns = 'Dimension', 
                  values = 'Value').reset_index()
m['Volume'] = m.Length*m.Height*m.Width