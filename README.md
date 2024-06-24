# Python Scripts Collection

This repository is a collection of various Python scripts for different purposes. Each script is designed to perform a specific task, making it easy to find and use the script that fits your needs. 

## Table of Contents

- [Installation](#installation)
- [Scripts](#scripts)
  - [exchange_rate_fetcher.py](#exchange_rate_fetcherpy)
  - [pdf_tools.py](#pdf_toolspy)


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/python-scripts-collection.git
    cd python-scripts-collection
    ```

2. Install any required dependencies:
    ```sh
    pip install -r requirements.txt
    ```


## Scripts

### exchange_rate_fetcher.py

This script provides two functions: get_historical_exchange_rate to fetch the historical exchange rate for a given date from USD to GBP using web scraping, and get_latest_exchange_rate to fetch the latest exchange rate using an external API.
To use the latest exchange rate functionality, you need to obtain a free API key from ExchangeRate-API, which offers a free plan with 1,500 API requests per month and updates once per day.
Replace the placeholder in the script with your API key. This tool allows users to easily retrieve both historical and latest exchange rates for their currency conversion needs.

### pdf_tools.py
This script provides utilities for managing and manipulating PDF files. It includes functions to convert each page of a PDF into high-resolution images, merge multiple PDF files into a single document, and split a PDF into individual pages. The convert_pdf_to_images function uses the PyMuPDF library to generate images from PDF pages, saving them in the specified format (JPEG or PNG). The process_folder function scans a directory for PDF files and converts each one using the aforementioned function. The merge_pdfs function combines all PDF files in a specified directory into one consolidated PDF using the PyPDF2 library. Finally, the split_pdf function separates each page of a given PDF into its own file. The script can be run with different operations (convert, merge, or split) by setting the appropriate variables in the main execution block.