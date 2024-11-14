
def is_cell_alive(value : int) -> bool:
    if (int(value) == 1):
        return True
    return False

def get_next_cell_value(current_value : int, neighbors_numbers : int) -> int :
    
    match current_value:
        case 0:
            if (neighbors_numbers == 3):
                return 1
            return 0
        case 1:
            if (neighbors_numbers > 3 or neighbors_numbers < 2):
                return 0
            return 1


def get_next_cell_index (index_cell : int, index_current_cell : int, number_lines : int) -> int:
    
    result = index_current_cell - index_cell
    if (result == number_lines + 1 or result == number_lines):
       return index_cell + 1
    elif (result == number_lines - 1):
        return index_current_cell - 1
    elif (result == 1 or result == 0):
        return index_current_cell + 1
    elif (result == -1):
        return index_current_cell + number_lines - 1
    elif (result == 1 - number_lines or result == -number_lines):
        return index_cell + 1
    
    return -1
          
def get_next_cell(index_current_cell : int, board : list, index_cell : int, number_lines : int) -> tuple:
    
    next_index = get_next_cell_index(index_cell, index_current_cell, number_lines)
    if (index_cell != index_current_cell):
        if (is_cell_alive(board[index_cell])):
            return True, next_index
        return False, next_index
    return False, next_index

def is_board_sucessor(input_board : list, output_board : list, dimensions : list):
    
    
    is_sucessor = True
    for index, line in enumerate(output_board):
        if (index >= int(dimensions[1])) and (index % int(dimensions[1]) != 0) and ((index + 1) % int(dimensions[1]) != 0) and (index <= (int(dimensions[0]) * int(dimensions[1]) - int(dimensions[1]))):  
            number_of_alive_cells = 0
            next_cell_index = index - int(dimensions[1]) - 1
            for i in range(0, 8):
                prev_cell_index = next_cell_index
                is_cell_alive, next_cell_index = get_next_cell(index, output_board, next_cell_index, int(dimensions[1]))
                if is_cell_alive:
                    number_of_alive_cells += 1
            
            cell_value = get_next_cell_value(int(line), number_of_alive_cells)
            
            if cell_value != int(input_board[index]):
                import ipdb
                ipdb.set_trace()
                is_sucessor = False
                print("O tabuleiro de entrada não é gerado pelo de saída...", sep='\n')
                break
    print('dfas')
    if is_sucessor:
        print("O tabuleiro de entrada é gerado pelo de saída...", sep='\n')
        

        