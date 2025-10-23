from msal import ConfidentialClientApplication
import requests

class SharePointClient:
    def __init__(self, client_id, client_secret, tenant_id, authority, scopes):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.authority = authority
        self.scopes = scopes
        self.token_type = None
        self.access_token = None
        self.expires_in = None
        self.ext_expires_in = None
        self.token_source = None

        self.connect()

    def connect(self):
        """Establish connection and authentication to SharePoint"""
        app = ConfidentialClientApplication(
            client_id=self.client_id,
            authority=self.authority,
            client_credential=self.client_secret
        )

        result = app.acquire_token_for_client(scopes=self.scopes)

        print(result)
        self.token_type = result["token_type"]
        self.access_token = result["access_token"]
        self.expires_in = result["expires_in"]
        self.ext_expires_in = result["ext_expires_in"]
        self.token_source = result["token_source"]
        print("Connected to SharePoint")

    def get_site(self, site_name, site_path):
        """Get SharePoint site"""
        url = f"https://graph.microsoft.com/v1.0/sites/{site_name}:{site_path}"
        headers = {"Authorization": f"Bearer {self.access_token}"}

        response = requests.get(
            url=url,
            headers=headers
        )

        site = response.json()

        return site

    def get_drive(self, site_id):
        """Get SharePoint site drive"""
        url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"
        headers = {"Authorization": f"Bearer {self.access_token}"}

        response = requests.get(
            url=url,
            headers=headers
        )

        drive = response.json()

        return drive

    def list_files(self, site_name, site_path):
        """List files from a SharePoint site"""
        print("Files")

    def upload(self, drive_id, file_path, file_name):
        """Upload a file to SharePoint"""
        with open(file_path, "rb") as f:
            content = f.read()

            url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root:/{file_name}:/content"
            headers = {"Authorization": f"Bearer {self.access_token}"}

            response = requests.put(url=url, headers=headers, data=content)

            if response.status_code not in [200, 201]:
                return print("Failed to upload the file")

            print("File uploaded to SharePoint")
            return response.json()

    def download(self, site_name, site_path, file, download_path):
        """Download a file from a SharePoint site"""
        print("File has been downloaded")