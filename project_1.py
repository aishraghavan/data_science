from pandas import *

def create_data():
    d = {'name': Series(['Jon', 'Sam', 'Ben', 'Frank', 'Bob'], index=['a', 'b', 'c', 'd', 'e']),
        'age': Series([22,34,56,12,56], index=['a', 'b', 'c', 'd', 'e']),
        'fare': Series([23,12,4.5,8.2], index=['a', 'b', 'c', 'e']),
        'survived': Series([False, True, False, True, True],index=['a', 'b', 'c', 'd', 'e'])
        }
    df = DataFrame(d)
    return df

if __name__ == "__main__":
    d = create_data()
    print d
    print d['name']
    print d[['name', 'age']]
    print d.loc['a']


HDF Group
