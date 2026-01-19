from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[i, j] = (r, g, b)

    img.save("encrypted.png")
    print("Image Encrypted Successfully!")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[i, j] = (r, g, b)

    img.save("decrypted.png")
    print("Image Decrypted Successfully!")


choice = input("Encrypt or Decrypt (e/d): ")
key = int(input("Enter key value: "))

if choice == 'e':
    encrypt_image("/home/suhana/Desktop/prodigy task/input.png", key)
elif choice == 'd':
    decrypt_image("encrypted.png", key)
else:
    print("Invalid choice")

