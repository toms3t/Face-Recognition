import face_recognition

# Load the jpg files into numpy arrays

image = face_recognition.load_image_file("l.jpg")

# Get the face encodings for each face in each image file

# Since there could be more than one face in each image, it returns a list of encodings.

# here I know that my image has only one face, so I grab index 0.

try:

    image_encode = face_recognition.face_encodings(image)[0]

except IndexError:

    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")

    quit()

known_faces = [

   image_encode

]

image2 = face_recognition.load_image_file("l4.jpg")

try:

    image_encode2 = face_recognition.face_encodings(image2)[0]

except IndexError:

    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")

    quit()
# results is an array of True/False telling if the unknown face matched anyone in the known_faces array

results = face_recognition.compare_faces(known_faces, image_encode2)

print("Is the unknown face a picture of Lynn? {}".format(results[0]))