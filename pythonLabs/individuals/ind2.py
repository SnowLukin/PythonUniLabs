def individual_task_2():
    def print_matrix(matrix):
        print('\n'.join('\t'.join(map(str, row)) for row in matrix))
        print()

    class Matrix:
        def __init__(self, matrix):
            self.matrix = matrix

        def print_matrix(self):
            print('\n'.join('\t'.join(map(str, row)) for row in self.matrix))
            print()

        def change_size(self, i, j):
            current_columns = len(self.matrix[0])
            current_rows = len(self.matrix)

            if i == 0 or j == 0:
                self.matrix = []
                return
            # Changing rows
            if current_rows < i:
                for _ in range(0, i - current_rows):
                    self.add_row()
            elif current_rows > i:
                for _ in range(0, current_rows - i):
                    self.del_row(len(self.matrix) - 1)
            # Changing columns
            if current_columns < j:
                for _ in range(0, j - current_columns):
                    self.add_column()
            elif current_columns > j:
                for _ in range(0, current_columns - j):
                    self.del_column(len(self.matrix[0]) - 1)
        def add_column(self):
            self.matrix = [row + [0] for row in self.matrix]

        def add_row(self):
            self.matrix.append([0 for _ in range(len(self.matrix[0]))])

        def del_column(self, i):
            self.matrix = [row[: i] + row[i + 1:] for row in self.matrix]

        def del_row(self, i):
            self.matrix = self.matrix[:i] + self.matrix[i + 1:]

        def sub_matrix(self, start_row, end_row, start_column, end_column):
            return [[self.matrix[i][j] for j in range(start_column, end_column + 1)] for i in range(start_row, end_row + 1)]
    entity = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Initial matrix")
    entity.print_matrix()
    print("Changed size")
    entity.change_size(2, 2)
    entity.print_matrix()
    entity.add_column()
    entity.add_row()
    entity.print_matrix()
    print("Sub matrix")
    sub_matrix = entity.sub_matrix(1, 2, 1, 2)
    print_matrix(sub_matrix)

    print("Delete column")
    entity.del_column(0)
    entity.print_matrix()

    print("Delete row")
    entity.del_row(1)
    entity.print_matrix()