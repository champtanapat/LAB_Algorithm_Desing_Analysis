stock_prices = []
#with open("/content/drive/MyDrive/Colab Notebooks/stock_prices.csv", "r") as f:
try:
  with open("D:/2_64/COS4502 Algorithm desing and analysis/LAB Data structure and algorithm/HashTable/stock_prices.csv", "r") as f:  
    for line in f:
      tokens = line.split(',')
      day = tokens[0]
      price = float(tokens[1])
      stock_prices.append([day, price])
  #print(stock_prices)
  print(stock_prices[0])
  print(stock_prices[1])
  print(stock_prices[2])
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()


for element in stock_prices:
  if element[0] == 'march 9':
    print(element[1])
