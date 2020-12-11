import requests

if __name__ == "__main__":
    print("Hello World!")

    output = requests.get("https://api.github.com")
    print(output)
