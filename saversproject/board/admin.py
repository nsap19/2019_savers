from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
# import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('saversproject/saversproject'))))
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# import sys
# sys.path.insert(0, 'saversproject/saversproject')
from .models import *


# Register your models here.

class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content']

class QABoardAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'title','content']

class QABoardCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'q_a']

admin.site.register(NoticeBoard, NoticeBoardAdmin)
admin.site.register(QABoard, QABoardAdmin)
admin.site.register(QABoardComment, QABoardCommentAdmin)


>>>>>>> 4ec8f3a956c12972e8d4aabf116ae74b5063b867
