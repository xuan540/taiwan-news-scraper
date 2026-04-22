import requests

class GitHubUploader:
    def __init__(self, repo_owner, repo_name, token):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.token = token
        self.api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/'

    def upload_file(self, file_path, file_name, commit_message):
        with open(file_path, 'rb') as file:
            content = file.read()
        content_b64 = base64.b64encode(content).decode('utf-8')

        data = {
            'message': commit_message,
            'content': content_b64,
        }

        headers = {'Authorization': f'token {self.token}'}
        response = requests.put(self.api_url + file_name, json=data, headers=headers)

        if response.status_code in (201, 200):
            print(f'File uploaded successfully: {file_name}')
        else:
            print(f'Error uploading file: {response.content}')