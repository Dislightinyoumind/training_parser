# -*- coding: utf-8 -*-
import re


def read_file(filename):
    """
    The function reads the input file into a list
    :param filename: input file
    :return: reading
    """
    with open(filename, encoding='UTF-8') as f:
        input_file = f.read().splitlines()
    return input_file


def check_input(input_file):
    '''
    The function of checking the emptiness of the input file.inc
    :param input_file: input text from file.inc
    :return:availability check
    '''

    if input_file == "":
        Availability = False
    else:
        Availability = input_file
    return Availability


def cleaning_input_file(input_file):
    """
    Cleaning the file from garbage
    :param input_file:
    :return:
    """
    input_file_cleared = []
    for i in input_file:
        a = i.split('--')[0]
        a = re.sub('\t', ' ', a)
        a = re.sub('/', '', a)
        a = re.sub("'", '', a)

        input_file_cleared.append(a)
    return input_file_cleared

def clean_file(input_file_cleared):
    """
    :param input_file_cleared:
    :return: input file without void
    """
    input_file_without_void=[]
    space=[i*' ' for i in range(100)]
    for i in input_file_cleared:
        if i!='' and i not in space:
            input_file_without_void.append(i)
    return input_file_without_void
