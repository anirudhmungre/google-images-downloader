from sys import argv, exit
from requests import get
from urllib.request import urlretrieve

if len(argv) != 5:
    print('Usage: python app.py <search_keyword> <num_results> <directory_to_save_images> <api_key>')
    exit(0)

keyword = argv[1]
api_key = argv[4]
num_images = int(argv[2])
directory = argv[3]
url = f'https://serpapi.com/search?api_key={api_key}&q={keyword}&tbm=isch&ijn=0'

print(f"""
OPTIONS
-------
Keyword:        {keyword}
API Key:        {api_key}
Number Images:  {num_images}
Save Directory: {directory}
Request URL:    {url}
""")

response = get(url)
print(f'Response Code: {response.status_code}')
if response.status_code == 200:
    data = response.json()
    for index, image in enumerate(data['images_results'][:num_images]):
        index += 1
        save_as = f'{directory}/{index}.jpg'
        try:
            urlretrieve(image['original'], save_as)
            print(f'#{index} has been saved as {save_as}')
        except Exception:
            print(f'#{index} Doesn\'t wanna download for some reason')
else:
    print('Something went wrong!')