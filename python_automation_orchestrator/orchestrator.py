
import requests
import subprocess
import json

content_output = subprocess.check_output(
    ["python", "python_content_generator/content_generator.py"])
print(content_output.decode())

product = {
    "title": "AI T-shirt of the Future",
    "description": "A stunning, AI-generated tee design for tech lovers.",
    "tags": ["AI", "Tech", "T-shirt", "Future", "Futuristic"],
    "imageUrl": "http://localhost:3000/mockup_output.png"
}

response = requests.post("http://localhost:8080/api/publish", json=product)
print("Response from Java Publisher:", response.json())
