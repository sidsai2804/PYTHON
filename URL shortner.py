import pyshorteners

def shorten_url(original_url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(original_url)
    return shortened_url

def main():
    original_url = input("Enter the URL to shorten: ")
    shortened_url = shorten_url(original_url)
    print(f"Shortened URL: {shortened_url}")

if __name__ == "__main__":
    main()
