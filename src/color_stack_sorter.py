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
        
        # Normalize ball colors to lowercase and store
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
        
        # Color sorting priority (least to most)
        color_priority = ['red', 'blue', 'green']
        
        # Maximum iterations to prevent infinite loop
        max_iterations = len(self.stacks['red']) * 20
        
        # Continue sorting until stacks are uniform or max iterations reached
        while not self._is_sorted() and len(self.moves) < max_iterations:
            # Find stacks with multiple colors
            mixed_stacks = [color for color, stack in self.stacks.items() 
                           if len(set(stack)) > 1]
            
            if not mixed_stacks:
                break
            
            # Systematic sorting strategy
            for from_color in color_priority:
                if from_color in mixed_stacks:
                    # Analyze color distribution in source stack
                    source_colors = Counter(self.stacks[from_color])
                    
                    # Find destination colors
                    dest_colors = [c for c in color_priority if c != from_color]
                    
                    # Try to move the most frequent color out
                    most_freq_color = max(source_colors, key=source_colors.get)
                    
                    for dest_color in dest_colors:
                        # Move to destination that doesn't have this color
                        if most_freq_color not in self.stacks[dest_color]:
                            # Find and remove the ball to move
                            ball_index = self.stacks[from_color].index(most_freq_color)
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
        # Check if each stack has at most one unique color
        return all(len(set(stack)) <= 1 for stack in self.stacks.values())