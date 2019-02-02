import yaml

with open('/home/eduardo/personal_git/HS/hearthscry.yaml') as f:
	configs = yaml.load(f)

print(configs)