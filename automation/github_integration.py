"""
GitHub Integration Module
Handles pulling and pushing files to GitHub repository
"""

import requests
import base64
from datetime import datetime
from typing import Optional, Dict
import config


class GitHubIntegration:
    def __init__(self):
        self.token = config.GITHUB_TOKEN
        self.repo = config.GITHUB_REPO
        self.branch = config.GITHUB_BRANCH
        self.base_url = f"https://api.github.com/repos/{self.repo}"
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_file_content(self, file_path: str) -> Optional[str]:
        """
        Pull a file from GitHub repository
        Returns the file content as a string, or None if failed
        """
        try:
            url = f"{self.base_url}/contents/{file_path}"
            params = {"ref": self.branch}

            response = requests.get(url, headers=self.headers, params=params, timeout=10)

            if response.status_code == 200:
                content_encoded = response.json()["content"]
                content = base64.b64decode(content_encoded).decode("utf-8")
                return content
            else:
                print(f"⚠️  Failed to fetch {file_path}: {response.status_code}")
                return None

        except Exception as e:
            print(f"⚠️  Error fetching {file_path}: {str(e)}")
            return None

    def push_file(self, file_path: str, content: str, commit_message: str) -> bool:
        """
        Push a file to GitHub repository
        Returns True if successful, False otherwise
        """
        try:
            # First, check if file exists to get its SHA
            url = f"{self.base_url}/contents/{file_path}"
            params = {"ref": self.branch}

            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            sha = None
            if response.status_code == 200:
                sha = response.json()["sha"]

            # Encode content
            content_encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")

            # Prepare payload
            payload = {
                "message": commit_message,
                "content": content_encoded,
                "branch": self.branch
            }

            if sha:
                payload["sha"] = sha

            # Push the file
            response = requests.put(url, headers=self.headers, json=payload, timeout=10)

            if response.status_code in [200, 201]:
                return True
            else:
                print(f"⚠️  Failed to push {file_path}: {response.status_code}")
                print(f"Response: {response.text}")
                return False

        except Exception as e:
            print(f"⚠️  Error pushing {file_path}: {str(e)}")
            return False

    def delete_old_briefs(self, briefs_folder: str, retention_days: int) -> int:
        """
        Delete briefs older than retention_days
        Returns count of deleted files
        """
        try:
            url = f"{self.base_url}/contents/{briefs_folder}"
            params = {"ref": self.branch}

            response = requests.get(url, headers=self.headers, params=params, timeout=10)

            if response.status_code != 200:
                return 0

            files = response.json()
            deleted_count = 0

            from datetime import timedelta
            cutoff_date = datetime.now() - timedelta(days=retention_days)

            for file in files:
                if file["name"].startswith("MORNING_BRIEF_"):
                    # Extract date from filename
                    try:
                        # MORNING_BRIEF_2025-11-18.md
                        date_str = file["name"].replace("MORNING_BRIEF_", "").replace(".md", "")
                        file_date = datetime.strptime(date_str, "%Y-%m-%d")

                        if file_date < cutoff_date:
                            # Delete the file
                            delete_url = f"{self.base_url}/contents/{briefs_folder}/{file['name']}"
                            delete_payload = {
                                "message": f"Auto-delete old brief: {file['name']}",
                                "sha": file["sha"],
                                "branch": self.branch
                            }

                            del_response = requests.delete(
                                delete_url,
                                headers=self.headers,
                                json=delete_payload,
                                timeout=10
                            )

                            if del_response.status_code == 200:
                                deleted_count += 1
                                print(f"🗑️  Deleted old brief: {file['name']}")
                    except:
                        continue

            return deleted_count

        except Exception as e:
            print(f"⚠️  Error cleaning old briefs: {str(e)}")
            return 0

    def test_connection(self) -> bool:
        """Test if GitHub connection works"""
        try:
            url = f"{self.base_url}"
            response = requests.get(url, headers=self.headers, timeout=10)
            return response.status_code == 200
        except:
            return False
