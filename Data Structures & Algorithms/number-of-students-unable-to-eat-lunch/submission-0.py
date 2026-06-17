class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if students == sandwiches:
            return 0
        continue1 = True
        while continue1:
            if sandwiches[0] == students[0]:
                del sandwiches[0]
                del students[0]
            else:
                again = students[0]
                del students[0]
                students.append(again)
            
            if len(sandwiches)==0 or (sandwiches[0] not in students):
                continue1 = False
        return len(students)
                