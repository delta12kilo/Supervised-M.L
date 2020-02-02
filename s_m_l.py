from sklearn.linear_model import LinearRegression
import pickle as pk

def load_model(file):
    with open(file,'rb') as f:
        return pk.load(f)

a = load_model('profit.pk')
start_up = 'test.pvt.ltd'
rnd = float(input('R&D cost in $: '))
marketing = float(input('Maketing in $: '))
admin = float(input('Administration cost in $: '))
sc = 1
sf = 0
profit = a.predict([[rnd,marketing,admin,sc,sf]])[0]
print(profit)