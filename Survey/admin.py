from django.contrib import admin
# from .models import Question,Join,Builder_Data,Modern_Home,Sales_team,Finished_Inventory,Join_Inventory,Join_Modern_Home,Join_Sales
# from .models import Add_address,ImageUpload
from .models import Question,Modern_Home,Sales_team,Finished_Inventory,Builder_Data,PDFDocument
# # # Register your models here.
admin.site.register(Builder_Data)
admin.site.register(Question)
# admin.site.register(Join)
# admin.site.register(Join_Sales)
# admin.site.register(Join_Inventory)
# admin.site.register(Join_Modern_Home)
admin.site.register(Modern_Home)
admin.site.register(Sales_team)
admin.site.register(Finished_Inventory)
admin.site.register(PDFDocument)
# admin.site.register(ImageUpload)
# admin.site.register(Add_address)