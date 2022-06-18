def gradingStudents(grades):
    out = [0] * len(grades)
    for i, grade in enumerate(grades):
        if grade % 5 >= 3 and grade > 37:
            out[i] = grade + (5 - (grade % 5))
        else:
            out[i] = grade
    return out