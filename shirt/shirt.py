import sys
from pathlib import Path
from PIL import Image, ImageOps


def main():
    # if the user does not specify exactly two command-line arguments
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        input_image = sys.argv[1]
        output_image = sys.argv[2]
        # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
        if not input_image.endswith(('.png', '.jpg', '.jpeg')) or not output_image.endswith(('.png', '.jpg', '.jpeg')):
            sys.exit("Invalid output")
        # if the input’s name does not have the same extension as the output’s name
        elif not Path(input_image).suffix == Path(output_image).suffix:
            sys.exit("Input and output have different extensions")
        else:
            p_shirt(input_image, output_image)


def p_shirt(your_image, result_image):
    try:
        # opening the image and the shirt
        your_image = Image.open(your_image)
        shirt = Image.open('shirt.png')
        # shirt = Image.open('/workspaces/51095931/shirt/shirt.png')
        # fitting the imgage to the shirt size
        your_image = ImageOps.fit(your_image, size = (600, 600))
        # paste shirt on image when shirt used as mask
        your_image.paste(shirt, shirt)
        your_image.save(result_image, format=None)
    except FileNotFoundError:
        sys.exit("Input does not exist")



if __name__ == "__main__":
    main()