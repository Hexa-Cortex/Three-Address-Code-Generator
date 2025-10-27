"""
Three Address Code Generator
Converts arithmetic expressions to TAC intermediate representation
"""

class TACGenerator:
    def __init__(self):
        self.temp_count = 0
        self.instructions = []
    
    def new_temp(self):
        """Generate a new temporary variable"""
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    def reset(self):
        """Reset the generator state"""
        self.temp_count = 0
        self.instructions = []
    
    def generate(self, expression):
        """Generate TAC from an arithmetic expression"""
        self.reset()
        tokens = self._tokenize(expression)
        result = self._parse_expression(tokens)
        return '\n'.join(self.instructions)
    
    def _tokenize(self, expr):
        """Simple tokenizer for arithmetic expressions"""
        tokens = []
        current = ""
        operators = {'+', '-', '*', '/', '%', '=', '(', ')'}
        
        for char in expr:
            if char.isspace():
                if current:
                    tokens.append(current)
                    current = ""
            elif char in operators:
                if current:
                    tokens.append(current)
                    current = ""
                tokens.append(char)
            else:
                current += char
        
        if current:
            tokens.append(current)
        
        return tokens
    
    def _parse_expression(self, tokens):
        """Parse and generate TAC for expression"""
        if '=' in tokens:
            eq_idx = tokens.index('=')
            var = tokens[eq_idx - 1]
            expr_tokens = tokens[eq_idx + 1:]
            result = self._parse_additive(expr_tokens, 0)
            self.instructions.append(f"{var} = {result[0]}")
            return result
        else:
            return self._parse_additive(tokens, 0)
    
    def _parse_additive(self, tokens, pos):
        """Parse addition and subtraction"""
        left, pos = self._parse_multiplicative(tokens, pos)
        
        while pos < len(tokens) and tokens[pos] in ['+', '-']:
            op = tokens[pos]
            pos += 1
            right, pos = self._parse_multiplicative(tokens, pos)
            temp = self.new_temp()
            self.instructions.append(f"{temp} = {left} {op} {right}")
            left = temp
        
        return left, pos
    
    def _parse_multiplicative(self, tokens, pos):
        """Parse multiplication, division, and modulo"""
        left, pos = self._parse_primary(tokens, pos)
        
        while pos < len(tokens) and tokens[pos] in ['*', '/', '%']:
            op = tokens[pos]
            pos += 1
            right, pos = self._parse_primary(tokens, pos)
            temp = self.new_temp()
            self.instructions.append(f"{temp} = {left} {op} {right}")
            left = temp
        
        return left, pos
    
    def _parse_primary(self, tokens, pos):
        """Parse primary expressions (variables, numbers, parentheses)"""
        if tokens[pos] == '(':
            pos += 1
            result, pos = self._parse_additive(tokens, pos)
            pos += 1  # skip ')'
            return result, pos
        else:
            return tokens[pos], pos + 1


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python tac_generator.py '<expression>'")
        print("Example: python tac_generator.py 'x = a + b * c'")
        return
    
    expression = sys.argv[1]
    generator = TACGenerator()
    tac = generator.generate(expression)
    
    print("Three Address Code:")
    print(tac)


if __name__ == "__main__":
    main()
