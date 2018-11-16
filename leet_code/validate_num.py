"""
Validate if a given string can be interpreted as a decimal number.
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:
Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
"""
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = 0

        digit_map = {
           5 : 1,
           0 : 1, 
           1 : 1,
      
        }

        sign_state = {
           0: 5,
           }

        
        dot = {
            0 : 6,
            5 : 6,
          }

        expo = {
            1 : 4,
            
        }
        map = {
            'd': digit_map,
            '-': sign_state,
            '+': sign_state,
            '.': dot,
            'e': expo,
        }
        default = {}
        for ch in s.strip():
            if '0' <= ch <= '9':
                ch = 'd'
            state = map.get(ch, default).get(state)

            if state is None:
                return False

        return state in [1, 3, 2]