from typing import List, Tuple
from collections import Counter

class ColorStackSorter:
    def __init__(self, red_stack: List[str], blue_stack: List[str], green_stack: List[str]):
        """
        Initialize the color stack sorter with three stacks of colored balls.
        
        Args:
            red_stack (List[str]): Stack of red balls
            blue_stack (List[str]): Stack of blue balls
            green_stack (List[str]): Stack of green balls
        
        Raises:
            ValueError: If stacks are not of equal length or have invalid contents
        """
        # Validate input stacks
        if not (len(red_stack) == len(blue_stack) == len(green_stack)):
            raise ValueError("All stacks must have equal number of balls")
        
        # Validate ball colors
        valid_colors = {'red', 'blue', 'green'}
        if not (all(ball.lower() in valid_colors for ball in red_stack) and
                all(ball.lower() in valid_colors for ball in blue_stack) and
                all(ball.lower() in valid_colors for ball in green_stack)):
            raise ValueError("Invalid ball colors. Only red, blue, and green are allowed.")
        
        # Normalize ball colors to lowercase
        self.stacks = {
            'red': [ball.lower() for ball in red_stack],
            'blue': [ball.lower() for ball in blue_stack],
            'green': [ball.lower() for ball in green_stack]
        }
        self.moves = []

    def sort(self) -> List[Tuple[str, str]]:
        """
        Sort the stacks by moving one ball at a time, maintaining equal stack sizes.
        
        Returns:
            List[Tuple[str, str]]: List of moves made, each move is (from_stack, to_stack)
        """
        # Reset moves
        self.moves = []
        
        # Color sorting priority
        color_order = ['red', 'blue', 'green']
        max_iterations = len(self.stacks['red']) * 10  # Prevent infinite loop
        
        while not self._is_sorted() and len(self.moves) < max_iterations:
            # Find all mixed stacks
            mixed_stacks = [color for color, stack in self.stacks.items() if len(set(stack)) > 1]
            
            if not mixed_stacks:
                break
            
            # Prioritize sorting by color frequency
            for color in color_order:
                if color in mixed_stacks:
                    # Count colors in the stack
                    color_counts = Counter(self.stacks[color])
                    
                    # Find the least frequent color to move
                    least_color = min(color_counts, key=color_counts.get)
                    
                    # Find destination stacks
                    destination_colors = [c for c in color_order if c != color]
                    
                    # Try to move to each destination
                    for dest_color in destination_colors:
                        if least_color not in self.stacks[dest_color]:
                            # Move the ball
                            ball_index = self.stacks[color].index(least_color)
                            ball = self.stacks[color].pop(ball_index)
                            self.stacks[dest_color].append(ball)
                            self.moves.append((color, dest_color))
                            break
        
        return self.moves

    def _is_sorted(self) -> bool:
        """
        Check if all stacks have only one color and are of equal length.
        
        Returns:
            bool: True if stacks are sorted, False otherwise
        """
        # Check if each stack has only one unique color
        for stack_name, stack in self.stacks.items():
            if len(set(stack)) > 1:
                return False
        
        return True