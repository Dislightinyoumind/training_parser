# -*- coding: utf-8 -*-
import re
from typing import List, Tuple, Any, Union





def read_input(path: str, mode: str, enc: str) -> str:
    '''
    The function that reads the input file.inc and converts it to a string
    :param path: road to the input file.inc
    :param mode: reading mode
    :param enc: encoding
    :return: string with input text
    '''
    with open(path, mode, encoding=enc) as file:
        text = file.read()

    return text


def check_input(text: str) -> bool:
    '''
    The function of checking the emptiness of the input file.inc
    :param text: input text from file.inc
    :return:availability check
    '''

    if text == "":
        Availability = False
    else:
        Availability = True
    return Availability


def cleaning_input(text: str) -> str
    """

    :param text: 
    :return: 
    """
    cleaning_comments = re.sub(r"--.+\n", r"\n", text)
    cleaning_extra_spaces = re.sub(r"\s*\n+", "\n", cleaning_comments)

    return cleaning_extra_spaces