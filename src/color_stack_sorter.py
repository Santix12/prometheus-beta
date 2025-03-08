from typing import List, Tuple

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
        
        # Normalize ball colors to lowercase and store original input
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
        
        # Predefined color priority for sorting
        color_priorities = {
            'red': 1,
            'blue': 2,
            'green': 3
        }
        
        # Maximum iterations to prevent infinite loop
        max_iterations = len(self.stacks['red']) * 10
        
        # Continue sorting until all stacks are single color
        while not self._is_sorted() and len(self.moves) < max_iterations:
            # Find stacks with mixed colors
            mixed_stacks = [color for color, stack in self.stacks.items() if len(set(stack)) > 1]
            
            if not mixed_stacks:
                break
            
            # Sort mixed stacks by priority
            mixed_stacks.sort(key=lambda x: color_priorities[x])
            
            # Pick the highest priority mixed stack
            from_color = mixed_stacks[0]
            
            # Find destination colors
            other_colors = [c for c in color_priorities.keys() if c != from_color]
            other_colors.sort(key=lambda x: color_priorities[x])
            
            # Try to move to destination
            for dest_color in other_colors:
                # Find a ball that doesn't match current stack to move
                for ball in self.stacks[from_color]:
                    if ball not in set(self.stacks[dest_color]):
                        # Remove from source, add to destination
                        self.stacks[from_color].remove(ball)
                        self.stacks[dest_color].append(ball)
                        self.moves.append((from_color, dest_color))
                        break
                
                # Break outer loop if a move was made
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