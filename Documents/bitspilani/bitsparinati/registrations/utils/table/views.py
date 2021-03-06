#!/usr/bin/env python
# coding: utf-8
import json

from django.db.models import Q
from django.http import HttpResponse
from django.views.generic.list import BaseListView
from django.core.serializers.json import DjangoJSONEncoder

from table.forms import QueryDataForm
from .tables import TableDataMap
from functools import reduce
from table.views import JSONResponseMixin
from itertools import chain


class FeedDataView(JSONResponseMixin, BaseListView):
	"""
	The view to feed ajax data of table.
	"""

	context_object_name = 'object_list'

	def get(self, request, *args, **kwargs):
		if not hasattr(self, 'token'):
			self.token = kwargs["token"]
		self.columns = TableDataMap.get_columns(self.token)

		query_form = QueryDataForm(request.GET)
		if query_form.is_valid():
			self.query_data = query_form.cleaned_data
		else:
			return self.render_to_response({"error": "Query form is invalid."})
		return BaseListView.get(self, request, *args, **kwargs)

	def get_queryset(self):
		model = TableDataMap.get_model(self.token)

		if model is None:
			return None
		return model.objects.all()

	def get_extra_queryset(self):
		model = TableDataMap.get_extra_model(self.token)
		
		if model is None:
			return None
		return model.objects.all()

	def filter_queryset(self, queryset, extra_queryset):
		def get_filter_arguments(filter_target):
			"""
			Get `Q` object passed to `filter` function.
			"""
			queries = []
			fields = [col.field for col in self.columns if col.searchable]
			for field in fields:
				key = "__".join(field.split(".") + ["icontains"])
				value = filter_target
				queries.append(Q(**{key: value}))
			return reduce(lambda x, y: x | y, queries)

		filter_text = self.query_data["sSearch"]
		if filter_text:
			for target in filter_text.split():
				queryset = queryset.filter(get_filter_arguments(target))
				extra_queryset = extra_queryset.filter(get_filter_arguments(target))

		return queryset, extra_queryset

	def sort_queryset(self, queryset, extra_queryset):
		def get_sort_arguments():
			"""
			Get list of arguments passed to `order_by()` function.
			"""
			arguments = []
			for key, value in self.query_data.items():
				if not key.startswith("iSortCol_"):
					continue
				field = self.columns[value].field.replace('.', '__')
				dir = self.query_data["sSortDir_" + key.split("_")[1]]
				if dir == "asc":
					arguments.append(field)
				else:
					arguments.append("-" + field)
			return arguments
		order_args = get_sort_arguments()
		if order_args:
			queryset = queryset.order_by(*order_args)
			extra_queryset = extra_queryset.order_by(*order_args)
		return queryset, extra_queryset

	def paging_queryset(self, queryset):
		start = self.query_data["iDisplayStart"]
		length = self.query_data["iDisplayLength"]
		if length < 0:
			return queryset
		else:
			return queryset[start: start + length]

	def convert_queryset_to_values_list(self, queryset):
		# FIXME: unit test
		return [
			[col.render(obj) for col in self.columns]
			for obj in queryset
		]

	def get_queryset_length(self, queryset, extra_queryset):
		return queryset.count() + extra_queryset.count()

	def get_context_data(self, **kwargs):
		"""
		Get context data for datatable server-side response.
		See http://www.datatables.net/usage/server-side
		"""
		sEcho = self.query_data["sEcho"]

		context = super(BaseListView, self).get_context_data(**kwargs)
		queryset = context["object_list"]
		extra_queryset = self.get_extra_queryset()
		if queryset is not None or extra_queryset is not None:
			total_length = self.get_queryset_length(queryset, extra_queryset)
			queryset, extra_queryset = self.filter_queryset(queryset, extra_queryset)
			display_length = self.get_queryset_length(queryset, extra_queryset)

			queryset, extra_queryset = self.sort_queryset(queryset, extra_queryset)

			queryset = list(chain(queryset, extra_queryset))

			queryset = self.paging_queryset(queryset)
			values_list = self.convert_queryset_to_values_list(queryset)
			context = {
				"sEcho": sEcho,
				"iTotalRecords": total_length,
				"iTotalDisplayRecords": display_length,
				"aaData": values_list,
			}
		else:
			context = {
				"sEcho": sEcho,
				"iTotalRecords": 0,
				"iTotalDisplayRecords": 0,
				"aaData": [],
			}
		return context

	def render_to_response(self, context, **response_kwargs):
		return self.render_to_json_response(context)