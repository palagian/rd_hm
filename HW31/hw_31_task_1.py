# 1. Написати програму, яка буде робити запит на один із 5 сайтів і друкувати статус-код відповіді, назву сайту, а також довжину HTML-коду із відповіді.
# Вибір сайту для здійснення запиту має бути здійснений випадковим чином (random).
#
# Сайти:
# - google.com,
# - facebook.com,
# - twitter.com,
# - amazon.com,
# - apple.com.

import random
import requests

# List of websites
websites = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.amazon.com",
    "https://www.apple.com"
]

# Choosing a random site
random_website = random.choice(websites)

# Request to the selected site
res = requests.get(random_website)

# Getting a response status code
status_code = res.status_code

# Getting a website name
website_name = random_website.split("//")[1]

# Getting the length of the HTML code
html_length = len(res.text)

# Displaying the results
print("Website: ", website_name)
print("Status code: ", status_code)
print("HTML length: ", html_length)
