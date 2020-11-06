from src.utils import f

a = '''
{
  "user": {
    "posts": [
      {"title": "Foo", "comments": ["Good one!", "Interesting..."]},
      {"title": "Bar", "comments": ["Ok"]},
      {"title": "Baz", "comments": []}
    ]
  }
}
'''

def test_valid_user():
    b = ['user']
    assert(f(a,b) == {'user': {"posts": [{"title": "Foo", "comments": ["Good one!", "Interesting..."]}, {"title": "Bar", "comments": ["Ok"]}, {"title": "Baz", "comments": []}]}})
    
def test_valid_posts():
    b = ['user.posts']
    assert(f(a,b) == {'user.posts': [{"title": "Foo", "comments": ["Good one!", "Interesting..."]}, {"title": "Bar", "comments": ["Ok"]}, {"title": "Baz", "comments": []}]})

def test_valid_first_title():
    b = ['user.posts[0].title']
    assert(f(a,b) == {'user.posts[0].title': 'Foo'})
    
def test_valid_last_title():
    b = ['user.posts[2].title']
    assert(f(a,b) == {'user.posts[2].title': 'Baz'})
    
def test_valid_first_comment():
    b = ['user.posts[0].comments[0]']
    assert(f(a,b) == {'user.posts[0].comments[0]': 'Good one!'})
    
def test_valid_last_comment():
    b = ['user.posts[0].comments[1]']
    assert(f(a,b) == {'user.posts[0].comments[1]': 'Interesting...'})
    
def test_valid_single_comment():
    b = ['user.posts[1].comments[0]']
    assert(f(a,b) == {'user.posts[1].comments[0]': 'Ok'})
    
def test_valid_no_comment():
    b = ['user.posts[2].comments[0]']
    assert(f(a,b) == {})
    
def test_invalid_post_title_under():
    b = ['user.posts[-1].title']
    assert(f(a,b) == {})
    
def test_invalid_post_title_over():
    b = ['user.posts[3].title']
    assert(f(a,b) == {})
    
def test_invalid_post_comment_under():
    b = ['user.posts[-1].comments[0]', 'user.posts[-1].comments[-1]', 'user.posts[-1].comments[1]']
    assert(f(a,b) == {})
    
def test_invalid_post_comment_over():
    b = ['user.posts[3].comments[0]', 'user.posts[3].comments[-1]', 'user.posts[3].comments[1]']
    assert(f(a,b) == {})
