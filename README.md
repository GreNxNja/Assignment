# AI Merch Maker Lite

## Overview

AI Merch Maker Lite is a multi-language automation pipeline that generates futuristic product content and visuals using AI, creates image mockups, and publishes listings to a mock (or real) store like Shopify.

## Tech Stack

| Module | Language / Framework | Description |
|--------|---------------------|-------------|
| Content Generator | Python + OpenAI (optional) | Generates product title, description, tags (GPT optional). |
| Image Captioning | Python + BLIP Transformer | Creates caption and tags from generated images. |
| Mockup Renderer | JavaScript + HTML Canvas | Renders mockup preview using generated image. |
| Publisher API | Java + Spring Boot | Simulates publishing the product. |
| Shopify Integration | Python + REST API | Uploads product with image to Shopify. |
| Orchestrator Script | Python | Runs content generator + hits publisher API. |

## Setup Instructions

### 1. Environment Variables

Create a `.env` file in the root and set:

```env
OPENAI_API_KEY=your-openai-key             # Optional if GPT is used
SHOPIFY_STORE_DOMAIN=your-shop.myshopify.com
SHOPIFY_ADMIN_ACCESS_TOKEN=your-admin-token
```

### 2. Generate Product Content & Image

```bash
python python_content_generator/content_generator.py
```

- Uses hardcoded title/description/tags by default
- Image path: `assets/generated_image.png`
- AI generation (GPT/DALL·E) is commented out, but available

### 3. View Mockup

Open `mockup_canvas/index.html` in a browser to preview your product mockup with image overlay.

### 4. Start Java API

Navigate to the Java publisher directory and run:

```bash
mvn spring-boot:run
```

This launches a fake API at `localhost:8080/api/publish`.

### 5. Run Orchestrator Script

```bash
python python_automation_orchestrator/orchestrator.py
```

- Invokes content/image generator
- Sends mock product JSON to Java server

### 6. Upload Product to Shopify

```bash
python python_content_generator/shopify_uploader.py
```

- Uploads the generated product and embedded image (base64)
- Uses 2024-07 Shopify Admin API
- Hardcoded product used by default; AI integration commented

## Folder Structure

```
AI-Merch-Maker-Lite/
├── assets/
│   └── generated_image.png
├── mockup_canvas/
│   └── index.html
├── python_content_generator/
│   ├── content_generator.py
│   └── shopify_uploader.py
├── python_automation_orchestrator/
│   └── orchestrator.py
├── spring_fake_publisher/
│   └── src/... (Java Spring Boot project)
├── .env
└── README.md
```

## Status

- [x] AI-powered content generation
- [x] BLIP image captioning
- [x] Image mockup rendering
- [x] Java backend simulation
- [x] Shopify API product uploader (with image)
- [ ] Fully automated end-to-end flow (future work)