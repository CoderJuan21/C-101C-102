import dropbox

class TransferData :
    def __init__ (self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.AwXUwS-PfcJedYWmuiGLcf3P4PkfFFSG1Z1nKxKKa9t6SPwo-9eT-6OGncd-K48ET_6NJLxNKKdtI9nyZwYhefyFczwvOdsOitRLisnYgNopGWOG0A6ubjyszSJ05-wMnfr-a94"
    transferData = TransferData(access_token)
    file_from = input("enter the file path to transfer")
    file_to = input("enter the file path to inport to dropbox")
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()

#C:/Users/AwesomeGamer/Dropbox/Test/Sample.txt
#C:/Users/AwesomeGamer/Downloads/englishbook.jpg
#C:\Users\AwesomeGamer\Downloads\Python\C-101\Dropbox - Shortcut.lnk