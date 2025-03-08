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
        
        # Continue sorting until stacks are uniform
        max_iterations = len(self.stacks['red']) * 6  # Prevent infinite loop
        color_mapping = {
            'red': ['blue', 'green'],
            'blue': ['red', 'green'],
            'green': ['red', 'blue']
        }
        
        while not self._is_sorted():
            # Check if we've exceeded max iterations
            if len(self.moves) >= max_iterations:
                break
            
            # Find any stack with multiple colors
            mixed_stacks = [color for color, stack in self.stacks.items() if len(set(stack)) > 1]
            
            if not mixed_stacks:
                break
            
            # Pick the first mixed stack
            from_color = mixed_stacks[0]
            
            # Determine potential destination colors
            potential_destinations = color_mapping[from_color]
            
            # Move to destination that will help sorting
            for dest_color in potential_destinations:
                # Choose a ball from source that is different from destination stack
                if from_color != dest_color:
                    # Find a ball that doesn't belong
                    for ball in self.stacks[from_color]:
                        if ball not in set(self.stacks[dest_color]):
                            # Remove from source, add to destination
                            self.stacks[from_color].remove(ball)
                            self.stacks[dest_color].append(ball)
                            self.moves.append((from_color, dest_color))
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