def main():
    my_personal_info = {
        'name': 'Jay',
        'student_id': '10267249',
        'Pizza_Toppings': [
            'Onions',
            'mushroom',
            'pepper'
        ],
        'fav_movies': [
            {'name': 'Avengers',
             'genre': 'Sci-Fiction'
            },
            {'name': 'RRR',
             'genre': 'Action'
            }
        ]
    }

    new_movie = {
        'name': 'A-team',
        'genre': 'Action'
    }
    my_personal_info['fav_movies'].append(new_movie)


    extra_toppings = {'paneer', 'corn'}
    add_toppings(my_personal_info['Pizza_Toppings'], extra_toppings)

def add_toppings(my_personal_info, extra_toppings):
    for t in extra_toppings:
        my_personal_info['Pizza_Toppings'].append(t)         
        
    print('Hi Joe, my name is ' + my_personal_info['name'] + ', ' + 'and my student ID is ' + my_personal_info[str['student_id']] + '.')
    
    print('My ideal pizza has ' + my_personal_info['Pizza_Toppings'][0], my_personal_info['Pizza_Toppings'][1], my_personal_info['Pizza_Toppings'][2], my_personal_info['Pizza_Toppings'][3], my_personal_info['Pizza_Toppings'][4] + '.')

    print('I like to watch ' + my_personal_info['fav_movie'][0]['genre'], my_personal_info['fav_movie'][1]['genre'], 'and',my_personal_info['fav_movie'][2]['genre'], 'movies.')

    print('Some of my favourites are ' + my_personal_info['fav_movie'][0]['name'], my_personal_info['fav_movie'][1]['name'], my_personal_info['fav_movie'][2]['name'] + ' !' )


main()    