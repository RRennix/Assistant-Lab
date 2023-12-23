import yaml
data = yaml.safe_load(open('path.yml','r',encoding='utf-8').read())
for Aplicativo in data['Aplicativos']:
    print(Aplicativo)