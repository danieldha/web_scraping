import requests
from bs4 import BeautifulSoup
import xlsxwriter
import ast
url_principal = 'https://webscraper.io/test-sites/e-commerce/scroll'
url_phones = 'https://webscraper.io/test-sites/e-commerce/scroll/phones/touch'
r = requests.get(url_phones)

soup = BeautifulSoup(r.text, 'lxml')
data_p = soup.find_all('div', class_="ecomerce-items-scroll")[0]
lista_datos = data_p['data-items']
lista_datos = ast.literal_eval(lista_datos)


workbook = xlsxwriter.Workbook('products.xlsx')
worksheet = workbook.add_worksheet('Hoja1')
worksheet.write('A1', 'Producto')
worksheet.write('B1', 'Descripción')
worksheet.write('C1', 'Precio')
fila = 2
for producto in lista_datos:
    worksheet.write('A' + str(fila), str(producto['title']))
    worksheet.write('B' + str(fila), str(producto['description']))
    worksheet.write('C' + str(fila), str(producto['price']))
    fila += 1
workbook.close()
