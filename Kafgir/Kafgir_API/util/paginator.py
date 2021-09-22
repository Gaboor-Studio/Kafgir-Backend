from rest_framework.response import Response

from django.core.paginator import Paginator

from django.conf import settings

import attr

class PaginationData:
    '''This is a class for getting and transfering pagination data.'''

    DEFAULT_PAGE_SIZE = getattr(settings, "PRIVATE_DIR", 20)
    
    def __init__(self, request):
        '''Constructor with one argument which is the request object in which the pagination query params
        are sent.\n

        Pagination query params:\n 
        size: Determines the size of the page. It can be configured in settings.py. default: 20
        page: Determines the number of the page.
        '''

        page = request.GET.get('page')
        self.page = 1 if page is None else int(page)
        
        size = request.GET.get('size')
        self.size = self.DEFAULT_PAGE_SIZE if size is None else int(size)

@attr.s
class PaginationOutput:
    '''This is an output DTO for paginated results.'''

    data: object = attr.ib() 
    total_pages: int = attr.ib()
    current_page: int = attr.ib()

class PaginatorUtil:
    '''This is a class for handling pagination stuffs easier.\n'''

    @staticmethod
    def paginate_query_set(query_set, pagination_data: PaginationData):
        '''This static method takes a queryset and the pagination data and returns a list of retrieved objects 
        and the number of total pages.
        '''
        
        paginator = Paginator(query_set, pagination_data.size)
        page = paginator.page(pagination_data.page)
        return page.object_list, paginator.num_pages

    @staticmethod
    def create_pagination_output(data, total_pages, current_page):
        ''' This static methods creates a pagination output given the data, total pages and the current page.'''
        
        return PaginationOutput(data, total_pages, current_page)
