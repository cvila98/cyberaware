from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from formacions.models import Formacio
from formacions.serializers import FormacioModelSerializer


class ExactMatchModelViweSet(viewsets.ModelViewSet):
    def get_queryset(self):
        qs = super(ExactMatchModelViweSet, self).get_queryset()
        filter = {}
        for param in self.request.query_params:
            if hasattr(self.model, param):
                filter[param] = self.request.query_params.get(param)

        if filter != {}:
            try:
                qs = qs.filter(**filter)
            except ValueError as error:
                raise NotFound(error.message)
        return qs

class FormacioSet(ExactMatchModelViweSet):
    model = Formacio
    queryset = Formacio.objects.get_queryset()
    serializer_class = FormacioModelSerializer
    filter_fields = list(serializer_class.Meta.fields)