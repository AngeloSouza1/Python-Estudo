import yfinance as yf
from datetime import datetime
from matplotlib import pyplot as plt

end_data = datetime.now().strftime('%Y-%m-%d')
print(end_data)
bb = yf.Ticker('BBAS3.SA')
data_bb = bb.history(
        #"BBAS3.SA", 
        start="2024-01-01", 
        end=end_data, 
)
data_bb['Close'].plot()
plt.savefig('bb_preco.png')
print(data_bb.tail())
data_bb['Volume'].plot()
plt.savefig('bb_volume.png')
