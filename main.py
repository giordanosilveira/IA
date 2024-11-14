import sys
import file
import game_life

# i % coluna == coluna
# i / coluna == linha


VIZINHOS = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1],
]



if __name__ == '__main__':
    
    if len(sys.argv) < 1:
        print("Usage: python main.py <file_name>")
        exit(1)
    
    file_name = sys.argv[1]
        
    board_input, board_dimensions = file.read_board(f"./inputs/{file_name}")
    print(board_input, board_dimensions)
    
    # board_output, board_dimensions = file.read_board(f"./outputs/{file_name}")
    # print(board_output, board_dimensions)
    
    alive_cells = 0
    next_index = int(board_dimensions[1])
    
    # game_life.is_board_sucessor(board_input, board_output, board_dimensions)
    