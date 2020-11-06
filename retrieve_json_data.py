from github import Github
from src.utils import f

import argparse
import json
import csv

def retrieve_json_data():
    parser = argparse.ArgumentParser(description = 'Retrieve specific keys from JSON files in public Github repositories.')
    parser.add_argument('--config', default = './config.json', help = 'Path to the config file')
    args = parser.parse_args()
    
    with open(args.config, encoding='utf-8') as config_file:
        config = json.load(config_file) 
        
        # Optional csv output file, might be blank.
        output_file = config['output_file']
        output_console = config['output_console']
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
            if output_console:
                print(ret)
            if output_file:
                writer.writerow(ret)
                
if __name__ == "__main__":
    retrieve_json_data()