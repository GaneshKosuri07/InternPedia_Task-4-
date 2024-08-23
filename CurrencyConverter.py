import requests

def get_exchange_rates(api_key):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['conversion_rates']
    print("Error fetching exchange rates.")
    return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == to_currency:
        return amount
    base_amount = amount / rates[from_currency]
    return base_amount * rates[to_currency]

def main():
    api_key = 'f3241c8f2e617f174f0cc6af'
    rates = get_exchange_rates(api_key)
    if not rates:
        return

    currencies = list(rates.keys())
    while True:
        print("\nAvailable currencies:", ', '.join(currencies))
        from_currency = input("Enter the source currency code: ").upper()
        to_currency = input("Enter the target currency code: ").upper()

        if from_currency not in currencies or to_currency not in currencies:
            print("Invalid currency code.")
            continue

        try:
            amount = float(input(f"Enter the amount in {from_currency}: "))
        except ValueError:
            print("Invalid amount.")
            continue

        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        print(f'{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}')

        if input("Do you want to perform another conversion? (yes/no): ").strip().lower() != 'yes':
            break

main()