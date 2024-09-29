import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data['photos']

    for i, photo in enumerate(photos[:5], start=1):
        img_url = photo['img_src']
        print(f"Downloading {img_url}")

        img_response = requests.get(img_url)

        if img_response.status_code == 200:
            file_name = f"mars_photo{i}.jpg"
            with open(file_name, 'wb') as file:
                file.write(img_response.content)
            print(f"Saved {file_name}")
        else:
            print(f"Failed to download image {i}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
