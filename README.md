# 🧠 GEN AI PROJECT SUBMISSION: IMAGE CAPTIONING USING BLIP

---

## 🎓 College Name: Vellore Institute of Technology , Vellore  
### 👤 Student Name: Abhradeep Basu
### 📧 Email Address: abhradeep.basu2023@vitstudent.ac.in

---

## 📌 1. Project Title:

**Image Captioning using BLIP (Bootstrapped Language-Image Pretraining)**

---

## ✍️ 2. Summary of Work Done

### Proposal and Idea Submission:

This project explores the use of **Generative AI** for **image captioning**, a task that automatically describes the content of an image in natural language. We leveraged the **BLIP model** by Salesforce, which is pre-trained for vision-language understanding.

### Objectives:

- Understand how multimodal generative AI models work.
- Use the `Salesforce/blip-image-captioning-base` model from HuggingFace.
- Accept both local and URL image inputs.
- Generate accurate and human-readable captions.
- Test the model across different scenarios like wildlife, objects, and abstract images.

### Execution and Demonstration:

The project was developed in Python using:
- `transformers` (HuggingFace)
- `Pillow` (PIL)
- `requests`
- `torch`

The following features were implemented:

- **Load images** from both local paths and web URLs.
- **Preprocess** the images and pass them through the BLIP model.
- **Generate** natural language captions.
- **Tested** with wildlife and object images for caption clarity and relevance.

---

## 💻 3. GitHub Repository Link

[🔗 GitHub Repository – BLIP Image Captioning](https://github.com/your-username/blip-image-captioning)  
*(Replace with actual URL)*

---

## ✅ 4. Testing Phase

### 4.1 Testing Strategy:

- Checked caption generation on:
  - Local `.jpg` and `.png` images.
  - High-quality and low-quality images.
  - Blank and ambiguous images.

### 4.2 Types of Testing Conducted:

- **Unit Testing**: Verified the correctness of `load_image()` and `generate_caption()` functions.
- **Integration Testing**: Ensured image loading, model inference, and caption decoding worked seamlessly.
- **User Testing**: Ran the model on diverse real-world images.
- **Performance Testing**: Measured model inference speed on CPU.

### 4.3 Results:

- **Accuracy**: Captions were context-aware and visually relevant.
- **Edge Cases**: For ambiguous images, output was sometimes vague but never incorrect.
- **Performance**: Model inference was under 2 seconds per image.

Example:

> **Input**: Bengal tiger in a forest  
> **Caption**: "a large tiger laying in the grass"

---

## 🌱 5. Future Work

1. **Build a Web Interface** (e.g., Streamlit or Flask)
2. **Support Multi-caption Generation**
3. **Fine-tune for Specific Domains** like medical or surveillance imagery.
4. **Translate Captions to Other Languages**
5. **Deploy on Lightweight Devices with ONNX/TorchScript**

---

## 🧾 6. Conclusion

This project demonstrated the power of **generative multimodal models** in producing descriptive image captions. With minimal setup and robust model architecture, we were able to create a pipeline that could be integrated into real-world applications like content accessibility, auto-tagging, and smart galleries.

The project helped deepen understanding of:
- Vision-language learning
- Pretrained model usage via HuggingFace
- Real-world AI deployment pipelines

---

# 📦 GitHub Repository Files

## 🖼️ Image Captioning using BLIP (Bootstrapped Language-Image Pretraining)

This project demonstrates how to generate human-like captions for images using the [Salesforce BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) model.

---

## Features

- ✅ Supports local & URL image inputs
- ✅ Leverages HuggingFace Transformers
- ✅ Clean Python script
- ✅ Ready for integration in web/mobile apps

---

## Tech Stack

| Component        | Description                       |
|------------------|-----------------------------------|
| `Python`         | Core programming language         |
| `Transformers`   | HuggingFace BLIP model            |
| `Pillow`         | Image processing                  |
| `Requests`       | Fetch image from URL              |
| `Torch`          | Backend inference engine          |

---

## Installation

```bash
git clone https://github.com/your-username/blip-image-captioning.git
cd blip-image-captioning
pip install torch torchvision transformers pillow requests
