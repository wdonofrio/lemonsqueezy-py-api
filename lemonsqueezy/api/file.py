import requests

from lemonsqueezy.api import BASE_URL, get_headers
from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.file import File


@handle_http_errors
def get_file(file_id: str | int) -> File:
    """Get the File"""
    response = requests.get(
        f"{BASE_URL}/files/{file_id}", headers=get_headers(), timeout=30
    )
    response.raise_for_status()
    file_data = response.json().get("data", {})
    return File(**file_data)


@handle_http_errors
def list_files() -> list[File]:
    """List the file"""
    file = []
    page = 1
    while True:
        response = requests.get(
            f"{BASE_URL}/files?page[number]={page}&page[size]=10",
            headers=get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()

        for file_data in response_data.get("data", []):
            file.append(File(**file_data))

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return file
