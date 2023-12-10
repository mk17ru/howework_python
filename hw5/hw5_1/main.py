import sys

import aiohttp
import asyncio
from pathlib import Path

async def download_image(session, url, destination):
    async with session.get(url) as response:
        if response.status == 200:
            image_data = await response.read()
            with open(destination, 'wb') as file:
                file.write(image_data)
            print(f"Downloaded: {destination}")
        else:
            print(f"Failed to download {url}")

async def download_images(folder, count_images):

    url_base = 'https://picsum.photos/200/300?image='

    async with aiohttp.ClientSession() as session:
        tasks = []
        for image_id in range(1, count_images + 1):
            url = f'{url_base}{image_id}'
            file = folder + "/" + str(image_id) + ".jpg"
            task = download_image(session, url, file)
            tasks.append(task)

        await asyncio.gather(*tasks)

folder = "artifacts"
destination_path = Path(folder)
destination_path.mkdir(parents=True, exist_ok=True)

if len(sys.argv) > 1:
    num_images_to_download = int(sys.argv[1])
else:
    #default
    num_images_to_download = 1

asyncio.run(download_images(folder, num_images_to_download))
