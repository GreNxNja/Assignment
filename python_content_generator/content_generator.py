import os
import base64
from dotenv import load_dotenv
from PIL import Image
# import torch
from torch import FloatTensor
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
)

# Load environment variables
load_dotenv()

# ------------------------------------
# OpenAI Client Setup (Optional - Uncomment to use)
# ------------------------------------
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --------------------------------------------
# HARDCODED PRODUCT CONTENT (Default)
# --------------------------------------------


def generate_product_content():
    return """
Title: AI Galaxy Tee
Description: A bold t-shirt designed with AI-generated galaxies and cosmic themes.
Tags: ["AI", "Galaxy", "Techwear", "T-shirt", "Futuristic"]
"""

# --------------------------------------------
# OpenAI-GENERATED PRODUCT CONTENT (Optional)
# Uncomment the function below to enable GPT content generation
# --------------------------------------------
# def generate_product_content():
#     prompt = "Generate a catchy product title, a short description, and 5 SEO tags for a futuristic AI-themed T-shirt."
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content.strip()


# --------------------------------------------
# HARDCODED IMAGE PATH (Default)
# --------------------------------------------
def generate_image(prompt=""):
    image_path = os.path.join(os.path.dirname(
        __file__), "../assets/generated_image.png")
    return os.path.abspath(image_path)


# --------------------------------------------
# OpenAI-GENERATED IMAGE (Optional)
# Uncomment the function below to enable DALL·E image generation
# --------------------------------------------
# def generate_image(prompt="AI-themed futuristic t-shirt design"):
#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=prompt,
#         size="1024x1024",
#         quality="standard",
#         response_format="b64_json"
#     )
#     if not response.data or not response.data[0].b64_json:
#         raise ValueError("No image data returned from OpenAI.")
#     image_data = response.data[0].b64_json
#     output_path = os.path.join(os.path.dirname(__file__), "../assets/generated_image.png")
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     with open(output_path, "wb") as f:
#         f.write(base64.b64decode(image_data))
#     return output_path


# --------------------------------------------
# IMAGE CAPTIONING AND TAGGING WITH BLIP
# --------------------------------------------
def caption_and_tag_image(image_path: str):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    image = Image.open(image_path).convert("RGB")

    # Caption with BLIP
    blip_processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base")
    blip_model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base")

    blip_inputs = blip_processor(images=image, return_tensors="pt")
    pixel_values: FloatTensor = blip_inputs["pixel_values"]  # type: ignore

    caption_ids = blip_model.generate(pixel_values=pixel_values)
    caption = blip_processor.decode(caption_ids[0], skip_special_tokens=True)

    # Default fallback tags
    tags = ["AI", "Galaxy", "Digital", "Minimal", "Future"]

    # --------------------------------------------
    # GPT-GENERATED TAGS BASED ON CAPTION (Optional)
    # --------------------------------------------
    # prompt = f"""
    # Given the following caption of an AI-generated T-shirt image, suggest 5 SEO-friendly tags relevant to futuristic apparel:
    #
    # Caption: "{caption}"
    #
    # Only respond with a Python list of strings.
    # """
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # raw_output = response.choices[0].message.content.strip()
    # try:
    #     generated_tags = eval(raw_output)
    #     if isinstance(generated_tags, list):
    #         tags = generated_tags
    # except:
    #     pass

    return caption, tags


# --------------------------------------------
# MAIN EXECUTION
# --------------------------------------------
if __name__ == "__main__":
    print("Generating product content...")
    content = generate_product_content()
    print("\nGenerated Product Content:\n", content)

    print("\nGenerating product image path...")
    image_path = generate_image()

    if os.path.exists(image_path):
        print("Image found at:", image_path)
        print("\nRunning image captioning and tagging...")
        caption, tags = caption_and_tag_image(image_path)
        print("\nImage Caption:", caption)
        print("Predicted Tags:", tags)
    else:
        print("ERROR: Image not found at", image_path)
