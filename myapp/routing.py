# mydjangoapp/websocket/routing.py
from django.urls import re_path

from myapp.consumers import ScriptProgressConsumerA02
from myapp.consumers import ScriptProgressConsumerA3
from myapp.consumers import ScriptProgressConsumerC20
from myapp.consumers import ScriptProgressConsumerC22
from myapp.consumers import ScriptProgressConsumerC24
from myapp.consumers import ScriptProgressConsumerC26
from myapp.consumers import ScriptProgressConsumerC28
from myapp.consumers import ScriptProgressConsumerC30
from myapp.consumers import ScriptProgressConsumerC32
from myapp.consumers import ScriptProgressConsumerC34
from myapp.consumers import ScriptProgressConsumerC36
from myapp.consumers import ScriptProgressConsumerC38
from myapp.consumers import ScriptProgressConsumerC40
from myapp.consumers import ScriptProgressConsumerC42
from myapp.consumers import ScriptProgressConsumerC44
from myapp.consumers import ScriptProgressConsumerC46
from myapp.consumers import ScriptProgressConsumerC48
from myapp.consumers import ScriptProgressConsumerD50
from myapp.consumers import ScriptProgressConsumerE52

websocket_urlpatterns = [

    re_path(r'ws/progressA02/$', ScriptProgressConsumerA02.as_asgi()),
    re_path(r'ws/progressA3/$', ScriptProgressConsumerA3.as_asgi()),
    re_path(r'ws/progressC20/$', ScriptProgressConsumerC20.as_asgi()),
    re_path(r'ws/progressC22/$', ScriptProgressConsumerC22.as_asgi()),
    re_path(r'ws/progressC24/$', ScriptProgressConsumerC24.as_asgi()),
    re_path(r'ws/progressC26/$', ScriptProgressConsumerC26.as_asgi()),
    re_path(r'ws/progressC28/$', ScriptProgressConsumerC28.as_asgi()),
    re_path(r'ws/progressC30/$', ScriptProgressConsumerC30.as_asgi()),
    re_path(r'ws/progressC32/$', ScriptProgressConsumerC32.as_asgi()),
    re_path(r'ws/progressC34/$', ScriptProgressConsumerC34.as_asgi()),
    re_path(r'ws/progressC36/$', ScriptProgressConsumerC36.as_asgi()),

    re_path(r'ws/progressC38/$', ScriptProgressConsumerC38.as_asgi()),
    re_path(r'ws/progressC40/$', ScriptProgressConsumerC40.as_asgi()),
    re_path(r'ws/progressC42/$', ScriptProgressConsumerC42.as_asgi()),
    re_path(r'ws/progressC44/$', ScriptProgressConsumerC44.as_asgi()),
    re_path(r'ws/progressC46/$', ScriptProgressConsumerC46.as_asgi()),

    re_path(r'ws/progressC48/$', ScriptProgressConsumerC48.as_asgi()),
    re_path(r'ws/progressD50/$', ScriptProgressConsumerD50.as_asgi()),
    re_path(r'ws/progressE52/$', ScriptProgressConsumerE52.as_asgi()),



]