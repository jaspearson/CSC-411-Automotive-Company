from bs4 import BeautifulSoup
import requests
import csv

class Toyota():

    store_id = 1

    def __init__(self):
        self.store_id = 1
        print("The toyota class was initialized.")

    def get_deals(self, this_keyword):

        url = "http://www.toyota.com/"

        # Make the request
        the_request = requests.get(url + this_keyword)

        # Parse the request
        soup = BeautifulSoup(the_request.text, 'html.parser')

        #print(soup)

        # Get the table that holds the products
        models_table = soup.find("div", attrs={'class': 'tcom-nav-drawer'})

        #print(models_table)


        # Get all product container divs
        models = models_table.find_all("li", class_=None)

        #print(models)

        # Initialize a dictionary object
        extracted_records = []

        # Loop through the the html products and extract key pieces of information.

        with open('models.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            for model in models:

                model_name = model.find('h4')
                price_mpg = model.findAll("span")

                if model_name is not None and len(price_mpg) > 0:


                    model_name = model_name.text.strip('\n').strip('\t').replace('\n', ' ').replace('\t', '').strip()

                    year = model_name[0:4]
                    price = price_mpg[0].text
                    mpg = price_mpg[1].text.split('/')

                    price = price.strip('$').replace(',', '')

                    print(['id', model_name, price, mpg[1], 'BS', year, 1])
                    writer.writerow(['id', model_name, price, mpg[1], 'BS', year, 1])


        writeFile.close()

Toyota().get_deals('Test')
