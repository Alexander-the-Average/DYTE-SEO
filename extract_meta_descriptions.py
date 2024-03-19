import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_meta_tags(url):
    """
    Function to retrieve the meta description and meta title from a given URL.
    """
    tags = {'meta_description': 'No meta description found', 'meta_title': 'No meta title found'}
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)

        # If the request was successful
        if response.status_code == 200:
            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the meta description tag
            description_tag = soup.find('meta', attrs={'name': 'description'})
            if description_tag:
                tags['meta_description'] = description_tag.get('content')

            # Find the title tag
            title_tag = soup.find('title')
            if title_tag:
                tags['meta_title'] = title_tag.get_text()

        else:
            tags['meta_description'] = f"Failed to access URL (status code: {response.status_code})"
            tags['meta_title'] = f"Failed to access URL (status code: {response.status_code})"
    except requests.RequestException as e:
        tags['meta_description'] = f"Request failed: {e}"
        tags['meta_title'] = f"Request failed: {e}"

    return tags

def main():
    input_csv = 'urls.csv'  # Input CSV file name
    output_csv = 'urls_with_meta_tags.csv'  # Output CSV file name

    # Reading the CSV file
    urls_df = pd.read_csv(input_csv)

    # Ensure the columns are of string type
    urls_df['Meta Description'] = pd.Series(dtype='str')
    urls_df['Meta Title'] = pd.Series(dtype='str')

    # Extracting the meta description and title for each URL
    for index, row in urls_df.iterrows():
        url = row['URLs']
        print(f"Processing: {url}")
        tags = get_meta_tags(url)
        urls_df.at[index, 'Meta Description'] = tags['meta_description']
        urls_df.at[index, 'Meta Title'] = tags['meta_title']

    # Saving the updated dataframe to a new CSV file
    urls_df.to_csv(output_csv, index=False)

    print(f"Updated CSV file saved to {output_csv}")

if __name__ == "__main__":
    main()
