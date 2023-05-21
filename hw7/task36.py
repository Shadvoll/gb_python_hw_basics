def calc_operation_table(opertation, num_rows=6, num_columns=6):
    def helper(opertation, num_rows, num_columns):
        return [
            [opertation(i, j) for j in range(1, num_columns+1)] for i in range(1, num_rows+1)
        ]
    table = helper(opertation, num_rows, num_columns)
    for row in table:
        for elem in row:
            print(elem, end='\t')
        print()


calc_operation_table(lambda x, y: x*y)

