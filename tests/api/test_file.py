from lemonsqueezy.api.file import get_file, list_files
from lemonsqueezy.models.file import File


def test_get_file(file_id):
    file = get_file(file_id)
    assert isinstance(file, File)


def test_list_files():
    files = list_files()
    assert all(isinstance(file, File) for file in files)
