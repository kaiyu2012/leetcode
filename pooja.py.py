from flask import Flask, request
import hashlib
import random
import re
import json
def specific_string(length, data):
    integrity = ''.join((random.choice(data)) for x in range(length))
    return integrity


def hash_string(string):
    hash_val = hashlib.sha256()
    hash_val.update(string.encode())
    return hash_val.hexdigest()


def create_matrix(data: list):
    for d in data:
        if type(d) != int:
            raise ValueError('Error')
    left_col_rows = [1, 2, 3, 4, 5, 6]
    col_15_rows = [7, 8, 9]
    right_col_rows = [10, 11, 12, 13, 14, 15]
    ptr = 0
    nulls = [None, None, None]
    out = []
    for i in range(1, 16):
        if i in left_col_rows:
            tmp = data[ptr: ptr + 9]
            tmp.extend(nulls)
        elif i in col_15_rows:
            tmp = data[ptr: ptr + 15]
        if i in right_col_rows:
            tmp = nulls
            tmp.extend(data[ptr: ptr + 9])
        ptr = ptr + 9
        out.append(tmp)
    print(f'DATA: {out}')
    return out


def reverse_matrix(matrix):
    out = []
    for row in matrix:
        for element in row:
            if element is not None:
                out.append(element)
    return out


def matrix_transpose_hash(matrix):
    string = ''
    for i in range(0, 15):
        for j in range(0, 15):
            if matrix[i][j] is None:
                string = string + "0"
            else:
                string = string + str(matrix[i][j])
    return specific_string(8, hash_string(string))

def check_for_insertion(matrix, row: int, col: int, value: int):
    flag = True
    if value < 0:
        return {
            'status': 'error: invalid value'
        }
    if (row in range(9, 15) and col in range(0, 6)) or (col in range(9, 15) and col in range(0, 6)):
        return {
            'status': 'error: invalid cell reference'
        }
    if matrix[row][col] is not None and matrix[row][col] < 0:
        return {
            'status': 'error: attempt to change fixed hint'
        }
    for i in range(0, 15):
        if matrix[row][i] == value or matrix[i][col] == value:
            flag = False
    if flag:
        return {
            'status': 'ok',
            'grid': reverse_matrix(matrix),
            'integrity': matrix_transpose_hash(matrix)
        }
    else:
        return {
            'status': 'warning',
            'grid': reverse_matrix(matrix),
            'integrity': matrix_transpose_hash(matrix)
        }
        
        
def _insert(parms):
    
    parms = ['op', 'value', 'grid', 'integrity', 'cell']

    
    cell = parms['cell']
    row_pos = 0
    col_pos = 0
    reg = r'^[rR][0-9]+[cC][0-9]+$'
    if re.match(reg, cell) is None:
        return f'Invalid cell position {cell}'
    parts = cell.split('c')
    if len(parts) == 1:
        parts = cell.split('C')
        if len(parts) == 1:
            return "Invalid cell value"
    row_pos = int(parts[0][1:])
    col_pos = int(parts[1])
    grid = json.loads(parms['grid'])
    if type(grid) != list:
        return 'Invalid list'
    if len(grid) != 153:
        return 'Grid must be of size 153'
    try:
        matrix = create_matrix(grid)
    except ValueError:
        return {
            'status': 'error: invalid grid value'
        }
    if 'cell' not in parms:
        return {
            'status': 'error: missing cell reference'
        }
    op = parms['op']
    if op != 'insert':
        return f'Invalid operation {op}'
    try:
        value = int(parms['value'])
    except ValueError:
        return {
            'status': 'error: invalid value'
        }
    integrity = parms['integrity']
    response = check_for_insertion(matrix, row_pos, col_pos, value)
    print(grid)
    print(parms)
    return