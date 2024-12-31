from lemonsqueezy.api.file import get_file, list_files
from lemonsqueezy.models.file import File


def test_get_file(client, file_id):
    file = get_file(client, file_id)
    assert isinstance(file, File)


def test_list_files(client):
    files = list_files(client)
    assert all(isinstance(file, File) for file in files)
