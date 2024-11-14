def read_board(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        line_string = []
        for index, line  in enumerate(lines):
            line = line.strip()
            if index == 0:
                board_dimensions = line.split(' ')
                continue
            line_string += line.split(' ')
    
    return line_string, board_dimensions



                          