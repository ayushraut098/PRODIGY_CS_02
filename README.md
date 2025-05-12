# PRODIGY_CS_02

  What This Tool Does
This tool scrambles your image in a simple but clever way:
It swaps pixels to confuse the structure.
Then it tweaks the colors using a secret number (called a key).
You can undo this later using the same number to get your original image back.

  How to Use It
Install the Pillow library
If it’s your first time using this kind of tool, open a terminal or command prompt and type:
"pip install pillow"
This installs the library that helps Python work with images.

Save the Script
Open any code editor (like VS Code, Notepad++, or IDLE), paste the code I gave you into a new file, and save it as:
"image_cipher.py"
Place Your Image Nearby
Make sure the image you want to encrypt (e.g., myphoto.jpg) is in the same folder as the Python file — or be ready to give the full path.

Run the Program
In the terminal, navigate to that folder and type:
python image_cipher.py

You’ll be guided step by step:
Choose whether to Encrypt (E) or Decrypt (D).
Enter your image file name.
Enter a number key between 0 and 255 — think of it as your secret code.
Choose a name for the output image, like secret.png.
That’s it! 
If you encrypted the image, the result will look scrambled or distorted.
Run the same tool again, choose Decrypt, and use the same key to get the original back.
