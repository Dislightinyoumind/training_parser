from Lib.pre_parser import read_file, check_input
from Lib.parser import parsing_function
from Lib.post_parser import frame_creation



def pars_process(filename, key_words_for_delete=["WEFAC"],):
    read_input_file = read_file(filename)
    check_file=check_input(read_input_file)
    clean_file = parsing_function(check_file, key_words_for_delete)
    df_file = frame_creation(clean_file)
    return df_file


filename = 'input_data/input.inc'

if __name__ == '__main__':
    output_df = pars_process(filename, key_words_for_delete=["WEFAC"])
    output_df.to_excel('output_data/output_file.xlsx')