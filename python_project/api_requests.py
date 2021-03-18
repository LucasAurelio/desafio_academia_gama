import requests


def get_response(endpoint):
    try:
        endpoint_response = requests.get(endpoint, timeout=6000).json()
        return endpoint_response

    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.TooManyRedirects as errm:
        print(errm)
    except requests.ConnectionError as errc:
        print(errc)
    except requests.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)


def main_endpoint():
    pass
