from pathlib import Path
import zipfile
import argparse
import json
from jsonschema import validate
import Producer
import shutil
from collections import OrderedDict
import pubsub_publisher


def parser(data, objname = None, previous_output = None):
    games = ['range_start','range_end']
    card_history = ['user_hash','added']
    card = ['user_hash','added','player','card_counter']
    output = {}
    card_counter = 0    
    for items in data:
        if objname and previous_output:
            output['table'] = objname 
            for key in eval(objname):
                output[key] = previous_output[key]
            if 'card_counter' not in eval(objname):
                output['card_counter'] = card_counter
                card_counter+=1
        else:
            output['table'] = 'batch'
        #if type(data) == dict:
        if isinstance(data, dict):
            items = items.encode('ascii')
            if not isinstance (data[items], list) and not isinstance(data[items], dict):
                output[items] = str(data[items]).encode('ascii')
            else:
                parser(data[items], items, output)
        elif isinstance(data, list):
            for item in items:
                item = item.encode('ascii')
                if not isinstance (items[item], list) and not isinstance(items[item], dict):
                    output[item] = str(items[item]).encode('ascii')
                else:
                    parser(items[item], item, output)
            print output
            #Producer.produce(output['table'], output)
            pubsub_publisher.produce(output['table'], output)
    if isinstance(data, dict):
        print output
        #Producer.produce(output['table'],output)
        pubsub_publisher.produce(output['table'], output)
                        
    
def main():
    #while True:
    zippath = Path('/home/eduardo/personal_git/HS_samples/Extract/HearthScry/').glob('**/*.zip')
    zips = [x for x in zippath]
    for zip in zips:
        filedir = str(zip).replace('.zip','')
        with zipfile.ZipFile(str(zip), 'r') as zip_ref:
            zip_ref.extractall(filedir)
        filepath = Path(filedir).glob('**/*.json')
        files = [x for x in filepath]
        for f in files:
            with open(str(f)) as jsonfile:
                data = json.load(jsonfile, object_pairs_hook=OrderedDict)
        with open('/home/eduardo/personal_git/HS_samples/HS/hearthscryschema.json') as schemafile:
                schema = json.load(schemafile)
        try:
            validate(data,schema)
        except Exception as e:
            print 'error'
        parser(data)
        shutil.move(str(zip), '/home/eduardo/personal_git/HS_samples/Data/HearthScry/')
        shutil.rmtree(filedir)


if __name__ == "__main__":
    main()
