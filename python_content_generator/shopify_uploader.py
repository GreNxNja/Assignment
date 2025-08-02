import os
import json
import base64
import requests
from dotenv import load_dotenv
# from python_content_generator import content_generator  # Uncomment if using AI-generated content

load_dotenv()

SHOP_DOMAIN = os.getenv("SHOPIFY_STORE_DOMAIN")
ACCESS_TOKEN = os.getenv("SHOPIFY_ADMIN_ACCESS_TOKEN")

#  Hardcoded product content
title = "AI Galaxy Tee"
description = "A bold t-shirt designed with AI-generated galaxies and cosmic themes."
tags = ["AI", "Galaxy", "Techwear", "T-shirt", "Futuristic"]
tag_string = ", ".join(tags)

# Hardcoded image path
image_path = os.path.join(os.path.dirname(
    __file__), "../assets/generated_image.png")

#  Commented AI-generated content logic
# product_content = content_generator.generate_product_content()
# image_path = content_generator.generate_image()
# caption, tags = content_generator.caption_and_tag_image(image_path)

caption = "AI-generated t-shirt design"  # Fallback if not using BLIP

#  Encode image
with open(image_path, "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

product_data = {
    "product": {
        "title": title,
        "body_html": f"<strong>{description}</strong>",
        "vendor": "AI Merch Generator",
        "product_type": "T-shirt",
        "tags": tag_string,
        "variants": [
            {
                "option1": "Default",
                "price": "24.99",
                "sku": "AI-GALAXY-001"
            }
        ],
        "images": [
            {
                "attachment": encoded_image,
                "filename": "generated_image.png",
                "alt": caption
            }
        ]
    }
}

headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": ACCESS_TOKEN
}


def upload_product():
    url = f"https://{SHOP_DOMAIN}/admin/api/2024-04/products.json"
    response = requests.post(url, headers=headers,
                             data=json.dumps(product_data))

    if response.status_code == 201:
        print("Product uploaded successfully.")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Failed to upload product.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)


if __name__ == "__main__":
    upload_product()
