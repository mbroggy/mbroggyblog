#!/usr/bin/env python
# filepath: c:\Users\Michael Broggy\code\mbroggyblog\qr_code_generator.py
import os
import frontmatter
import qrcode
from PIL import Image

# Directory paths (adjust as needed)
POSTS_DIRS = [
    r"c:\Users\Michael Broggy\code\mbroggyblog\content\posts",
    r"c:\Users\Michael Broggy\code\mbroggyblog\content\sca",
    r"c:\Users\Michael Broggy\code\mbroggyblog\content\tech",
    r"c:\Users\Michael Broggy\code\mbroggyblog\content\brewing",
]
IMAGES_DIR = r"c:\Users\Michael Broggy\code\mbroggyblog\static\images"
BASE_URL = "https://xooyooz.xyz"

# Ensure images directory exists
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

MAIN_TEXT_COLOR = "#000000"  
BACKGROUND_COLOR = "#FFFFFF"

for POSTS_DIR in POSTS_DIRS:
    for root, dirs, files in os.walk(POSTS_DIR):
        print(f"Entering directory: {root}")  # Debug print
        for filename in files:
            if filename.endswith(".md"):
                post_path = os.path.join(root, filename)
                print(f"Processing file: {post_path}")  # Debug print

                # Parse front matter from the file
                with open(post_path, "r", encoding="utf-8") as f:
                    post = frontmatter.load(f)

                    print(f"Generating QR code for: {post_path}")  # Debug print

                    # If there's a 'slug' in front matter, use it; otherwise use the filename
                    base_name = os.path.splitext(filename)[0]
                    slug = post.get("slug", base_name)

                    # Force the slug to lowercase
                    slug_lower = slug.lower()

                    # Build the post URL using the lowercase slug
                    post_url = f"{BASE_URL}/posts/{slug_lower}/"

                    # Generate the QR code with the main text color as the foreground and black as the background
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(post_url)
                    qr.make(fit=True)
                    img = qr.make_image(fill_color=MAIN_TEXT_COLOR, back_color=BACKGROUND_COLOR)
                    img = img.resize((125, 125))

                    # Save the QR code image using a lowercase filename
                    qr_filename = f"qr-{slug_lower}.png"
                    qr_filepath = os.path.join(IMAGES_DIR, qr_filename)
                    img.save(qr_filepath)

                    # Add the QR code path to the front matter if not present
                    if 'qr' not in post:
                        post['qr'] = f"/images/{qr_filename}"
                        with open(post_path, "w", encoding="utf-8") as f:
                            f.write(frontmatter.dumps(post))

                    # Print the Markdown reference with the lowercase slug
                    print(
                        f"For {filename}, use:\n"
                        f"![QR code for {slug_lower}](/images/{qr_filename})\n"
                    )
