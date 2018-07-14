from django.http import HttpResponse
# from io import StringIO
from django.shortcuts import render

depts_list = [
  {'no': 10, 'name': '财务部', 'location': '北京'},
  {'no': 20, 'name': '研发部', 'location': '成都'},
  {'no': 30, 'name': '销售部', 'location': '上海'},
]

def index(request):
  # output = StringIO()
  # for dept in depts_list:
  #   output.write('\t\t<div>\n')
  #   output.write(f'\t\t\t<span>{dept["no"]}</span>\n')
  #   output.write(f'\t\t\t<span>{dept["name"]}</span>\n')
  #   output.write(f'\t\t\t<span>{dept["location"]}</span>\n')
  #   output.write('\t\t</div>\n')

  return render(request,
                'hrs.html',
                {'depts_list': depts_list})

  # return HttpResponse(output.getvalue())



