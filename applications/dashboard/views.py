from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View, TemplateView

from mxhacks.mixins import AdminSession, ReviewerSession, StaffSession

from rest_framework.response import Response
from rest_framework.views import APIView

from applications.models import Application, Batch, Review
from hackers.models import Campus, Hacker, School

from hackers.serializers import HackerSerializer

import csv
from datetime import date
import random


class ApplicationsStat(StaffSession, APIView):

    def get(self, request, format='json'):
        applications = Application.objects.all().order_by('created')
        daily_applications = []

        for application in applications:
            date_key = (
                str(application.created.year) + '-' +
                str(application.created.month) + '-' +
                "%02d" % application.created.day
            )

            day = None
            for application_day in daily_applications:
                if application_day['day'] == date_key:
                    day = application_day
                    break
            if not day:
                daily_applications.append({
                    'day': date_key,
                    'applications': 1
                })
            else:
                day['applications'] += 1

        return Response(daily_applications)


class ApplicationsPie(StaffSession, APIView):

    def get(self, request, format='json'):
        total = Application.objects.all().count()
        finished = Application.objects.filter(finished=True).count()
        accepted = Application.objects.filter(accepted=True).count()

        step_1 = Application.objects.filter(step=2).count()
        step_2 = Application.objects.filter(step=3).count()
        step_3 = Application.objects.filter(step=4).count()
        step_4 = Application.objects.filter(step=5).count()

        return Response({
            'progress': {
                'total': total,
                'finished': finished,
                'finished_proportion': (finished * 100) / total
            },
            'filters': {
                'total': total,
                'accepted': accepted,
                'accepted_proportion': (accepted * 100) / total
            },
            'steps': {
                'total': total,
                '1': step_1,
                '1_proportion': (step_1 * 100) / total,
                '2': step_2,
                '2_proportion': (step_2 * 100) / total,
                '3': step_3,
                '3_proportion': (step_3 * 100) / total,
                '4': step_4,
                '4_proportion': (step_4 * 100) / total,
            }
        })


class EducationStats(StaffSession, APIView):

    def get(self, request, format='json'):
        schools_q = School.objects.all()
        schools = []
        for s in schools_q:
            school_hackers = Hacker.objects.filter(school=s)
            school_campus = Campus.objects.filter(school=s)
            campuss = []
            for c in school_campus:
                campus_hackers = Hacker.objects.filter(school=s, campus=c)
                campus = {
                    'name': c.name,
                    'id': c.pk,
                    'totals': {
                        'total': campus_hackers.count(),
                        'finished': sum([ch.application.finished for ch in campus_hackers]), # NOQA
                        'accepted': sum([ch.application.accepted for ch in campus_hackers]), # NOQA
                    }
                }
                campuss.append(campus)
            school = {
                'name': s.name,
                'id': s.id,
                'totals': {
                    'total': school_hackers.count(),
                    'finished': sum([h.application.finished for h in school_hackers]), # NOQA
                    'accepted': sum([h.application.accepted for h in school_hackers]), # NOQA
                },
                'campus': sorted(campuss, key=lambda x: x['totals']['total'])[::-1]
            }
            schools.append(school)

        return Response(sorted(schools, key=lambda x: x['totals']['total'])[::-1])


class DemographicsView(StaffSession, APIView):

    def get(self, request, format='json'):
        hackers = Hacker.objects.filter(application__finished=True)
        ages = {}
        gender = {'males': 0, 'females': 0}
        education_level = {
            'Secundaria': 0,
            'Preparatoria': 0,
            'Universidad': 0,
            'Maestría': 0,
            'Doctorado': 0,
        }
        t_shirt_size = {
            'Small Women': 0,
            'Medium Women': 0,
            'Large Women': 0,
            'Extra Large Women': 0,
            'Small Men': 0,
            'Medium Men': 0,
            'Large Men': 0,
            'Extra Large Men': 0,
        }

        experience = {
            'first_time_hacker': 0,
            'first_time_event': 0,
        }

        working = {'true': 0, 'false': 0}
        locations = {}

        for h in hackers:

            # Age count
            age = ages.get(str(h.age), None)
            if age:
                ages[str(h.age)] += 1
            else:
                ages[str(h.age)] = 1

            # Gender
            if h.male:
                gender['males'] += 1
            if h.female:
                gender['females'] += 1

            # Education Level
            if h.education_level == 'Secundaria':
                education_level['Secundaria'] += 1
            if h.education_level in ['Preparatoria', 'Bachillerato']:
                education_level['Preparatoria'] += 1
            if h.education_level == 'Universidad':
                education_level['Universidad'] += 1
            if h.education_level == 'Maestría':
                education_level['Maestría'] += 1
            if h.education_level == 'Doctorado':
                education_level['Doctorado'] += 1

            # T-Shirt Size
            if h.tshirt_size == 'Chica - Mujer':
                t_shirt_size['Small Women'] += 1
            if h.tshirt_size == 'Mediana - Mujer':
                t_shirt_size['Medium Women'] += 1
            if h.tshirt_size == 'Grande - Mujer':
                t_shirt_size['Large Women'] += 1
            if h.tshirt_size == 'Extra Grande - Mujer':
                t_shirt_size['Extra Large Women'] += 1
            if h.tshirt_size == 'Chica - Hombre':
                t_shirt_size['Small Men'] += 1
            if h.tshirt_size == 'Mediana - Hombre':
                t_shirt_size['Medium Men'] += 1
            if h.tshirt_size == 'Grande - Hombre':
                t_shirt_size['Large Men'] += 1
            if h.tshirt_size == 'Extra Grande - Hombre':
                t_shirt_size['Extra Large Men'] += 1

            # Experience and working status
            if h.first_time_hacker:
                experience['first_time_hacker'] += 1
            if h.first_time_event:
                experience['first_time_event'] += 1

            if h.currently_working:
                working['true'] += 1
            else:
                working['false'] += 1

            # Location
            location = locations.get(h.state + ', ' + h.country, None)
            if location:
                locations[h.state + ', ' + h.country] += 1
            else:
                locations[h.state + ', ' + h.country] = 1

        demos = {
            'total': hackers.count(),
            'ages': ages,
            'gender': gender,
            'education_level': education_level,
            't_shirt_size': t_shirt_size,
            'experience': experience,
            'working': working,
            'locations': locations,
        }

        return Response(demos)


class PunchCardView(StaffSession, APIView):

    def get(self, request, format='json'):
        q = Application.objects.all()
        week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        ret_val = {x: {y: 0 for y in range(24)} for x in week}

        for _ in q:
            ret_val[week[_.created.date().weekday()]][_.created.hour] += 1  # NOQA

        return Response(ret_val)


class ExportView(AdminSession, TemplateView):

    template_name = 'dashboard/export.html'

    def get_context_data(self, **kwargs):
        context = super(ExportView, self).get_context_data(**kwargs)
        context['batches'] = Batch.objects.all().order_by('-created')
        return context

    def post(self, request):
        start_date = request.POST.get('start_date', None)
        end_date = request.POST.get('end_date', None)

        if not any([start_date, end_date]):
            return redirect(reverse('applications_dashboard:export'))

        try:
            start_date = [int(x) for x in start_date.split('-')]
            start_date = date(start_date[0], start_date[1], start_date[2])

            end_date = [int(x) for x in end_date.split('-')]
            end_date = date(end_date[0], end_date[1], end_date[2])
        except:
            return redirect(reverse('applications_dashboard:export'))

        batch = Batch()
        batch.created_by = request.user
        batch.start_date = start_date
        batch.end_date = end_date
        batch.save()

        return redirect(reverse('applications_dashboard:export'))


class CSVView(AdminSession, View):

    def get(self, request, pk):
        batch = get_object_or_404(Batch, pk=pk)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="MXHacksIV_{}_{}.csv"'.format(
            str(batch.start_date),
            str(batch.end_date),
        )

        batch.requested += 1
        batch.save()

        writer = csv.writer(response)
        writer.writerow([
            'ID',
            'E-mail',
            'First Name',
            'Last Name',
            'Age',
            'Gender',
            'School',
            'Campus',
            'Major',
            'School ID',
            'School Join Year',
            'School Graduation Year',
            'Currently Working',
            'Country',
            'State',
            'T-Shirt Size',
            'Dietary restrictions',
            'First time hacker',
        ])

        q = Application.objects.filter(
            finished = True,
            created__gte = batch.start_date,
            created__lte = batch.end_date
        )

        for application in q:
            hacker = application.hacker
            writer.writerow([
                hacker.pk,
                hacker.email,
                hacker.first_name.title(),
                hacker.last_name.title(),
                hacker.age,
                'Male' if hacker.male else 'Female',
                hacker.school.name,
                hacker.campus.name,
                hacker.major,
                hacker.school_identification,
                hacker.school_join_year,
                hacker.school_graduation_year,
                'Yes' if hacker.currently_working else 'No',
                hacker.country,
                hacker.state,
                hacker.tshirt_size.split(' - ')[0],
                hacker.dietary_restrictions,
                'Yes' if hacker.first_time_hacker else 'No',
            ])

        return response


class ReviewApplications(ReviewerSession, TemplateView):

    template_name = 'dashboard/review.html'


class ReviewDetail(ReviewerSession, APIView):

    def get(self, request, format='json'):
        q = Application.objects.filter(
            finished=True,
            reviews__lte=6,
        ).values('id')

        reviewed = Review.objects.filter(reviewer=request.user).values('application') # NOQA

        q_ids = [_['id'] for _ in q]
        r_ids = [_['id'] for _ in reviewed]

        ids = [_ for _ in q_ids if _ not in r_ids]
        pk = random.choice(ids)

        application = Application.objects.get(pk=pk)
        hacker = HackerSerializer(application.hacker).data

        return Response(hacker)
