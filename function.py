import os

products = []
if os.path.isfile('function.csv'):
	print('Yeah!找到檔案')
	with open ('function.csv','r',encoding = 'utf-8') as f:
		for line in f:
			if line == '商品,價格\n':
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案...') 	

#testing

#讀取檔案





# 讓使用者輸入


while True:
	name = input('請輸入商品名稱: ')
	if name == "q":
		break
	price = input('請輸入商品價格: ')
	products.append([name,price])

print(products)

#印出所有購買記錄
for p in products:
	print(p[0]+'的價格是'+p[1])


#寫入檔案

with open ('function.csv','w',encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+','+p[1]+'\n')



