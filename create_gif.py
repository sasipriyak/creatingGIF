import imageio.v3 as iio
import os

input_files = input("Enter PNG file paths (comma-separated): ").split(',')
filenames = [file.strip() for file in input_files]

images = []
for filename in filenames:
    if os.path.exists(filename):
        print(f"Loading: {filename}")
        img = iio.imread(filename)
        images.append(img)
    else:
        print(f"Error: File not found -> {filename}")

if images:
    output_path = "Priya.gif"
    iio.imwrite(output_path, images, duration=500, loop=0)
    print(f"GIF created successfully: {output_path}")
else:
    print("No images found, GIF not created.")
