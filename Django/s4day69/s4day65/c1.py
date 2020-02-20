from django.core.signing import TimestampSigner
class MySigner(TimestampSigner):

    def sign(self, value):

        return value+'123123123'

    def unsign(self, value, max_age=None):

        v = value[0:-8]
        return v
