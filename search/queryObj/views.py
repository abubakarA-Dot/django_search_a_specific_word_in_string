from django.shortcuts import render, redirect
from . models import *
from django.db.models import Q
from django.views.generic import ListView
import re

# Create your views here.

def ssearch(request):
    return render(request, 'seach_obj.html')

def reports_list(request):
    reports = Report.objects.all()
    context = {
        'reports': reports
    }
    return render(request, 'seach_obj.html', context)

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
    context_object_name = 'reports_searched_query'
    model = Report
    template_name = 'seach_obj.html'


    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        print("\n User input query \n", query)
        if query:
            checks_ran_searched_query = Report.objects.filter(Q(checks_ran__icontains=query))
            checks_result = [ch for ch in checks_ran_searched_query]

            

            
            next_5_checks_ran = []
            next_5_for_first = []
            for chks in checks_ran_searched_query:
                chks_result = re.sub("(?<=\D)[.,]|[.,](?=\D)", " ",chks.checks_ran.lower()).split()
                if query in chks_result:
                    # to display next 5 words after the searched word
                    chks_resultt = chks_result[chks_result.index(query) + 1: chks_result.index(query) + 6]
                    next_5_checks = " ".join(chks_resultt)
                    # to display previous 5 words from checks ran
                    prev_5_words = chks_result[chks_result.index(query) - 5: chks_result.index(query)]
                    prev_5_words = " ".join(prev_5_words)
                    next_5_checks_ran.append({
                        'checks_ran': chks.checks_ran,
                        'next_5_words': next_5_checks,
                        'prev_5': prev_5_words,
                        'query': query,
                        'query_title': chks.title,
                        'farm_id':chks.farm.farm_name,
                    })

    

            
            # prev_5_words_checks_ran = ''
            # for prev_5_words in checks_result:
            #     prev_5_words = prev_5_words.checks_ran.split()
            #     if query in prev_5_words:
            #         prev_5_words = prev_5_words[prev_5_words.index(query) - 5: prev_5_words.index(query)]
            #         prev_5_words_checks_ran = prev_5_words


            recommendations_searched_query = Report.objects.filter(Q(recommendations__icontains=query))
            result = [q for q in recommendations_searched_query]
            
            
            next_5_recommended = []
            for recomends in recommendations_searched_query:
                # recomendss = re.split("\s|(?<!\d)[,.](?!\d)", recomends.recommendations.lower())
                recomendss = re.sub("(?<=\D)[.,]|[.,](?=\D)", " ",recomends.recommendations.lower()).split()
                if query in recomendss:

                    # to display previous 5 words from recommendations
                    prev_5_wordd = recomendss[recomendss.index(query) - 5: recomendss.index(query)]
                    print("\n prev 5", prev_5_wordd)
                    prev_str = " ".join(prev_5_wordd)

                    # to display next 5 words after the searched word from recommendations
                    recomendsss = recomendss[recomendss.index(query) + 1: recomendss.index(query) + 6]
                    next_strr = " ".join(recomendsss)
                    
                    next_5_recommended.append({
                        'recommendation_query':recomends.recommendations,
                        'found_word':next_strr,
                        'prev_str':prev_str,
                        'query': query,
                        'query_title': recomends.title,
                        'farm_id':recomends.farm.farm_name,
                    })



            
            # prev_5_wordss = []
            # for prev_5_words in recommendations_searched_query:
            #     prev_5_wordsss = prev_5_words.recommendations.split()
            #     if query in prev_5_wordsss:
            #         prev_5_wordd = prev_5_wordsss[prev_5_wordsss.index(query) - 5: prev_5_wordsss.index(query)]
            #         strr = " ".join(prev_5_wordd)
            #         prev_5_wordss.append({
            #             'rec_query': prev_5_words,
            #             'prev_5': strr
            #         })

            # user searched query
            # recommended_query = []
            # for r in recommendations_searched_query:
            #     rec = r.recommendations.split()
            #     if query in rec:
            #         recommended_query.append(query)
            #         break
            # to search a specific word from string in checks ran
            # checks_list = []
            # for c in checks_ran_searched_query:
            #     che_result = c.checks_ran.split()
            #     print("\n Checks ran word \n", che_result)
            #     if query in che_result:
            #         checks_list.append(query)
            #         print("\n Checks ran word \n", checks_list)
            #         break
        context = super().get_context_data(**kwargs)
        context['next_5_checks_ran'] = next_5_checks_ran
        # context['prev_5_words_checks_ran'] = prev_5_words_checks_ran
        # context['prev_5_wordss'] = prev_5_wordss
        context['next_5_recomends'] = next_5_recommended
        context['checks_ran_searched_query'] = checks_ran_searched_query
        context['recommendations_searched_query'] = recommendations_searched_query
        context['next_5_for_first'] = next_5_for_first
        # context['recommended_query'] = recommended_query
        # context['checks'] = checks_list
        return context