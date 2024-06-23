# Python Scripts Collection

This repository is a collection of various Python scripts for different purposes. Each script is designed to perform a specific task, making it easy to find and use the script that fits your needs. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Scripts](#scripts)
  - [exchange_rate_fetcher.py](#exchange_rate_fetcherpy)


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

