import inspect
from django.contrib import admin
import app.models

# Register your models here.
ms = inspect.getmembers(app.models, inspect.isclass)
for model in ms: admin.site.register(model[1])
