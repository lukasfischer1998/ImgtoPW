# Image to Password Converter

![Binary Code Network Technology Concept Background](https://img.freepik.com/free-vector/binary-code-netwrok-technology-concept-background_1017-13992.jpg?w=1380&t=st=1713483353~exp=1713483953~hmac=ac28be3a0c820b7b71e44899b8f208fa5d8016db397f3d96ae00c0ed598358de)

Converts images into passwords using ASCII characters.
I've seen someone use something similiar so I went and tried to make my own version of it.

## Features:

- Converts images to binary format.
- Transforms binary data into ASCII characters.
- Generates passwords of variable lengths.
- Allows users to find existing passwords by specifying start index and length.
- Note: Images larger than 500x500 pixels may take longer to process. It's recommended to use images with diverse colors for better results!!

## How it works:

1. Input an image file.
2. The image is converted to binary format.
3. Binary data is translated into ASCII characters.
4. Users can either generate new passwords or find existing ones.
5. Passwords are saved in the "finalPW" directory as PW(0-...).txt File. Theres also the Start Index and length given in the PW.txt File so youre able to find it if youre still in
   possession of the picture.

## Usage:

1. Place your image file in the `img` folder.
2. If there are multiple images in the img folder, the program will automatically prompt you to choose one.
3. Run `main.py`.
4. Choose youre preferred Picture
5. Choose between creating new passwords or finding existing ones.
6. Follow the prompts to specify password length or search parameters.
7. View generated passwords in the "finalPW" directory.

## Required Packages:

- PIL (Python Imaging Library)
- numpy
- os

## Note

If you would be willing to introduce another kind of algorithm to create a safe pw form a picture just go for a pull request and contribute.
See ya Lukas.
