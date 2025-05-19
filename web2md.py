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

import urllib.parse

def save_markdown(url, markdown_content):
    try:
        # Extract the hostname and create a directory name
        parsed_url = urllib.parse.urlparse(url)
        hostname = parsed_url.hostname
        if not hostname:
            print(f"Could not parse hostname from {url}")
            return

        # Use the top-level domain as the directory name
        domain_parts = hostname.split(".")
        if len(domain_parts) > 1:
            directory_name = domain_parts[-2] # Get the part before the last dot (e.g., google from www.google.com)
        else:
            directory_name = hostname # Use the whole hostname if no dots

        # Create the directory if it doesn't exist
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            print(f"Created directory: {directory_name}")

        # Create a safe filename from the URL path
        filename = parsed_url.path.replace("/", "_").replace(":", "_")
        if not filename:
            filename = "index" # Use 'index' if the path is empty

        full_path = os.path.join(directory_name, filename + ".md")

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"Saved {url} to {full_path}")
    except IOError as e:
        print(f"Error saving {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving {url}: {e}")

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
