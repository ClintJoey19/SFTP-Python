from sftp import SFTPClient
from dotenv import load_dotenv
import os

load_dotenv()

sftpHost = os.getenv("SFTP_HOST")
sftpPort = int(os.getenv("SFTP_PORT"))
username = os.getenv("SFTP_USERNAME")
password = os.getenv("SFTP_PASSWORD")

local_path = "./key.txt"
remote_path = "/Bank Statements/key.txt"

if __name__ == "__main__":
    sftpClient = SFTPClient(
        host=sftpHost,
        port=sftpPort,
        username=username,
        password=password
    )

    sftpClient.list_files("/Bank Statements")

    sftpClient.download(remote_path, "./downloads/file.txt")

    sftpClient.close()
