import paramiko

class SFTPClient:
    def __init__(self, host, port, username, password=None, private_key_path=None):
        """Initialize and connect to the SFTP server"""
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.private_key_path = private_key_path
        self.transport = None
        self.sftp = None

        self.connect()

    def connect(self):
        """Establish SFTP connection"""
        self.transport = paramiko.Transport((self.host, self.port))

        if self.private_key_path:
            key = paramiko.RSAKey.from_private_key(self.private_key_path)
            self.transport.connect(username=self.username, pkey=key)
        else:
            self.transport.connect(username=self.username, password=self.password)

        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        print("Connected to SFTP Server")

    def list_files(self, remote_path="/"):
        """List the files from the SFTP remote path"""
        for file in self.sftp.listdir(path=remote_path):
            print(file)

    def upload(self, local_path, remote_path):
        """Upload a local file to the remote SFTP directory"""
        self.sftp.put(local_path, remote_path)

    def download(self, remote_path, local_path):
        """Download file from the SFTP server"""
        self.sftp.get(remote_path, local_path)

    def close(self):
        """Close the SFTP connection"""
        if self.sftp:
            self.sftp.close()
        if self.transport:
            self.transport.close()
        print("SFTP connection closed")