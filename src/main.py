from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
def filter(n):
	def comp(list):
    		return list['market_cap_rank']

	coinList = cg.get_coins_markets('usd')
	coinList.sort(key = comp)
	return coinList[:n]