from django.shortcuts import render, redirect
from . models import *
from django.db.models import Q
from django.views.generic import ListView

# Create your views here.

def ssearch(request):
    return render(request, 'seach_obj.html')

# def reports_list(request):
#     reports = Report.objects.all()
#     context = {
#         'reports': reports
#     }
#     return render(request, 'seach_obj.html', context)

# def search_by_q_objects(request):
#     query = request.GET.get('query')
#     if query:
#         checks_ran_searched_query = Report.objects.filter(Q(checks_ran__icontains=query)).order_by('-id')
#         checks_result = [ch for ch in checks_ran_searched_query]
#         last_5_checks_ran = ''
#         for chks in checks_result:
#             chks_result = chks.checks_ran.split()[-5:]
#             last_5_checks_ran = chks_result
#         checks_list = []
#         for c in checks_result:
#             che_result = c.checks_ran.split()
#             if query in che_result:
#                 checks_list.append(query)
#                 break
#         recommendations_searched_query = Report.objects.filter(Q(recommendations__icontains=query))
#         result = [q for q in recommendations_searched_query]
#         recommended = ''
#         for recommend in result:
#             rec = recommend.recommendations.split()[-5:]
#             recommended = rec
#             print("\n last 5 words \n", recommended)
#         recommended_query = []
#         for r in result:
#             rec = r.recommendations.split()
#             if query in rec:
#                 recommended_query.append(query)
#                 break
        
#     else:
#         reports_searched_query = Report.objects.all()
#     context = {
#         'checks_ran_searched_query': checks_ran_searched_query,
#         'recommendations_searched_query': recommendations_searched_query,
#         'recommended_query': recommended_query,
#         'checks':checks_list,
#         'last_5_checks_ran': last_5_checks_ran,
#         'last_5_recommended':recommended,
#     }
#     return render(request, 'seach_obj.html', context)


# class ReportListView(ListView):
#     context_object_name = 'report_list_object'
#     template_name = 'report/report_list.html'
#     def get_queryset(self):
#         pass
#     def get_context_data(self, **kwargs):
#         context = super(ReportListView, self).get_context_data(**kwargs)
#         context['report'] = Report.objects.all()
#         context['farm'] = Farm.objects.all()
#         #context['owner'] = FarmOwnerUser.objects.all()
#         return context


class RecommendationsChecksRanSearch(ListView):
    context_object_name = 'blogs'
    model = Report
    template_name = 'seach_obj.html'

    # def get_queryset(self):
    #     pass
    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        print("\n User input query \n", query)
        if query:
            print("\n If query exists \n", query)
            checks_ran_searched_query = Report.objects.filter(Q(checks_ran__icontains=query))
            checks_result = [ch for ch in checks_ran_searched_query]
            last_5_checks_ran = ''
            for chks in checks_result:
                chks_result = chks.checks_ran.split()[-5:]
                last_5_checks_ran = chks_result
            checks_list = []
            for c in checks_result:
                che_result = c.checks_ran.split()
                if query in che_result:
                    checks_list.append(query)
                    break
            recommendations_searched_query = Report.objects.filter(Q(recommendations__icontains=query))
            result = [q for q in recommendations_searched_query]
            recommended = ''
            for recommend in result:
                rec = recommend.recommendations.split()[-5:]
                recommended = rec
            recommended_query = []
            for r in result:
                rec = r.recommendations.split()
                if query in rec:
                    recommended_query.append(query)
                    break
        context = super().get_context_data(**kwargs)
        context['last_5_checks_ran'] = last_5_checks_ran
        context['last_5_recommended'] = recommended
        context['checks_ran_searched_query'] = checks_ran_searched_query
        context['recommendations_searched_query'] = recommendations_searched_query
        context['recommended_query'] = recommended_query
        context['checks'] = checks_list
        return context