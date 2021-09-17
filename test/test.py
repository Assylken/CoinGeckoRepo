import sys

sys.path.insert(0, '/Users/asylk/Desktop/pycoingecko/src')
  
from main import filter

n = int(input('Enter a number to output top N cryptocurrencies: '))
print()
coinList = filter(n)
for val in coinList:
	print(val['name'], "| Price: ", val['current_price'], "$ | Market_Cap: ", val['market_cap'])