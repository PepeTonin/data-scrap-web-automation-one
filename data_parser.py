from bs4 import BeautifulSoup
import pandas as pd

data_file = open('data.txt', 'r')

data = data_file.read()

soup = BeautifulSoup(data, 'html.parser')

target_data = []
for element in soup.find_all('h4'):
    target_data.append(element.text)

df = pd.DataFrame(target_data)
df.to_excel('data.xlsx', index=False, header=False)
data_file.close()
