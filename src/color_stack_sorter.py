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
        
        # Color reference order
        color_order = ['red', 'blue', 'green']
        
        # Maximum iterations to prevent infinite loop
        max_iterations = len(self.stacks['red']) * 30
        
        while not self._is_sorted() and len(self.moves) < max_iterations:
            # Perform multiple passes through color groups
            for source_index, from_color in enumerate(color_order):
                # Find destination colors
                dest_colors = [c for c in color_order if c != from_color]
                
                # Analyze source stack
                source_counter = Counter(self.stacks[from_color])
                
                # If stack is mixed, try to resolve
                if len(source_counter) > 1:
                    # Priority colors for moving
                    move_colors = sorted(source_counter.keys(), 
                                         key=lambda x: color_order.index(x))
                    
                    # Try to move each color
                    for move_color in move_colors:
                        for dest_color in dest_colors:
                            # Can we move to this destination?
                            if move_color not in self.stacks[dest_color]:
                                # Find and move the ball
                                ball_index = self.stacks[from_color].index(move_color)
                                ball = self.stacks[from_color].pop(ball_index)
                                self.stacks[dest_color].append(ball)
                                self.moves.append((from_color, dest_color))
                                break
        
        return self.moves

    def _is_sorted(self) -> bool:
        """
        Check if all stacks have only one color.
        
        Returns:
            bool: True if stacks are sorted, False otherwise
        """
        # Verify each stack has at most one unique color
        return all(len(set(stack)) <= 1 for stack in self.stacks.values())