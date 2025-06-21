
import random

def encrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    # Simple encryption: add key to each RGB channel (clamped to 255)
    encrypted_pixels = [(min(r + key, 255), min(g + key, 255), min(b + key, 255)) for (r, g, b) in pixels]

    # Optionally shuffle pixels (more secure but hard to reverse)
    # random.seed(key)
    # random.shuffle(encrypted_pixels)

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Reverse the encryption: subtract key from each RGB channel
    decrypted_pixels = [(max(r - key, 0), max(g - key, 0), max(b - key, 0)) for (r, g, b) in pixels]

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")


if _name_ == "_main_":
    key = 30  
    encrypt_image("input.jpg", "encrypted.jpg", key)
    decrypt_image("encrypted.jpg", "decrypted.jpg", key)



