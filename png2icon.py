from PIL import Image

def png_to_ico(png_path, ico_path, sizes=[(64, 64)]):
    """
    Convert PNG image to ICO format
    
    Args:
        png_path: Path to input PNG file
        ico_path: Path to output ICO file
        sizes: List of sizes for the ICO file
    """
    # Open the PNG image
    img = Image.open(png_path)
    
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Create list of images in different sizes
    images = []
    for size in sizes:
        resized_img = img.resize(size, Image.Resampling.LANCZOS)
        images.append(resized_img)
    
    # Save as ICO
    images[0].save(ico_path, format='ICO', sizes=[img.size for img in images])
    print(f"Successfully converted {png_path} to {ico_path}")

# Example usage
if __name__ == "__main__":
    png_file = "C:\\Users\\15694\\Desktop\\实习\\homepage\\images\\favicon\\profile_icon.png"  # Replace with your PNG file path
    ico_file = "C:\\Users\\15694\\Desktop\\实习\\homepage\\images\\favicon\\profile_icon.ico"  # Replace with desired ICO file path

    try:
        png_to_ico(png_file, ico_file)
    except FileNotFoundError:
        print(f"Error: {png_file} not found")
    except Exception as e:
        print(f"Error: {e}")