#!/usr/bin/env python
# filepath: c:\Users\Michael Broggy\code\mbroggyblog\brewing_label.py
import os
import frontmatter
import subprocess
from PIL import Image

# Directory paths (adjust as needed)
POSTS_DIR = r"c:\Users\Michael Broggy\code\mbroggyblog\content\posts"
IMAGES_DIR = r"c:\Users\Michael Broggy\code\mbroggyblog\static\images"
LABELS_DIR = r"c:\Users\Michael Broggy\code\mbroggyblog\labels"

# Ensure labels directory exists
if not os.path.exists(LABELS_DIR):
    os.makedirs(LABELS_DIR)

# Function to resize the QR code image
def resize_qr_code(qr_code_path, max_size=(100, 100)):
    with Image.open(qr_code_path) as img:
        img.thumbnail(max_size)
        resized_path = os.path.join(LABELS_DIR, os.path.basename(qr_code_path))
        img.save(resized_path)
    return resized_path

# Function to sanitize filenames
def sanitize_filename(filename):
    return filename.replace(":", "_")

# Function to generate label content
def generate_label_content(post):
    brew_name = post.get('brew_name', post['title'])
    brew_abv = post.get('brew_abv', '')
    qr_code = post.get('qr', '')
    brew_style = post.get('brew_style', '')

    # Adjust the QR code path to use the full path and resize it
    if qr_code:
        qr_code_path = os.path.join(IMAGES_DIR, os.path.basename(qr_code))
        qr_code_path = resize_qr_code(qr_code_path)
    else:
        qr_code_path = ''

    content = f"""
# {brew_name}

**ABV:** {brew_abv}

**Style:** {brew_style}

![QR Code]({qr_code_path})
"""
    return content

# Check if pandoc is available
def check_pandoc():
    try:
        subprocess.run(["pandoc", "--version"], check=True)
    except FileNotFoundError:
        print("Error: pandoc is not installed or not found in your PATH.")
        exit(1)

# Process each Markdown file in the POSTS_DIR
check_pandoc()
for root, dirs, files in os.walk(POSTS_DIR):
    for filename in files:
        if filename.endswith(".md"):
            post_path = os.path.join(root, filename)
            print(f"Processing file: {post_path}")  # Debug print

            # Parse front matter from the file
            with open(post_path, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)

            # Check if the post contains brew_ variables
            if any(key.startswith('brew_') for key in post.keys()):
                # Generate label content
                label_content = generate_label_content(post)

                # Sanitize the filename
                sanitized_title = sanitize_filename(post['title'])

                # Save label content to a temporary Markdown file
                temp_md_path = os.path.join(LABELS_DIR, f"{sanitized_title}.md")
                with open(temp_md_path, "w", encoding="utf-8") as f:
                    f.write(label_content)

                # Convert the Markdown file to a printable label using pandoc
                label_pdf_path = os.path.join(LABELS_DIR, f"{sanitized_title}.pdf")
                subprocess.run([
                    "pandoc", temp_md_path, "-o", label_pdf_path, "--pdf-engine=xelatex",
                    "-V", "geometry:paperwidth=54mm,paperheight=70mm,margin=5mm",
                    "-V", "caption=", "-fmarkdown-implicit_figures"
                ])

                # Remove the temporary Markdown file
                os.remove(temp_md_path)

                print(f"Label generated: {label_pdf_path}")