from sort import sort,get_da
from viev import get_data,get_number_operation
from write_read_file import read_file,write_file
from main import sort_data


def button():
    return sort_data(get_number_operation,read_file,write_file,sort,get_da,get_data)