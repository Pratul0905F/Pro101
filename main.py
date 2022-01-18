import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BAX3pS_grM5M-Z0GNJmMdqudC5_usV00fYL9zgR6bNwv_hi0f23YHfp4ymIdeCIMNqLqGlK0PEae6cjFD9beDngWWljBmzSFDDe2OBTFfg8Sg710GektoUI7WijSLh_a80bjdwzHKUvn'
    transferData = TransferData(access_token)

    file_from = './sample.txt'
    file_to = "/Fortnite007"

    # API v2
    transferData.upload_file(file_from, file_to)

main()