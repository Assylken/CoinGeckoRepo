# CoinGecko API Python

### Installation
PyPI
```bash
pip install pycoingecko
```
or from source
```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

### Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

### Examples

You need just input a number of **_top_** N cryptocurrencies which are sorted by market capitalization.

Usage examples:

```python

Enter a number to output top N cryptocurrencies: 6

Bitcoin | Price:  47660 $ | Market_Cap:  896763348174 
Ethereum | Price:  3454.05 $ | Market_Cap:  405983703199
Cardano | Price:  2.38 $ | Market_Cap:  76238147654
Tether | Price:  1.0 $ | Market_Cap:  69515893173
Binance Coin | Price:  413.69 $ | Market_Cap:  63913830108
XRP | Price:  1.08 $ | Market_Cap:  50072615531

```

### Test

Run unit tests with:

```
# after installing the project
run test.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
