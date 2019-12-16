class BaseResponse:

    def __init__(self):
        self.status = True
        self.error = None
        self.data = None


response = BaseResponse()
ret = response.__dict__
print(ret, type(ret))
