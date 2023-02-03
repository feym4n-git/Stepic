class GenericView:


    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ''

    def post(self, request):
        pass

    def put(self, request):
        pass

        def __getattribute__(self, item):
            item = item.lower()
            return object.__getattribute__(self, item)

    class DetailView(GenericView):
        def render_request(self, request, method):
            if method not in self.methods:
                raise TypeError('данный запрос не может быть выполнен')

            return getattr(self, method)(request)

        def get(self, request):
            if type(request) is not dict:
                raise TypeError('request не является словарем')

            if 'url' not in request:
                raise TypeError('request не содержит обязательного ключа url')

            return f"url: {request['url']}"

