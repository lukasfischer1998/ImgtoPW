from PIL import Image
import numpy as np
import sys


class ImageConverter:
    def __init__(self, batch_size=1000):
        self.batch_size = batch_size  # Initialize batch size

    def convert_to_binary(self, val):
        # Convert value to binary and ensure 8 digits
        binary_val = bin(val)[2:]
        filled_binary_val = binary_val.zfill(8)
        return filled_binary_val

    def process_pixel(self, pixel_val):
        # Convert each color channel to binary
        red_binary = self.convert_to_binary(pixel_val[0])
        green_binary = self.convert_to_binary(pixel_val[1])
        blue_binary = self.convert_to_binary(pixel_val[2])
        return [red_binary, green_binary, blue_binary]

    def process_batch(self, batch_pixels):
        binary_array = []  # Initialize binary data list
        for row in batch_pixels:
            for pixel_val in row:
                # Process pixel and append binary data
                binary_array.extend(self.process_pixel(pixel_val))
        return binary_array

    def img_to_binary(self, imgpath):
        try:
            img = Image.open(imgpath)
        except FileNotFoundError:
            print(f"Error: File '{imgpath}' not found.")
            return None
        except Exception as e:
            print(f"error occurred opening the image: {str(e)}")
            return None

        img_array = np.array(img)  # Convert to numpy array
        height, width, _ = img_array.shape  # Get dimensions
        binary_array = []  # Initialize binary data list

        total_pixels = width * height  # Calc total pixels
        pixels_processed = 0  # Process counter

        for i in range(0, height, self.batch_size):
            for j in range(0, width, self.batch_size):
                # Process batch of pixels
                batch_pixels = img_array[i:i +
                                         self.batch_size, j:j + self.batch_size]
                binary_array.extend(self.process_batch(batch_pixels))

                pixels_processed += batch_pixels.size  # Update processed pixels
                progress = min(
                    int((pixels_processed / total_pixels) * 100), 100)
                sys.stdout.write('\r')  # cursor start
                sys.stdout.write("[%-100s] %d%%" %
                                 ('=' * progress, progress))  # Display
                sys.stdout.flush()  # flush buffer

        return binary_array  # Return binary data

    def write_to_file(self, data, filename):
        if not data:
            print("Error: No data to write.")
            return

        try:
            with open(filename, 'w') as file:
                file.truncate(0)  # Clear existing content
                for item in data:  # Write binary data
                    file.write("%s\n" % item)
        except Exception as e:
            print(f"error occurred while writing to file: {str(e)}")
