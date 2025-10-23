from sftp import SFTPClient
from dotenv import load_dotenv
import os
from sharepoint import SharePointClient

load_dotenv()

sftpHost = os.getenv("SFTP_HOST")
sftpPort = int(os.getenv("SFTP_PORT"))
username = os.getenv("SFTP_USERNAME")
password = os.getenv("SFTP_PASSWORD")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["https://graph.microsoft.com/.default"]

local_path = "./key.txt"
remote_path = "/Bank Statements/key.txt"

if __name__ == "__main__":
    # sftpClient = SFTPClient(
    #     host=sftpHost,
    #     port=sftpPort,
    #     username=username,
    #     password=password
    # )
    #
    # sftpClient.list_files("/Bank Statements")
    #
    # # sftpClient.download(remote_path, "./downloads/file.txt")
    #
    # sftpClient.close()

    # SharePoint integration
    sharepointClient = SharePointClient(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        tenant_id=TENANT_ID,
        authority=AUTHORITY,
        scopes=SCOPES
    )

    site_name = "aretexaus.sharepoint.com"
    site_path = "/sites/ANZ-D365FOIntegration"

    site = sharepointClient.get_site(site_name, site_path)
    site_id = site["id"]

    drive = sharepointClient.get_drive(site_id)
    drive_id = drive["value"][0]["id"]

    # Upload sample
    upload_file = sharepointClient.upload(drive_id, "./key.txt", "key.txt", "ANZ Bank statements")
    print(upload_file)

    # List files sample
    # files = sharepointClient.list_files(drive_id)
    #
    # for file in files:
    #     print(file["name"])
