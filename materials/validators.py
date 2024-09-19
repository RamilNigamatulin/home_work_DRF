import re
from rest_framework.serializers import ValidationError


class VideoLinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = value.get(self.field)
        if tmp_val is not None:
            youtube_link = re.compile(
                '^(https://www.youtube.com/)'
            )
            if not youtube_link.match(tmp_val):
                raise ValidationError('Ссылка возможна только на Youtube')
