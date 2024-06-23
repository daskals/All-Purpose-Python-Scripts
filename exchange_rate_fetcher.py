import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_historical_exchange_rate(from_currency, to_currency, date):
    """
    Fetches the historical exchange rate from `from_currency` to `to_currency` for a specific date.

    Parameters:
        from_currency (str): The currency code to convert from (e.g., 'USD').
        to_currency (str): The currency code to convert to (e.g., 'GBP').
        date (str): The date for the exchange rate in 'YYYY-MM-DD' format.

    Returns:
        float: The closing exchange rate from `from_currency` to `to_currency` on the given date.
    """
    # Format the date to match the URL structure
    date_formatted = datetime.strptime(date, "%Y-%m-%d").strftime("%d_%m_%Y")
    url = f"https://www.exchangerates.org.uk/{from_currency}-{to_currency}-{date_formatted}-exchange-rate-history.html"

    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the exchange rate information in the HTML
        exchange_rate_info = soup.find('div', class_='exchange-rate-info')
        if exchange_rate_info:
            # Extract the closing exchange rate
            close_rate_text = exchange_rate_info.find_all('p')[0].text.strip()
            close_rate = float(close_rate_text.split('=')[-1].strip().split()[0])
            return close_rate
        else:
            raise ValueError("Exchange rate information not found on the page.")
    else:
        raise requests.exceptions.RequestException(f"Failed to retrieve the page, status code: {response.status_code}")


def get_latest_exchange_rate(api_key, from_currency, to_currency):
    """
    Fetches the latest exchange rate from `from_currency` to `to_currency`.

    Parameters:
        api_key (str): The API key for the exchange rate service.
        from_currency (str): The currency code to convert from (e.g., 'USD').
        to_currency (str): The currency code to convert to (e.g., 'GBP').

    Returns:
        float: The latest exchange rate from `from_currency` to `to_currency`.
    """
    base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    try:
        # Send a GET request to the API
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        if 'conversion_rates' in data and to_currency in data['conversion_rates']:
            return data['conversion_rates'][to_currency]
        else:
            raise ValueError("Invalid response from exchange rate API or unsupported currency code.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as val_err:
        print(f"Value error: {val_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


# Example usage
api_key = "your_api_key_here"
from_currency = "USD"
to_currency = "GBP"
date = "2024-06-23"

try:
    if date == datetime.now().strftime("%Y-%m-%d"):
        exchange_rate = get_latest_exchange_rate(api_key, from_currency, to_currency)
        if exchange_rate:
            print(f"The latest exchange rate from {from_currency} to {to_currency} is {exchange_rate}")
        else:
            print("Exchange rate not found.")
    else:
        exchange_rate = get_historical_exchange_rate(from_currency, to_currency, date)
        print(f"The exchange rate from {from_currency} to {to_currency} on {date} was {exchange_rate}")
except ValueError as e:
    print(e)