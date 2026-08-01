"""
Process Shrikant's anime character image:
1. Remove white background
2. Fade out the bottom (to remove the floor shadow)
3. Resize for banner (right side)
4. Crop face for lanyard avatar
5. Export as base64 PNG strings
"""
from PIL import Image
import base64
import io
import os

INPUT_IMG = r"s:\JavaScript Projects\Github readme\varation 1.jpg"
OUT_DIR = r"s:\JavaScript Projects\Github readme"

def remove_white_bg(img, threshold=235):
    """Remove white background and floor shadow."""
    rgba = img.convert("RGBA")
    data = rgba.getdata()
    new_data = []
    
    width, height = rgba.size
    
    for y in range(height):
        # Calculate fade factor for the bottom 15% of the image
        fade_start = int(height * 0.85)
        fade_alpha = 1.0
        if y > fade_start:
            fade_alpha = max(0.0, 1.0 - (y - fade_start) / (height - fade_start))
            
        for x in range(width):
            idx = y * width + x
            r, g, b, a = data[idx]
            
            # More aggressive thresholding for the floor shadow which is gray/white
            if r > threshold and g > threshold and b > threshold:
                new_data.append((r, g, b, 0))
            elif r > threshold - 25 and g > threshold - 25 and b > threshold - 25:
                alpha = max(0, int(255 * (1 - (r + g + b - 3*(threshold-25)) / (3*25))))
                new_data.append((r, g, b, int(min(a, alpha) * fade_alpha)))
            else:
                new_data.append((r, g, b, int(a * fade_alpha)))
                
    rgba.putdata(new_data)
    return rgba

def img_to_base64_png(img, max_size_kb=250):
    """Convert PIL image to base64 PNG string, optimizing size."""
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    size_kb = buf.tell() / 1024
    
    while size_kb > max_size_kb and img.width > 200:
        new_w = int(img.width * 0.85)
        new_h = int(img.height * 0.85)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="PNG", optimize=True)
        size_kb = buf.tell() / 1024
    
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("ascii"), img

def main():
    print("Loading image...")
    img = Image.open(INPUT_IMG)
    
    # --- Banner image (right side) ---
    print("\n=== Processing banner image ===")
    banner_img = remove_white_bg(img, threshold=230)
    
    banner_w = 540
    ratio = banner_w / banner_img.width
    banner_h = int(banner_img.height * ratio)
    banner_img = banner_img.resize((banner_w, banner_h), Image.LANCZOS)
    
    banner_b64, banner_img = img_to_base64_png(banner_img, max_size_kb=400)
    
    with open(os.path.join(OUT_DIR, "_banner_img_b64.txt"), "w") as f:
        f.write(banner_b64)
    print("Banner image done.")
    
    # We skip lanyard avatar here as it's already built and fine.

if __name__ == "__main__":
    main()
