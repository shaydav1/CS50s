import json
import requests
import sys


def main():
    try:
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        price = o["bpi"]["USD"]["rate_float"]
        amount = n * price
        print(f"${amount:,.4f}")
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        ...


if __name__ == "__main__":
    main()
