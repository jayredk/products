import os # 載入作業系統

# 讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查檔案是否存在
	print('找到檔案了！')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,名稱' in line:
				continue
			[name, price] = line.strip().split(',')
			products.append([name,price])
else:
	print('檔案不存在！')

# 讓使用者輸入：
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	products.append([name,price])

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是：', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,名稱\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
