import re
import json

def expand_contractions(self, text):
        """
        Expand contractions in given text.
        
        Parameters:
        text (str): Text to expand.

        Returns:
        str: Text with expanded contractions.
        """
        with open('./supplementary/contractions.json', 'r') as f:
            contraction_map = json.load(f)

        contractions_pattern = re.compile('({})'.format('|'.join(contraction_map.keys())), flags=re.IGNORECASE|re.DOTALL)

        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contraction_map.get(match) if contraction_map.get(match) else contraction_map.get(match.lower())
            expanded_contraction = first_char+expanded_contraction[1:]
            return expanded_contraction

        expanded_text = contractions_pattern.sub(expand_match, text)
        expanded_text = re.sub("'", "", expanded_text)

        return expanded_text
