import requests

def submit_news_sitemap(sitemap_url, api_key):
    search_console_api_url = f'https://www.googleapis.com/webmasters/v3/sites/{sitemap_url}:submit'
    headers = {'Content-Type': 'application/json'}
    params = {'key': api_key}

    response = requests.post(search_console_api_url, headers=headers, params=params)

    if response.status_code == 200:
        print('News sitemap submitted successfully!')
    else:
        print(f'Error submitting news sitemap: {response.status_code} - {response.text}')

if __name__ == '__main__':
    # Replace 'YOUR_NEWS_SITEMAP_URL' with the actual URL of your news sitemap
    news_sitemap_url = 'YOUR_NEWS_SITEMAP_URL'

    # Replace 'YOUR_SEARCH_CONSOLE_API_KEY' with your Google Search Console API key
    api_key = 'YOUR_SEARCH_CONSOLE_API_KEY'

    submit_news_sitemap(news_sitemap_url, api_key)
