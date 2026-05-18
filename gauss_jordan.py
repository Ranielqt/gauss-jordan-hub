import copy

class GaussJordanSolver:
    """
    A modular class to solve systems of linear equations using the 
    Gauss-Jordan elimination method.
    """

    def __init__(self, matrix):
        """
        Initialize with an augmented matrix [A|b].
        :param matrix: List of lists (e.g., [[2, 1, 8], [3, -1, 7]])
        """
        self.matrix = copy.deepcopy(matrix)
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.steps = []

    def solve(self):
        """
        Executes the Gauss-Jordan elimination algorithm.
        :return: (success: bool, final_matrix: list, steps: list, result: list)
        """
        # Record initial state
        self._record_step("Initial augmented matrix")

        pivot_row = 0
        for j in range(self.cols - 1): # Iterate through each variable column
            if pivot_row >= self.rows:
                break
                
            # 1. Partial Pivoting (Find the row with the largest absolute value in the current column)
            max_val = abs(self.matrix[pivot_row][j])
            max_row = pivot_row
            for i in range(pivot_row + 1, self.rows):
                if abs(self.matrix[i][j]) > max_val:
                    max_val = abs(self.matrix[i][j])
                    max_row = i
                    
            # Check if column is zero (singular)
            if max_val < 1e-10:
                continue 
                
            # 2. Swap Rows if necessary
            if max_row != pivot_row:
                self.matrix[pivot_row], self.matrix[max_row] = self.matrix[max_row], self.matrix[pivot_row]
                self._record_step(f"Swap Row {pivot_row + 1} and Row {max_row + 1}")
                
            # 3. Scale Pivot Row to 1
            pivot_element = self.matrix[pivot_row][j]
            self.matrix[pivot_row] = [x / pivot_element for x in self.matrix[pivot_row]]
            self._record_step(f"Normalize Row {pivot_row + 1} (Divide by {pivot_element:.3f})")
            
            # 4. Eliminate elements in all other rows (above and below pivot)
            for i in range(self.rows):
                if i != pivot_row:
                    factor = self.matrix[i][j]
                    if abs(factor) > 1e-10: # Only eliminate if non-zero
                        self.matrix[i] = [self.matrix[i][k] - factor * self.matrix[pivot_row][k] for k in range(self.cols)]
                        self._record_step(f"Eliminate Row {i + 1}: R{i+1} = R{i+1} - ({factor:.3f})*R{pivot_row+1}")
            
            pivot_row += 1

        # 5. Check for Inconsistency (e.g., 0x + 0y = 5)
        for i in range(self.rows):
            all_zeros = all(abs(val) < 1e-10 for val in self.matrix[i][:-1])
            if all_zeros and abs(self.matrix[i][-1]) > 1e-10:
                return False, self.matrix, self.steps, None
                
        # 6. Extract solutions from RREF matrix
        solution = self._extract_solution()
        return True, self.matrix, self.steps, solution

    def _record_step(self, description):
        """Helper to log the current matrix state."""
        self.steps.append({
            "description": description,
            "matrix": copy.deepcopy(self.matrix)
        })

    def _extract_solution(self):
        """Extracts values of variables from the final matrix."""
        final_solution = []
        for i in range(min(self.rows, self.cols - 1)):
            # Check if row has a pivot at the diagonal
            if abs(self.matrix[i][i] - 1.0) < 1e-10:
                final_solution.append(self.matrix[i][-1])
        return final_solution

def gauss_jordan_solve(matrix):
    """Bridge function to maintain compatibility with app.py."""
    solver = GaussJordanSolver(matrix)
    return solver.solve()
