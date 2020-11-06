from src.utils import f

a = ''' 
{
    "guid": "1234",
    "content": {
    "type": "text/html",
    "title": "Challenge 1",
    "entities": [ "1.2.3.4", "wannacry", "malware.com"]
    },
    "score": 74,
    "time": 1574879179
}
'''
    
def test_valid_non_nested():
    b = ['guid', 'score', 'time']
    assert(f(a,b) == {'guid': '1234', 'score': 74, 'time': 1574879179})
    
def test_invalid_non_nested():
    b = ['guid', 'score', 'time', 'date']
    assert(f(a,b) == {'guid': '1234', 'score': 74, 'time': 1574879179})
    
def test_valid_nested():
    b = ['content.type', 'content.title']
    assert(f(a,b) == {'content.type': 'text/html', 'content.title': 'Challenge 1'})
    
def test_invalid_nested_1():
    b = ['content.type', 'content.title', 'score.time']
    assert(f(a,b) == {'content.type': 'text/html', 'content.title': 'Challenge 1'})
    
def test_invalid_nested_2():
    b = ['content.type', 'content.title', 'content.date']
    assert(f(a,b) == {'content.type': 'text/html', 'content.title': 'Challenge 1'})
    
def test_valid_nested_indexed_first():
    b = ['content.entities[0]']
    assert(f(a,b) == {'content.entities[0]': '1.2.3.4'})
    
def test_valid_nested_indexed_last():
    b = ['content.entities[2]']
    assert(f(a,b) == {'content.entities[2]': 'malware.com'})
    
def test_invalid_nested_indexed_over():
    b = ['content.entities[0]', 'content.entities[3]']
    assert(f(a,b) == {'content.entities[0]': '1.2.3.4'})    
    
def test_invalid_nested_indexed_under():
    b = ['content.entities[0]', 'content.entities[-1]']
    assert(f(a,b) == {'content.entities[0]': '1.2.3.4'})
