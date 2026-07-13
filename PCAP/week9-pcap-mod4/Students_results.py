class StudentsDataException(Exception):
    pass

class BadLineData(StudentsDataException):
    pass

class FileEmpty(StudentsDataException):
    pass

# Dictionary to hold 'Firstname Lastname': combined_score
student_scores = {}
file_name = input("Enter student data file name: ")

try:
    stream = open(file_name, "rt")
    lines = stream.readlines()
    stream.close()
    
    # Check if file is completely empty
    if len(lines) == 0:
        raise FileEmpty("The file is empty.")
        
    for line_num, line in enumerate(lines, 1):
        # Split line by whitespace
        parts = line.split()
        
        # If line doesn't have exactly 3 parts (First, Last, Score), it's malformed
        if len(parts) != 3:
            raise BadLineData(f"Line {line_num} is malformed.")
            
        first_name, last_name, score_str = parts
        
        try:
            score = float(score_str)
        except ValueError:
            raise BadLineData(f"Line {line_num} contains an invalid score.")
            
        full_name = f"{first_name} {last_name}"
        
        # Add score to existing record or create a new entry
        if full_name in student_scores:
            student_scores[full_name] += score
        else:
            student_scores[full_name] = score

    # Print out sorted alphabetically by student name
    for student in sorted(student_scores.keys()):
        print(f"{student}\t{student_scores[student]}")

except IOError as e:
    print("File could not be opened.")
except StudentsDataException as e:
    print("Data Error:", e)