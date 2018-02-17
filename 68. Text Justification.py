import math


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        curWords = []
        curLineWordLen = 0
        for w in words:
            if curLineWordLen == 0:
                curWords.append(w)
                curLineWordLen = len(w)
            elif curLineWordLen + len(w) + 1 <= maxWidth:
                curWords.append(w)
                curLineWordLen = curLineWordLen + len(w) + 1
            else:
                if len(curWords) == 1:
                    line = curWords[0]
                    while len(line) < maxWidth:
                        line += ' '
                    result.append(line)
                else:
                    cnt = maxWidth - curLineWordLen
                    space = cnt // (len(curWords) - 1)
                    extra = cnt % (len(curWords) - 1)
                    line = curWords[0]
                    for i in range(1, len(curWords)):
                        line += ' '
                        for j in range(space):
                            line += ' '
                        if extra:
                            line += ' '
                            extra = extra - 1
                        line += curWords[i]

                    result.append(line)
                curWords = [w]
                curLineWordLen = len(w)

        if len(curWords):
            line = curWords[0]
            for i in range(1, len(curWords)):
                line += ' '
                line += curWords[i]
            while len(line) < maxWidth:
                line += ' '
            result.append(line)
        return result


if __name__ == '__main__':
    s = Solution()
    ret = s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    for v in ret:
        print(v + "|")
