from mxhacks.mixins import StaffSession

from rest_framework.response import Response
from rest_framework.views import APIView

from applications.models import Application
from hackers.models import Campus, Hacker, School


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
            'secundaria': 0,
            'preparatoria': 0,
            'bachillerato': 0,
            'universidad': 0,
            'maestría': 0,
            'doctorado': 0,
            'missing': 0
        }
        t_shirt_size = {
            'S-W': 0,
            'M-W': 0,
            'L-W': 0,
            'XL-W': 0,
            'S-M': 0,
            'M-M': 0,
            'L-M': 0,
            'XL-M': 0,
            'missing': 0
        }

        experience = {
            'first_time_hacker': 0,
            'first_time_event': 0,
            'missing': 0
        }

        working = {'true': 0, 'false': 0, 'missing': 0}
        locations = {'missing': 0}

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
            if h.education_level:
                if h.education_level == 'Secundaria':
                    education_level['secundaria'] += 1
                if h.education_level == 'Preparatoria':
                    education_level['preparatoria'] += 1
                if h.education_level == 'Bachillerato':
                    education_level['bachillerato'] += 1
                if h.education_level == 'Universidad':
                    education_level['universidad'] += 1
                if h.education_level == 'Maestría':
                    education_level['maestría'] += 1
                if h.education_level == 'Doctorado':
                    education_level['doctorado'] += 1
            else:
                education_level['missing'] += 1

            # T-Shirt Size
            if h.tshirt_size:
                if h.tshirt_size == 'S-W':
                    t_shirt_size['S-W'] += 1
                if h.tshirt_size == 'M-W':
                    t_shirt_size['M-W'] += 1
                if h.tshirt_size == 'L-W':
                    t_shirt_size['L-W'] += 1
                if h.tshirt_size == 'XL-W':
                    t_shirt_size['XL-W'] += 1
                if h.tshirt_size == 'S-M':
                    t_shirt_size['S-M'] += 1
                if h.tshirt_size == 'M-M':
                    t_shirt_size['M-M'] += 1
                if h.tshirt_size == 'L-M':
                    t_shirt_size['L-M'] += 1
                if h.tshirt_size == 'XL-M':
                    t_shirt_size['XL-M'] += 1
            else:
                t_shirt_size['missing'] += 1

            # Experience and working status
            if h.application.step >= 4:
                if h.first_time_hacker:
                    experience['first_time_hacker'] += 1
                if h.first_time_event:
                    experience['first_time_event'] += 1

                if h.currently_working:
                    working['true'] += 1
                else:
                    working['false'] += 1
            else:
                experience['missing'] += 1
                working['missing'] += 1

            # Location
            if h.country and h.state:
                location = locations.get(h.state + ', ' + h.country, None)
                if location:
                    locations[h.state + ', ' + h.country] += 1
                else:
                    locations[h.state + ', ' + h.country] = 1
            else:
                locations['missing'] += 1

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