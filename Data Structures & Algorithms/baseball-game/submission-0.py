class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out = []
        ops = ["+","C","D"]
        for elem in operations:
            if elem not in ops:
                out.append(int(elem))
            else:
                if elem=="D":
                    out.append(2*out[-1])
                elif elem=="C":
                    out.pop()
                elif elem=="+":
                    out.append(out[-2]+out[-1])
        return sum(out)