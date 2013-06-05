from lettuce import *
from lxml import html
from django.test.client import Client
#from nose_tools import assert_equals


@before.all
def set_browser():
    world.browser = Client()


@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
