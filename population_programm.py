import requests
import pygal

#создание вызова API и сохранение ответа
url_c = 'https://api.github.com/search/repositories?q=language:c&sort=stars'
url_j = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
url_h = 'https://api.github.com/search/repositories?q=language:haskell&sort=stars'
url_p = 'https://api.github.com/search/repositories?q=language:perl&sort=stars'
url_g = 'https://api.github.com/search/repositories?q=language:go&sort=stars'

c = requests.get(url_c)
java = requests.get(url_j)
haskell = requests.get(url_h)
perl = requests.get(url_p)
go = requests.get(url_g)

print('Status code for C:', c.status_code)
print('Status code for Java:', java.status_code)
print('Status code for Haskell:', haskell.status_code)
print('Status code for Perl:', perl.status_code)
print('Status code for Go:', go.status_code)

#сохранение ответа API в переменной
dict_c = c.json()
dict_java = java.json()
dict_haskell = haskell.json()
dict_perl = perl.json()
dict_go = go.json()

# получение ключей
if dict_c.keys() == dict_java.keys() == dict_haskell.keys() == dict_perl.keys() == dict_go.keys():
    print('\nKeys for C, Java, Haskell, Perl and Go: ')
    print(dict_c.keys())
else:
    print('C, Java, Java, Perl and Go have different keys')

#вывод количества репрозоториев
print('\nTotal repositories returned for С: ', dict_c['total_count'])
print('Total repositories returned for Java: ', dict_java['total_count'])
print('Total repositories returned for Haskell: ', dict_haskell['total_count'])
print('Total repositories returned for Perl: ', dict_perl['total_count'])
print('Total repositories returned for Go: ', dict_go['total_count'])

#создание списка и определение количества репрозоториев по которым доступна информация
dict_cs = dict_c['items']
print('\nRepositories returned for C: ', len(dict_cs))

dict_javas = dict_java['items']
print('Repositories returned for Java: ', len(dict_java))

dict_haskells = dict_haskell['items']
print('Repositories returned for Haskell: ', len(dict_haskell))

dict_perls = dict_perl['items']
print('Repositories returned for Perl: ', len(dict_perl))

dict_gos = dict_go['items']
print('Repositories returned for Go: ', len(dict_go))

#анализ и вывод списка ключей для языков программирования C, Java, Perl, Haskell и Go.
dict_c = dict_cs[0]
dict_java = dict_javas[0]
dict_haskell = dict_haskells[0]
dict_perl = dict_perls[0]
dict_go = dict_gos[0]

if len(dict_c) == len(dict_java) == len(dict_haskell) == len(dict_perl) == len(dict_go):
    print('\nKeys for C, Java, Haskell, Perl and Go: ', str(len(dict_c)) + '. ')
    for key in sorted(dict_c.keys()):
        print(key)
    
else:
    print('\nKeys for C, Java, Haskell, Perl and Go: ', str(len(dict_c)) + ', ' + str(len(dict_java))+ ', '
          + str(len(dict_haskell)) + ', ' + str(len(dict_perl)) + ', ' + str(len(dict_go)))
    print('\nKeys C: ', len(dict_c))
    print('\nKeys Java: ', len(dict_java))
    print('\nKeys Haskell: ', len(dict_haskell))
    print('\nKeys Perl: ', len(dict_perl))
    print('\nKeys Go: ', len(dict_go))
    

#краткая информация о каждом репрозитории каждого языка
print('\nSelected information about each repository for language - C:')
for dict_c in dict_cs:
    print('\nName: ', dict_c['full_name'])
    print('Language: ', dict_c['language'])
    print('Stars: ', dict_c['stargazers_count'])
    print('Repository: ', dict_c['html_url'])
    print('Created: ', dict_c['created_at'])
    print('Updated: ', dict_c['updated_at'])
    print('Description: ', dict_c['description'])

print('\nSelected information about each repository for language - Java:')
for dict_java in dict_javas:
    print('\nName: ', dict_java['full_name'])
    print('Language: ', dict_java['language'])
    print('Stars: ', dict_java['stargazers_count'])
    print('Repository: ', dict_java['html_url'])
    print('Created: ', dict_java['created_at'])
    print('Updated: ', dict_java['updated_at'])
    print('Description: ', dict_java['description'])

print('\nSelected information about each repository for language - Haskell:')
for dict_haskell in dict_haskells:
    print('\nName: ', dict_haskell['full_name'])
    print('Language: ', dict_haskell['language'])
    print('Stars: ', dict_haskell['stargazers_count'])
    print('Repository: ', dict_haskell['html_url'])
    print('Created: ', dict_haskell['created_at'])
    print('Updated: ', dict_haskell['updated_at'])
    print('Description: ', dict_haskell['description'])

print('\nSelected information about each repository for language - Perl:')
for dict_perl in dict_perls:
    print('\nName: ', dict_perl['full_name'])
    print('Language: ', dict_perl['language'])
    print('Stars: ', dict_perl['stargazers_count'])
    print('Repository: ', dict_perl['html_url'])
    print('Created: ', dict_perl['created_at'])
    print('Updated: ', dict_perl['updated_at'])
    print('Description: ', dict_perl['description'])

print('\nSelected information about each repository for language - Go:')
for dict_go in dict_gos:
    print('\nName: ', dict_go['full_name'])
    print('Language: ', dict_go['language'])
    print('Stars: ', dict_go['stargazers_count'])
    print('Repository: ', dict_go['html_url'])
    print('Created: ', dict_go['created_at'])
    print('Updated: ', dict_go['updated_at'])
    print('Description: ', dict_go['description'])
    

#создание списка для переборки значений каждого языка программирования
plots_dicts_с = []
for dict_с in dict_cs:
    if dict_с['stargazers_count'] > 10000:
        plots_dict = {
            'value': dict_c['stargazers_count'],
            'xlink': dict_c['html_url']
            }
        plots_dicts_с.append(plots_dict)

plots_dicts_java = []
for dict_java in dict_javas:
    if dict_java['stargazers_count'] > 10000:
        plots_dict = {
            'value': dict_java['stargazers_count'],
            'xlink': dict_java['html_url']
            }
        plots_dicts_java.append(plots_dict)

plots_dicts_haskell = []
for dict_haskell in dict_haskells:
    if dict_haskell['stargazers_count'] > 10000:
        plots_dict = {
            'value': dict_haskell['stargazers_count'],
            'xlink': dict_haskell['html_url']
            }
        plots_dicts_haskell.append(plots_dict)

plots_dicts_perl = []
for dict_perl in dict_perls:
    if dict_perl['stargazers_count'] > 10000:
        plots_dict = {
            'value': dict_perl['stargazers_count'],
            'xlink': dict_perl['html_url']
            }
        plots_dicts_perl.append(plots_dict)

plots_dicts_go = []
for dict_go in dict_gos:
    if dict_go['stargazers_count'] > 10000:
        plots_dict = {
            'value': dict_perl['stargazers_count'],
            'xlink': dict_perl['html_url']
            }
        plots_dicts_go.append(plots_dict)

#построение визуализации
my_config = pygal.Config()
my_config.x_label_rotation = 90
my_config.title_font_size = 24
my_config.label_font_size = 9
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.width = 1200
chart = pygal.Bar(my_config)
chart.title = "Most C, Java, Haskell, Perl and Go projects on GitHub"

chart.add('С', plots_dicts_с)
chart.add('Java', plots_dicts_java)
chart.add('Haskell', plots_dicts_haskell)
chart.add('Perl', plots_dicts_perl)
chart.add('Go', plots_dicts_go)

chart.render_to_file('language_programm.svg')

