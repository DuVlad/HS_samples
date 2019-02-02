import yaml
from pathlib import Path
import zipfile
import sys
from kafka import KafkaProducer
import argparse
from pprint import pprint
import json
import re


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
    zippath = Path('/home/eduardo/personal_git/Extract/HearthScry/').glob('**/*.zip')
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
            yaml = get_config('/home/eduardo/personal_git/HS/hearthscry.yaml')
            for key, config in yaml.iteritems():
                a = json_parser(data,config.get('fields'))
        #for finfo in zipped.infolist():
        #    ifile = zipped.open(finfo)
        #    line_list = ifile.readlines()
        #    print line_list

        #message = raw_input("Input message:")
        #response = producer.send(topic, message)
        #print response

if __name__ == "__main__":
    main()
