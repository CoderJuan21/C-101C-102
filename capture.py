import dropbox
import time
import random
import cv2
start_time = time.time()

def Take_Snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret , frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False
    return img_name
    print("snapshot taken!")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.AwXUwS-PfcJedYWmuiGLcf3P4PkfFFSG1Z1nKxKKa9t6SPwo-9eT-6OGncd-K48ET_6NJLxNKKdtI9nyZwYhefyFczwvOdsOitRLisnYgNopGWOG0A6ubjyszSJ05-wMnfr-a94"
    file = img_name
    file_from = file
    file_to = "/NewFolder1/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(file.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>= 30):
            name = Take_Snapshot()
            upload_file(name)

main()
