from PIL import Image
import requests
from io import BytesIO
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Load processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def load_image(image_path_or_url):
    if image_path_or_url.startswith("http://") or image_path_or_url.startswith("https://"):
        response = requests.get(image_path_or_url)
        image = Image.open(BytesIO(response.content)).convert("RGB")
    else:
        image = Image.open(image_path_or_url).convert("RGB")
    return image

def generate_caption(image_path_or_url):
    raw_image = load_image(image_path_or_url)
    inputs = processor(raw_image, return_tensors="pt")

    with torch.no_grad():
        out = model.generate(**inputs)

    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Example usage
if __name__ == "__main__":
    image_path = "https://www.naturesafariindia.com/wp-content/uploads/2021/09/bengal-tiger-characterstics-compared-930x620.jpg"  # You can use a URL or local file path
    print("Generated Caption:", generate_caption(image_path))
