import requests
import json

def check_Assignment(domain):
    url = f"https://api.domainsdb.info/v1/domains/search?domain={domain}"

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        print(f"Domain Name: {data['domain']}")
        print(f"Status: {data['status']}")
        
        if data['status'] == 'free':
            print(f"The domain {domain} is available for registration.")
        else:
            print(f"The domain {domain} is already registered.")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    domain = input("Enter a domain name: ")
    check_domain_availability(domain)
