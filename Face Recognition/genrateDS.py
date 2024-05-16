import cv2

def generate_DS():
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def face_cropped(img):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_img, 1.3, 5)  # detect faces
        # scaling factor = 1.3
        # Minimum neighbor = 5

        if len(faces) == 0:
            return []

        cropped_faces = []
        for (x, y, w, h) in faces:
            cropped_face = img[y:y + h, x:x + w]
            cropped_faces.append(cropped_face)

        return cropped_faces if cropped_faces else None

    cap = cv2.VideoCapture(0)
    id = 1
    img_id = 0

    while True:
        ret, frame = cap.read()
        cropped_faces = face_cropped(frame)

        if cropped_faces:
            for face in cropped_faces:
                img_id += 1
                face = cv2.resize(face, (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                path = 'face/user.' + str(id) + '.' + str(img_id) + '.jpg'
                cv2.imwrite(path, face)

                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                # (50, 50) is the point where txt be written
                # font scale = 1
                # thickness = 2
                # (0, 255, 0) Green color

                cv2.imshow('Cropped Face', face)
                if cv2.waitKey(1) == 48 or int(img_id) == 200:
                    break

        if cv2.waitKey(1) == 48 or int(img_id) == 200:
            break

    cap.release()
    cv2.destroyAllWindows()
    print('Collecting sample is completed....')

generate_DS()
