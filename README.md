
# JSON Data Retriever

A tool to obtain specific keys from JSON files in public Github repositories.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- pip
- virtualenv

To get **pip**: download [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
```
python get-pip.py
```
Pip is now installed!

To get **virutalenv**: 
```
pip install virtualenv
``` 

### Installing

Create a new virtual environment:
```
virtualenv -p python3 venv
```

Start the virtual environment:
```
source venv/bin/activate
```    
Install requirements with pip:
```
pip install -r requirements.txt
```

### Configuring

Go through **config.json**:
- **github_token**: your github token, you can create a github token by going to Github -> Settings -> Personal access tokens -> Generate new token.
- **repo_id**: the ID of the public github repository you want to query. *Default*: mitre/cti.
- **file_directory**: The directory within the repository that contains the JSON files we want to query. *Default*: /enterprise-attack/attack-pattern/.
- **keys**: the keys you want to access within the JSON files. *Default*: 'id', 'objects[0].name', 'objects[0].kill_chain_phases'. 
- **output_file**: you can save the results in a csv as well, this field is optional, you can just leave it blank, and no csv will be created. *Default*: ./output/output.csv 

### Running

Once the configuration phase is complete, you can run the script:
```
python retrieve_json_data.py
```

### Testing

You can run the tests by typing:

```
pytest -v ./tests
```

## Built With

* [PyGithub](https://github.com/PyGithub/PyGithub) - Python library to access the GitHub API v3 and Github Enterprise API v3.

## Authors

* **Jonathan Perkes** - jonathanperkes@gmail.com