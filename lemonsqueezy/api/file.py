import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.file import File
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_file(client: LemonSqueezyProtocol, file_id: str | int) -> File:
    """Get the File"""
    response = requests.get(
        f"{client.base_url}/files/{file_id}", headers=client.headers, timeout=30
    )
    response.raise_for_status()
    file_data = response.json().get("data", {})
    return File(**file_data)


@handle_http_errors
def list_files(client: LemonSqueezyProtocol) -> list[File]:
    """List the file"""
    file = []
    page = 1
    while True:
        response = requests.get(
            f"{client.base_url}/files?page[number]={page}&page[size]=10",
            headers=client.headers,
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
