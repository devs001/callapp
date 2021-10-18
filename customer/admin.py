from django.contrib import admin, messages
from django.forms import utils
from .forms import CsvFiles
from django.urls import path
from django.shortcuts import render
import datetime
from django.utils.html import format_html
from django.http import HttpResponseRedirect
admin.site.site_header = 'callapp'


