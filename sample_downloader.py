from datasets import load_dataset
from PIL import Image
import os
from pyprojroot import here

dataset = load_dataset('naver-clova-ix/cord-v2', split='validation')
save_dir = os.path.join(here(), "Val_data")
os.makedirs(save_dir, exist_ok=True)

for i in range(20):
    image = dataset[i]['image']
    image = image if isinstance(image, Image.Image) else Image.fromarray(image)
    image.save(os.path.join(save_dir, f'image_{i}.png'))
    print(f"Saved image {i} to {save_dir}")

print("All images have been saved.")
