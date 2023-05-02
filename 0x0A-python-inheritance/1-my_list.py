#!/usr/bin/python3
''' defines from  1-my_list '''


class MyList(list):
    ''' Represents the class MyList '''

    def print_sorted(self):
        ''' prints our the list '''
        print(sorted(self))
