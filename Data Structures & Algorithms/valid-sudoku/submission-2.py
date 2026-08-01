class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = "123456789"
        # Check 1: Row contains 1-9 w/o duplicates
        for row in board:
            elem_list = []
            for elem in row:
                if elem not in elem_list and elem in numbers:
                    elem_list.append(elem)
                elif elem in elem_list:
                    return False

        # Check 2: Each column contains 1-9 w/o duplicates
        for i in range(9):
            elem_list = []
            for row in board:
                if row[i] not in elem_list and row[i] in numbers:
                    elem_list.append(row[i])
                elif row[i] in elem_list:
                    return False

        # Check 3: Sub-boxes only contain 1-9 w/o duplicates
        sets = [[1,2,3],[4,5,6],[7,8,9]]
        # need to iterate through rows of board and columns
        #use mod 3. 0 mod 3
        """
        boxes list looks like       0 | 1 | 2
                                    3 | 4 | 5
                                    6 | 7 | 8
        """
        boxes = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:""}
        for row in range(9):
            for col in range(9):
                if row in range(0,3) and col in range(0,3):
                    #0
                    if board[row][col] != ".":
                        boxes[0] += board[row][col]
                elif row in range(0,3) and col in range(3,6):
                    #1
                    if board[row][col] != ".":
                        boxes[1] += board[row][col]
                elif row in range(0,3) and col in range(6,9):
                    #2
                    if board[row][col] != ".":
                        boxes[2] += board[row][col]
                elif row in range(3,6) and col in range(0,3):
                    #3
                    if board[row][col] != ".":
                        boxes[3] += board[row][col]
                elif row in range(3,6) and col in range(3,6):
                    #4
                    if board[row][col] != ".":
                        boxes[4] += board[row][col]
                elif row in range(3,6) and col in range(6,9):
                    #5
                    if board[row][col] != ".":
                        boxes[5] += board[row][col]
                elif row in range(6,9) and col in range(0,3):
                    #6
                    if board[row][col] != ".":
                        boxes[6] += board[row][col]
                elif row in range(6,9) and col in range(3,6):
                    #7
                    if board[row][col] != ".":
                        boxes[7] += board[row][col]
                elif row in range(6,9) and col in range(6,9):
                    #8
                    if board[row][col] != ".":
                        boxes[8] += board[row][col]
        for k,v in boxes.items():
            print((k,v))
            if len(set(v)) != len(v):
                return False
        return True
