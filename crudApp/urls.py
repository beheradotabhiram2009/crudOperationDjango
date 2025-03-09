from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("first/", views.first),
    path('students/', views.student_list, name="student_list"),
    path('students/student_entry', views.student_entry, name="student_entry"),
    path("students/add_student", views.add_student, name='add_student'),
    path('students/edit_student/<rno>', views.edit_student, name="edit_student"),
    path("students/edit_student/update_student/<rno>", views.update_student, name='update_student'),
    path("students/delete_student/<rno>", views.delete_student, name='delete_student'),
    ]
