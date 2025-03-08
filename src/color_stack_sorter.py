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
        
        # Color sorting priorities
        color_priorities = {
            'red': 1,
            'blue': 2,
            'green': 3
        }
        
        # Maximum iterations to prevent infinite loop
        max_iterations = len(self.stacks['red']) * 50
        
        while not self._is_sorted() and len(self.moves) < max_iterations:
            # Identify mixed stacks
            mixed_stacks = [
                color for color, stack in self.stacks.items() 
                if len(set(stack)) > 1
            ]
            
            if not mixed_stacks:
                break
            
            # Sort mixed stacks by priority (lowest to highest)
            mixed_stacks.sort(key=lambda x: color_priorities[x])
            
            # Take the lowest priority mixed stack
            from_color = mixed_stacks[0]
            
            # Find unique colors in the source stack
            source_colors = set(self.stacks[from_color])
            
            # Possible destination colors
            dest_colors = [
                color for color in color_priorities.keys() 
                if color != from_color
            ]
            dest_colors.sort(key=lambda x: color_priorities[x])
            
            # Try to move to each destination color
            move_successful = False
            for dest_color in dest_colors:
                # Find colors that can be moved
                movable_colors = [
                    color for color in source_colors 
                    if color not in self.stacks[dest_color]
                ]
                
                for move_color in movable_colors:
                    # Find the index of a ball of this color
                    ball_index = self.stacks[from_color].index(move_color)
                    
                    # Move the ball
                    ball = self.stacks[from_color].pop(ball_index)
                    self.stacks[dest_color].append(ball)
                    self.moves.append((from_color, dest_color))
                    move_successful = True
                    break
                
                # Stop after the first successful move
                if move_successful:
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