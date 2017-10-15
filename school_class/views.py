from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.views import generic
from school_class.models import SchoolClass
from django.urls import reverse
import datetime
# from django.contrib.auth import get_user_model
from students.models import Student
# Create your views here.


# User = get_user_model()
class SingleSchoolClass(generic.DetailView):
    model = SchoolClass
    context_object_name = "school_class"
    template_name = "school_class/class_detail.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        student = get_object_or_404(Student,username__iexact=self.kwargs.get('username'))
        context['student_classes'] = student.classes.all()
        return context


class ListSchoolClass(generic.ListView):
    model = SchoolClass
    context_object_name = "classes"
    template_name = "school_class/class_list.html"


class StudentClasses(generic.ListView):
    model = SchoolClass
    context_object_name = "classes"
    template_name = "school_class/student_class_list.html"

    def get_queryset(self):
        try:
            student = get_object_or_404(Student,username__iexact=self.kwargs.get('username'))
            self.classes_student = student
            # self.classes_student = Student.objects.get(username__iexact=self.kwargs.get('username'))
        except Exception as e:
            # print ("some error:%s" % e,self.kwargs.get('username'))
            raise Http404
        else:
            return self.classes_student.classes.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        student = self.classes_student
        context['classes_student'] = student
        _times = [datetime.time(x,y) for x in range(7,19) for y in range(0,31,30)]
        full_sched = []
        for time in _times:
            days = [time]
            for day in ['M','T','W','Th','F']:
                days.append(student.getClassAt(time,day))
            full_sched.append(days)
        context['sched'] = full_sched
        # context['times'] = _times
        #class_times = self.classes_student.getClassTimes()
        return context

class Conflict(generic.TemplateView):
    template_name = "school_class/class_conflict.html"

def addClass(request,pk,username):
    student = get_object_or_404(Student,username__iexact=username)
    school_class = get_object_or_404(SchoolClass,pk=pk)
    cur_times = student.getClassTimes()
    days,start_time,end_time = school_class.getTimes()

    for d in days:
        if not (d in cur_times):
            continue
        conflict_classes = []
        for interval in cur_times[d]:
            int_start = interval[0]
            int_end = interval[1]
            int_class = interval[2]
            ## if the start_time or end_time falls within interval
            if (start_time >= int_start and start_time <= int_end) or (end_time >= int_start and end_time <= int_end):
                conflict_classes += [int_class]
        if len(conflict_classes) >0:
            return render(request,"school_class/class_conflict.html",{"conflicts":conflict_classes})
            # return HttpResponseRedirect(reverse('classes:conflict'))
    #       return HttpResponseRedirect("school_class/conflict.html")
    student.classes.add(school_class)
    student.save()
    # return render(request,"school_class/student_class_list.html",{'username':username})
    return HttpResponseRedirect(reverse('classes:for_student',kwargs={'username':username}))

def removeClass(request,pk,username):
    student = get_object_or_404(Student,username__iexact=username)
    school_class = get_object_or_404(SchoolClass,pk=pk)
    student.classes.remove(school_class)
    student.save()
    # return render(request,"school_class/student_class_list.html",{'username':username})
    return HttpResponseRedirect(reverse('classes:for_student',kwargs={'username':username}))
