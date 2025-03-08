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
        
        # Continue sorting until stacks are uniform or no more moves possible
        max_iterations = len(self.stacks['red']) * 3  # Prevent infinite loop
        iterations = 0
        
        while not self._is_sorted() and iterations < max_iterations:
            # Find the stack with the most color variation
            max_color = self._get_max_color()
            
            # Find the stack with the least color variation 
            min_color = self._get_min_color()
            
            if max_color == min_color:
                break  # Cannot make further progress
            
            # Move a ball from the max color stack to the min color stack
            ball = self.stacks[max_color].pop()
            self.stacks[min_color].append(ball)
            self.moves.append((max_color, min_color))
            
            iterations += 1
        
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

    def _get_max_color(self) -> str:
        """
        Find the color of the stack that should give up a ball.
        
        Returns:
            str: Color of the stack to move from
        """
        # Order of precedence: green > blue > red
        color_order = ['green', 'blue', 'red']
        for color in color_order:
            # Choose color with most color variation
            if len(set(self.stacks[color])) > 1:
                return color
        
        return color_order[0]  # Default to green if no mixed stacks

    def _get_min_color(self) -> str:
        """
        Find the color of the stack that should receive a ball.
        
        Returns:
            str: Color of the stack to move to
        """
        # Order of precedence: red < blue < green
        color_order = ['red', 'blue', 'green']
        for color in color_order:
            # Prefer stacks with fewer unique colors
            if len(set(self.stacks[color])) < len(set(self.stacks[color_order[0]])):
                return color
        
        return color_order[2]  # Default to green