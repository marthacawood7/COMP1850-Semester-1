import sys
from image import Image
from filtering import blur

if len(sys.argv) != 3:
    print("Error")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

img = Image.read(input_file)
blurred = blur(img)
blurred.write(output_file)