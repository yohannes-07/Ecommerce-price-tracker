import requests
from bs4 import BeautifulSoup
import json
import time
import random

# Load headers from a JSON file
with open("headers.json") as headers_file:
    headers = json.load(headers_file)

def scrape_data(search_query="python"):
    time.sleep(random.randint(1, 5))  # Introduce random delay
    url = f"https://www.upwork.com/search/jobs/?q={search_query}&sort=recency"

    # Send request with headers to mimic browser behavior
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise error if request fails

    # Parse HTML content
    parser = BeautifulSoup(response.content, 'lxml')

    # Extract job information
    job_elements = parser.find_all('a', class_="job-title-link break visited")[:10]

    jobs = []
    for job_element in job_elements:
        title = job_element.text.strip()
        url = f"https://upwork.com/{job_element['href']}"
        description = job_element.find_next('span', class_="js-description-text").text.strip()

        jobs.append({'title': title, 'url': url, 'description': description})

    return jobs

print(scrape_data())
