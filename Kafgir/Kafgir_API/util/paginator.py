from rest_framework.response import Response

from django.core.paginator import Paginator

import attr

class PaginationData:

    DEFAULT_PAGE_SIZE = 20
    
    def __init__(self, request):
        page = request.GET.get('page')
        self.page = 1 if page is None else int(page)
        
        size = request.GET.get('size')
        self.size = self.DEFAULT_PAGE_SIZE if size is None else int(size)

@attr.s
class PaginationOutput:
    data: object = attr.ib()
    total_pages: int = attr.ib()
    current_page: int = attr.ib()

class PaginatorUtil:

    @staticmethod
    def paginate_query_set(query_set, pagination_data: PaginationData):
        paginator = Paginator(query_set, pagination_data.size)
        page = paginator.page(pagination_data.page)
        return page.object_list, paginator.num_pages

    @staticmethod
    def create_pagination_output(data, total_pages, current_page):
        return PaginationOutput(data, total_pages, current_page)
