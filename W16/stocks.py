
import ffn
import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

DataIntc = ffn.get('INTC:Open, INTC:High, INTC:Low, INTC:Close', start='2022-06-01',
end='2022-06-30')
DataIntc.rename(columns={'intcopen':'Intel 開盤', 'intchigh':'Intel 高點', 'intclow':'Intel 低點', 'intcclose':'Intel 收盤'})
print(DataIntc)
print("")
print("===================================================")
print("")
