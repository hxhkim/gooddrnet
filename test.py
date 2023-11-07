import requests

url = "https://www.cmcsungmo.or.kr/api/attach/view/doctor/D0001029/thumbs/1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

response = requests.get(url, verify=False)

if response.status_code == 200:
    image_data = response.content
    with open("test.jpg", "wb") as img_file:
        img_file.write(image_data)
    