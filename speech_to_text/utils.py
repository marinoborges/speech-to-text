from mimetypes import MimeTypes

from .config import SUPPORTED_CONTENT_TYPES


def guess_mime_type(audio_file_path, forced_mime_type=None):
    mime = MimeTypes()
    mime_type = forced_mime_type or mime.guess_type(audio_file_path)[0]
    print("Source file mime type: " + mime_type)
    if mime_type not in SUPPORTED_CONTENT_TYPES:
        raise ValueError('MimeType {} not recognized or supported for '
                         'audio file {}'.format(mime_type, audio_file_path))
    return mime_type
