import numpy as np
import json

def get_rasyid_bio():

    name = 'Lathif Al Rasyid'
    age = 24
    address = 'Gang Wisnu No 18 Gandok Concat Depok Sleman DIY'
    hobbies = ['Membaca Buku', 'Koding', 'Menonton Anime']
    is_married = False
    list_school = {
        'SD':{
            'name':'SDN 1 Surodakan',
            'year_in':2002,
            'year_out':2008,
            'major':np.nan
        },
        'SMP':{
            'name':'SMPN 1 Trenggalek',
            'year_in':2008,
            'year_out':2011,
            'major':np.nan
        },
        'SMA':{
            'name':'SMAN 2 Trenggalek',
            'year_in':2011,
            'tear_out':2014,
            'major':'IPA'
        },
        'Univ':{
            'name':'Universitas Negeri Yogyakarta',
            'year_in':2014,
            'year_out':2018,
            'major':'Matematika'
        }
    }
    skills = {
        'Python':'advanced',
        'Matlab':'advanced',
        'Java':'beginner'
    }
    interest_in_coding = True

    wrapped_bio = {
        'name':name,
        'age':age,
        'address':address,
        'hobbies':hobbies,
        'is_married':is_married,
        'list_school':list_school,
        'skills':skills,
        'interest_in_coding':interest_in_coding
    }

    json_bio = json.dumps(wrapped_bio)

    return json_bio


if __name__ == '__main__':
    rasyid_bio = get_rasyid_bio()
    print(rasyid_bio)
