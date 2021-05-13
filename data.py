import pandas as pd
import statistics
import plotly.figure_factory as pf 
import random
import plotly.graph_objects as go

dataframe = pd.read_csv('./medium_data.csv')
data = dataframe['id'].tolist()

popmean = statistics.mean(data)
popstdev = statistics.stdev(data)

print(popmean,popstdev)

def ex():
    sample = []

    for i in range(30):
        index = random.randint(0 , len(data)-1)
        value = data[index]
        sample.append(value)
    
    meansample = statistics.mean(sample)
    
    return meansample 

expmean = []

for i in range(100):
    meansample = ex()
    expmean.append(meansample)
print(meansample)
mean = statistics.mean(expmean)
sd = statistics.stdev(expmean)
print(mean , sd)

fstart , fend = mean-sd , mean+sd 
sstart , send = mean-(2*sd) , mean+(2*sd)
tstart , tend = mean-(3*sd),mean+(3*sd)

zscore = ( mean - popmean )/sd
print( ' The ZSCORE of intervention is :' , zscore)

fig = pf.create_distplot([expmean], ["Sampling Mean"] , show_hist= False)
fig.add_trace(go.Scatter(x = [mean , mean] , y = [ 0 , 0.002] , mode = "lines" , name = "MEAN"))
fig.add_trace(go.Scatter(x = [fstart , fstart] , y = [ 0 , 0.002] , mode = "lines" , name = "FIRST STDEV START"))
fig.add_trace(go.Scatter(x = [fend , fend] , y = [ 0 , 0.002] , mode = "lines" , name = "FIRST STDEV END"))
fig.add_trace(go.Scatter(x = [sstart , sstart] , y = [ 0 , 0.002] , mode = "lines" , name = "SECOND STDEV START"))
fig.add_trace(go.Scatter(x = [send , send] , y = [ 0 , 0.002] , mode = "lines" , name = "SECOND STDEV END"))
fig.add_trace(go.Scatter(x = [tstart , tstart] , y = [ 0 , 0.002] , mode = "lines" , name = "THIRD STDEV START"))
fig.add_trace(go.Scatter(x = [tend , tend] , y = [ 0 , 0.002] , mode = "lines" , name = "THIRD STDEV END"))
fig.show()



