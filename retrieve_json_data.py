from github import Github
from src.utils import f

import json
import csv

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file) 
    
    output_file = config['output_file']
    keys = config['keys']
    
    if output_file:
        writer = csv.DictWriter(open(output_file, 'w'), keys)
        writer.writeheader()
        
    g = Github(config['github_token'])
    repo = g.get_repo(config['repo_id'])
    files = repo.get_contents(config['file_directory'], ref = 'master')
        
    for file in files:
        data = file.decoded_content.decode('utf-8')
        ret = f(data, keys)
        print(ret)
        if output_file:
            writer.writerow(ret)