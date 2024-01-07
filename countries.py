from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.scrapethissite.com/pages/simple/")
time.sleep(2)

c_name = driver.find_elements(By.CLASS_NAME, 'country-name')
c_capital = driver.find_elements(By.CLASS_NAME, 'country-capital')
c_population = driver.find_elements(By.CLASS_NAME, 'country-population')
c_area = driver.find_elements(By.CLASS_NAME, 'country-area')

country_name = [i.text for i in c_name]
country_capital = [i.text for i in c_capital]
country_population = [i.text for i in c_population]
country_area = [i.text for i in c_area]

countries_list = []

for i in range(len(country_name)):
    country_dict = {
        "name": country_name[i],
        "capital": country_capital[i],
        "population": country_population[i],
        "area": country_area[i]
    }
    countries_list.append(country_dict)

csv_file_path = "countries_data.csv"

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["name", "capital", "population", "area"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for country in countries_list:
        writer.writerow(country)

print(f"CSV file '{csv_file_path}' has been created successfully.")

driver.quit()