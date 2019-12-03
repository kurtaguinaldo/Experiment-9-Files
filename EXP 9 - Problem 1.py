import pandas as pd

a = {'Student' : ['Ice Bear','Panda','Grizzly'],'Math': [80,95,79]}
b = {'Student' : ['Ice Bear','Panda','Grizzly'],'Electronics': [85,81,83]}
c = {'Student' : ['Ice Bear','Panda','Grizzly'],'GEAS': [90,79,93]}
d = {'Student' : ['Ice Bear','Panda','Grizzly'],'ESAT': [93,89,88]}

x = pd.DataFrame(a,columns = ['Student','Math'])
x2 = pd.DataFrame(b,columns = ['Student','Electronics'])
x3 = pd.DataFrame(c,columns = ['Student','GEAS'])
x4 = pd.DataFrame(d,columns = ['Student','ESAT'])

z = pd.merge(x,x2, how = 'right', on = 'Student')
y = pd.merge(z,x3, how = 'right', on = 'Student')
v = pd.merge(y,x4, how = 'right', on = 'Student')

w = pd.melt(v, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
j = w.sort_values('Student').reset_index().drop(columns = ['index'])
i = j.rename(columns = {'variable' : 'Subject' , 'value' : 'Grades'})