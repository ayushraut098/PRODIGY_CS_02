from PIL import Image
import os

def swap_pixels(img):
    pixels = list(img.getdata())
    for i in range(0, len(pixels) - 1, 2):
        pixels[i], pixels[i + 1] = pixels[i + 1], pixels[i]
    img.putdata(pixels)
    return img

def add_key_to_pixels(img, key, encrypt=True):
new_img = Image.new("RGB", img.size)
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if encrypt:
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
            else:
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
            new_img.putpixel((x, y), (r, g, b))
    
    return new_img

def encrypt_image(input_path, output_path, key):
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        img = swap_pixels(img)
        img = add_key_to_pixels(img, key, encrypt=True)
        img.save(output_path)
        print(f"Image encrypted and saved as '{output_path}'")

def decrypt_image(input_path, output_path, key):
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        img = add_key_to_pixels(img, key, encrypt=False)
        img = swap_pixels(img)
        img.save(output_path)
        print(f"Image decrypted and saved as '{output_path}'")

def main():
    print("Simple Image Encryption tool")
    print("-----------------------")
    action = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().upper()

    if action not in ['E', 'D']:
        print("Invalid choice.")
        return

    input_path = input("Enter the image file path: ").strip()
    if not os.path.exists(input_path):
        print("file does not exists")
        return

    try:
        key = int(input("Enter a numeric key (0-255): "))
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Invalid key! Enter an integer between 0 to 255 ")
        return

    output_path = input("Enter the output file path (e.g., 'output.png'): ").strip()

    if action == 'E':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
