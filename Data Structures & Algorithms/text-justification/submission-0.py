class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0 # line arr, len of line in chars
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) <= maxWidth:
                # can fit word in line
                line.append(words[i])
                length += len(words[i])
                i += 1
            else:
                # cant fit word in line , i.e. line complete
                extra_space = maxWidth - length
                space = extra_space // (max(1, len(line)-1))
                remainder = extra_space % max(1, len(line)-1)

                # add spaces to the words
                for j in range(max(1, len(line)-1)):
                    line[j] += ' ' * space
                    if remainder:
                        line[j] += ' ' 
                        remainder -= 1
                res.append(''.join(line))
                line, length = [], 0

        # handle last line
        last_line = ' '.join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + ' '*trail_space)
        return res