class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request: dict):
        if 'method' not in request or request['method'] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        render = self.__getattribute__(request.get('method').lower())(request)
        return render



class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )

view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html)