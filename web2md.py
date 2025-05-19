# This script will read URLs from url.txt and convert them to markdown.
# Handling sub-pages will require more complex logic, potentially involving
# parsing links and recursively fetching/converting. This initial script
# will focus on converting the main page content.

import requests
from markdownify import markdownify as md
import os

def fetch_and_convert(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes
        html_content = response.text
        markdown_content = md(html_content)
        return markdown_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_markdown(url, markdown_content):
    # Create a safe filename from the URL
    filename = url.replace("http://", "").replace("https://", "").replace("/", "_").replace(":", "_") + ".md"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"Saved {url} to {filename}")
    except IOError as e:
        print(f"Error saving {filename}: {e}")

def main():
    url_file = "url.txt"
    if not os.path.exists(url_file):
        print(f"Error: {url_file} not found in the current directory.")
        return

    with open(url_file, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        print(f"Processing {url}...")
        markdown_content = fetch_and_convert(url)
        if markdown_content:
            save_markdown(url, markdown_content)

if __name__ == "__main__":
    main()
