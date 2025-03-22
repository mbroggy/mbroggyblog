#!/usr/bin/env python
# filepath: c:\Users\Michael Broggy\code\mbroggyblog\qr_code_generator.py
import os
import qrcode

# Directory paths (adjust as needed)
POSTS_DIR = r"c:\Users\Michael Broggy\code\mbroggyblog\content\posts"
IMAGES_DIR = r"c:\Users\Michael Broggy\code\mbroggyblog\static\images"
BASE_URL = "https://xooyooz.xyz"

# Ensure images directory exists
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

# Iterate through .md files in posts directory
for filename in os.listdir(POSTS_DIR):
    if filename.endswith(".md"):
        post_path = os.path.join(POSTS_DIR, filename)

        # Extract the exact slug from the filename (no forced lowercase)
        base_name = os.path.splitext(filename)[0]

        # Build the post URL using the same case
        post_url = f"{BASE_URL}/posts/{base_name}/"

        # Generate the QR code
        img = qrcode.make(post_url)

        # Resize to 125x125
        img = img.resize((125, 125))

        # Save the QR code image
        qr_filename = f"qr-{base_name}.png"
        qr_filepath = os.path.join(IMAGES_DIR, qr_filename)
        img.save(qr_filepath)

        # Print the Markdown reference
        print(
            f"For {filename}, use:\n"
            f"![QR code for {base_name}](/images/{qr_filename})\n"
        )