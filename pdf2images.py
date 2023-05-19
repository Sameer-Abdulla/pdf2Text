import os
from pdf2image import convert_from_path

def pdf_to_images(pdf_path, output_folder):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save each image in the specified output folder
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i+1}.jpeg')
        image.save(image_path, 'JPEG')
        image_paths.append(image_path)

    return image_paths

# Provide the path to the PDF file
pdf_path = '/Users/chemmi/Desktop/SRM-HACK/handWritten_To_Text/PPL.pdf'

# Specify the output folder for the images
output_folder = '/Users/chemmi/Desktop/SRM-HACK/handWritten_To_Text/OutputImages'

# Convert the PDF to images and save them in the output folder
image_paths = pdf_to_images(pdf_path, output_folder)

print("The pages of the PDF have been saved as images:")
