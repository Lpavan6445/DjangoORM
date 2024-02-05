from rest_framework.response import Response
from .practice import all_solutions
from rest_framework.decorators import api_view

@api_view(['GET'])
def getSolutions(request, solution):
    print(solution)
    print(all_solutions[solution]());
    res = all_solutions[solution]()
    return Response(res)