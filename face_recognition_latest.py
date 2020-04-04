import face_recognition
import os

# Load the jpg files into numpy arrays

image = face_recognition.load_image_file("dad.jpg")

# Get the face encodings for each face in each image file

# Since there could be more than one face in each image, it returns a list of encodings.

# here I know that my image has only one face, so I grab index 0.

try:

    image_encode = face_recognition.face_encodings(image)[0]

except IndexError:

    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")

    quit()

images = os.listdir('known_people')
# for image in images:

# iterate over each image
for image in images:
    if image[-3:] == 'jpg':
        print(image)
        # load the image
        current_image = face_recognition.load_image_file("known_people/" + image)
        # encode the loaded image into a feature vector
        try:
            current_image_encoded = face_recognition.face_encodings(current_image)[0]
        except IndexError:
            print("I wasn't able to locate any faces in {}. Skipping...".format(image))
            continue
        # match your image with the image and check if it matches
        result = face_recognition.compare_faces(
            [current_image_encoded], image_encode)
        # check if it was a match
        if result[0] == True:
            print ("Matched: " + image)
        else:
            print ("Not matched: " + image)

