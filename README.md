# 🖼️ Task 02 – Image Encryption using Pixel Manipulation (Python)

## 📌 Overview
This project implements **image encryption and decryption** using **pixel manipulation techniques**.  
The idea is to modify pixel values using a numeric key so that the original image becomes visually unreadable, and can later be restored using the same key.

This task introduces the concept of **data confidentiality in multimedia security** and demonstrates how simple transformations can protect image data.

Features
- Encrypt an image using a user-defined key
- Decrypt the encrypted image using the same key
- Supports RGB image format
- Simple CLI-based interaction
- Uses Python Imaging Library (Pillow)

---
- Each pixel’s RGB values are modified using a mathematical operation with a secret key
- Encryption alters pixel intensity values
- Decryption reverses the transformation using the same key
- This is a **symmetric encryption approach**

Example: Encrypted Pixel = (Original Pixel + Key) % 256
Decrypted Pixel = (Encrypted Pixel - Key) % 256
