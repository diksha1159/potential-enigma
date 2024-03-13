# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.bbc.com/news'

# try:
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

#     soup = BeautifulSoup(response.text, 'html.parser')
#     headlines = soup.find('body').find_all('h3')
    
#     if headlines:
#         for x in headlines:
#             print(x.text.strip())
#     else:
#         print("No headlines found.")
# except requests.exceptions.RequestException as e:
#     print("Error fetching URL:", e)
# except Exception as e:
#     print("An error occurred:", e)

# import requests    

# # so my documenting skillsa arent exactly good but this is the library we need for now 
# # this is approach one btw

# def NewsFromBBC():
	
# 	# BBC news api
# 	# following query parameters are used
# 	# source, sortBy and apiKey
# 	query_params = {
# 	"source": "bbc-news",
# 	"sortBy": "top",
# 	"apiKey": "1f20debee1e043e1bd935f8eac09d02c"
# 	}
# 	main_url = " https://newsapi.org/v1/articles"

# 	# fetching data in json format
# 	res = requests.get(main_url, params=query_params)
# 	open_bbc_page = res.json()

# 	# getting all articles in a string article
# 	article = open_bbc_page["articles"]

# 	# empty list which will 
# 	# contain all trending news
# 	results = []
	
# 	for ar in article:
# 		results.append(ar["title"])
		
# 	for i in range(len(results)):
		
# 		# printing all trending news
# 		print(i + 1, results[i])

# 	#to read the news out loud for us
# 	from win32com.client import Dispatch
# 	speak = Dispatch("SAPI.Spvoice")
# 	speak.Speak(results)				 

# # Driver Code
# if __name__ == '__main__':
	
# 	# function call
# 	NewsFromBBC() 
# apparenlty a prb with this stmt 
# from newsapi import NewsApiClient
import pycountry
from newsapi.newsapi_client import NewsApiClient


# you have to get your api key from newapi.com and then paste it below
newsapi = NewsApiClient(api_key='1f20debee1e043e1bd935f8eac09d02c')

while True:
    # now we will take the name of the country from the user as input
    input_country = input("Country: ")
    input_countries = [f'{input_country.strip()}']
    countries = {}

    # iterate over all the countries in
    # the world using pycountry module
    for country in pycountry.countries:
        # and store the unique code of each country
        # in the dictionary along with its full name
        countries[country.name] = country.alpha_2

    # now we will check that the entered country name is
    # valid or invalid using the unique code
    codes = [countries.get(country.title(), 'Unknown code')
             for country in input_countries]

    # now we have to display all the categories from which the user will
    # decide and enter the name of that category
    option = input("Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")

    # now we will fetch the news according to the choice of the user
    top_headlines = newsapi.get_top_headlines(
        # getting top headlines from all the news channels
        category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')

    # fetch the top news under that category
    Headlines = top_headlines['articles']

    # now we will display the news with good readability for the user
    if Headlines:
        for articles in Headlines:
            b = articles['title'][::-1].index("-")
            if "news" in (articles['title'][-b+1:]).lower():
                print(
                    f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
            else:
                print(
                    f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
    else:
        print(
            f"Sorry no articles found for {input_country}, Something Wrong!!!")

    option = input("Do you want to search again[Yes/No]? ")
    if option.lower() != 'yes':
        break
