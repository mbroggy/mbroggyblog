#!/usr/bin/env python
# filepath: c:\Users\Michael Broggy\code\mbroggyblog\qr_code_generator.py
import os
import frontmatter
import qrcode

# Directory paths (adjust as needed)
POSTS_DIR = r"c:\Users\Michael Broggy\code\mbroggyblog\content\posts"
IMAGES_DIR = r"c:\Users\Michael Broggy\code\mbroggyblog\static\images"
BASE_URL = "https://xooyooz.xyz"

# Ensure images directory exists
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

for filename in os.listdir(POSTS_DIR):
    if filename.endswith(".md"):
        post_path = os.path.join(POSTS_DIR, filename)

        # Parse front matter from the file
        with open(post_path, "r", encoding="utf-8") as f:
            post = frontmatter.load(f)

        # If there's a 'slug' in front matter, use it; otherwise use the filename (no forced lowercase)
        base_name = os.path.splitext(filename)[0]
        slug = post.get("slug", base_name)

        # Build the post URL to match case from slug or filename
        post_url = f"{BASE_URL}/posts/{slug}/"

        # Generate the QR code
        img = qrcode.make(post_url)

        # Resize to 125x125
        img = img.resize((125, 125))

        # Save the QR code image
        qr_filename = f"qr-{slug}.png"
        qr_filepath = os.path.join(IMAGES_DIR, qr_filename)
        img.save(qr_filepath)

        # Print the Markdown reference
        print(
            f"For {filename}, use:\n"
            f"![QR code for {slug}](/images/{qr_filename})\n"
        )