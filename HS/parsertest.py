import yaml
from pathlib import Path
import zipfile
import sys
from kafka import KafkaProducer
import argparse
from pprint import pprint
import json
import re
from jsonschema import validate
import ast


def get_config(yaml_file):
    with open(yaml_file) as f:
        configs = yaml.load(f)
    return configs

def sanitize_field_name(key,
                        prefix=None):
    if prefix is not None:
        key = '{}_{}'.format(prefix, key)
    return re.sub('[^\w.]', '', str(key))

def json_parser(data,
                keys=None,
                prefix=None):
    out = {}
    outlist = []
    for key in keys:
        if type(key) == dict:
            keys_local = key[key.keys()[0]]
            if key.keys()[0] in data:
                if type(data[key.keys()[0]]) == list:
                    outback = {}
                    for item in data[key.keys()[0]]:
                        out_local = json_parser(item,
                                                keys_local,
                                                key.keys()[0])
                        if out_local != [{}]:
                            if prefix is None:
                                outback['card'] = out_local
                            else:
                                outback.update(out_local)
                    outlist.append(outback)
                    out = outlist
                elif key.keys()[0] == 'card':
                    outback = {}
                    out_local = json_parser(data[key.keys()[0]],
                            keys_local,
                            key.keys()[0])
                    print 'ABAIXO'
                    print out_local
                    print prefix
                    out['card'] = out_local
                else:
                    out_local = json_parser(data[key.keys()[0]],
                                                 keys_local,
                                                 key.keys()[0])
                    out.update(out_local)
        else:
            try:
                if data.get(key) is not None:
                    if type(data[key]) == list or type(data[key]) == dict:
                        out[sanitize_field_name(key, prefix)] = str(data[key])
                    else:
                        out[sanitize_field_name(key, prefix)] = data[key]
            except Exception as e:
                msg = 'Cant parse data {} - {}'.format(e, data)
                print e
    print out
    return out


def parser(data):
    batch_json = {}
    games_json = {}
    card_history_json = {}
    card_json = {}
    games_keys = ['range_start','range_end']
    card_history_keys = ['user_hash','added']
    card_keys = ['user_hash','added','player','card_counter']
    #batch['range_start'] = data
    #batch['range_end']
    #batch['unique_users'] 
    #batch['total_games']
    #print data
    for batch in data:
        batch = batch.encode('ascii')
        if type(data[batch]) not in [list,dict]:
            batch_json[batch] = str(data[batch]).encode('ascii')
        else:
            for games in data[batch]:
                for key in games_keys:
                    games_json[key] = batch_json[key]
                for game in games:
                    game = game.encode('ascii')
                    if type(games[game]) not in  [list,dict]:
                        games_json[game] = str(games[game]).encode('ascii')
                    else:
                        card_counter = 0
                        for card_histories in games[game]:
                            for key in card_history_keys:
                                card_history_json[key] = games_json[key]
                            card_history_json['card_counter'] = card_counter
                            card_counter+=1
                            for card_history in card_histories:
                                card_history = card_history.encode('ascii')
                                if type(card_histories[card_history]) not in (list,dict):
                                    card_history_json[card_history] = str(card_histories[card_history]).encode('ascii')
                                else:
                                    for card in card_histories[card_history]:
                                        for key in card_keys:
                                            card_json[key] = card_history_json[key]
                                        card = card.encode('ascii')
                                        card_json[card] = str(card_histories[card_history][card]).encode('ascii')
                                    
                                    #print card_json
                            #print card_history_json        
                #print games_json                    
    print batch_json
                                    

                #print a
                #print item2
                #print type(item2)
                #for item3 in item2: 
                    #item3 = item3.encode('utf-8')
                    #print item2[item3]
                    #print type(item3)
                    #if type(item3) not in [list,dict]:
                    #    games_json[item3] = item2[item3]
    
                        

def neongenesisevangelionparsa(data, objname = None, previous_output = None):
    games = ['range_start','range_end']
    card_history = ['user_hash','added']
    card = ['user_hash','added','player','card_counter']
    output = {}
    card_counter = 0
    if type(data) == dict:
        for items in data:
            if objname:
                for key in eval(objname):
                    output[key] = previous_output[key]
                if 'card_counter' not in eval(objname):
                    output['card_counter'] = card_counter
                    card_counter+=1
            items = items.encode('ascii')
            if type(data[items]) not in [list,dict]:
                output[items] = str(data[items]).encode('ascii')
            else:
                neongenesisevangelionparsa(data[items], items, output)
        print output
    elif type(data) == list:
        for items in data:
            if objname:
                for key in eval(objname):
                    output[key] = previous_output[key]
                if 'card_counter' not in eval(objname):
                    output['card_counter'] = card_counter
                    card_counter+=1
            for item in items:
                item = item.encode('ascii')
                if type(items[item]) not in [list,dict]:
                    output[item] = str(items[item]).encode('ascii')
                else:
                    neongenesisevangelionparsa(items[item], item, output)
            print output




def neongenesisevangelionparsa2(data, objname = None, previous_output = None):
    games = ['range_start','range_end']
    card_history = ['user_hash','added']
    card = ['user_hash','added','player','card_counter']
    output = {}
    card_counter = 0    
    for items in data:
        if objname:
            for key in eval(objname):
                output[key] = previous_output[key]
            if 'card_counter' not in eval(objname):
                output['card_counter'] = card_counter
                card_counter+=1
        if type(data) == dict:
            items = items.encode('ascii')
            if type(data[items]) not in [list,dict]:
                output[items] = str(data[items]).encode('ascii')
            else:
                neongenesisevangelionparsa2(data[items], items, output)
        elif type(data) == list:
            for item in items:
                item = item.encode('ascii')
                if type(items[item]) not in [list,dict]:
                    output[item] = str(items[item]).encode('ascii')
                else:
                    neongenesisevangelionparsa2(items[item], item, output)
            print output
    print output

def main():
    #parser = argparse.ArgumentParser(description='Rides events aggregate.')

    #parser.add_argument('-t', '--topic', metavar='<topic>', type=str,
    #                    required=True,
    #                    help='Kafka topic name.')

    #parser.add_argument('-K', '--kafka_host', metavar='<host>', type=str,
    #                    required=True,
    #                    help='Kafka host list.')

    #args = parser.parse_args()

    #topic = args.topic
    #host = args.kafka_host
    
    #producer = KafkaProducer(bootstrap_servers=host)
    
    #while True:
    zippath = Path('/home/eduardo/personal_git/HS_samples/Extract/HearthScry/').glob('**/*.zip')
    zips = [x for x in zippath]
    for z in zips:
        filedir = str(z).replace('.zip','')
        with zipfile.ZipFile(str(z), 'r') as zip_ref:
            zip_ref.extractall(filedir)
        filepath = Path(filedir).glob('**/*.json')
        files = [x for x in filepath]
        for f in files:
            with open(str(f)) as jsonfile:
                data = json.load(jsonfile)
        with open('/home/eduardo/personal_git/HS_samples/HS/hearthscryschema.json') as schemafile:
                schema = json.load(schemafile)
        try:
            validate(data,schema)
        except Exception as e:
            print 'error'
        neongenesisevangelionparsa2(data)
        #parser(data)

        

        #for finfo in zipped.infolist():
        #    ifile = zipped.open(finfo)
        #    line_list = ifile.readlines()
        #    print line_list

        #message = raw_input("Input message:")
        #response = producer.send(topic, message)
        #print response

if __name__ == "__main__":
    main()
