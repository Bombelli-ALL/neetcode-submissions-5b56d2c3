class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tmp: list = []
        for e in tokens:
            if e.isdigit() or e.lstrip('-').isdigit():
                tmp.append(int(e))
            else:
                if e ==  '+':
                    tm = tmp[-2] + tmp[-1]
                elif e == '-':
                    tm = tmp[-2] - tmp[-1]
                elif e == '*':
                    tm = tmp[-2] * tmp[-1]
                elif e == '/':
                    if tmp[-1] != 0:
                        tm = int(tmp[-2] / tmp[-1])

                    else:
                        tm = 0
                tmp.pop()
                tmp.pop()
                tmp.append(tm)
        return tmp[-1]