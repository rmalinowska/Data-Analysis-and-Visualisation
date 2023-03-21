#!/usr/bin/env python3

import pandas as pd
import datetime

def create_table():
    categories = []
    captions = []
    start_time = []
    end_time = []

    categories.append('term')
    captions.append('winter term')
    start_time.append(datetime.datetime(2023,10,1))
    end_time.append(datetime.datetime(2024,2,18))

    categories.append('term')
    captions.append('summer term')
    start_time.append(datetime.datetime(2024,2,19))
    end_time.append(datetime.datetime(2024,9,30))

    categories.append("classes")
    captions.append("block I")
    start_time.append(datetime.datetime(2023,10,2))
    end_time.append(datetime.datetime(2023,10,29))
    
    categories.append("deadline")
    captions.append("linkage deletion request")
    start_time.append(datetime.datetime(2023,10,20))
    end_time.append(datetime.datetime(2023,10,20))

    categories.append("classes")
    captions.append("block II")
    start_time.append(datetime.datetime(2023,10,30))
    end_time.append(datetime.datetime(2023,12,3))

    categories.append('linkage')
    captions.append('linkage time')
    start_time.append(datetime.datetime(2023,10,1))
    end_time.append(datetime.datetime(2024,2,18))
    
    categories.append("classes")
    captions.append("block III")
    start_time.append(datetime.datetime(2023,12,4))
    end_time.append(datetime.datetime(2023,12,21))

    categories.append("holiday")
    captions.append("winter break")
    start_time.append(datetime.datetime(2023, 12,22))
    end_time.append(datetime.datetime(2024, 1,7))

    categories.append("classes")
    captions.append("block III")
    start_time.append(datetime.datetime(2024, 1,8))
    end_time.append(datetime.datetime(2024, 1,28))

    categories.append("deadline")
    captions.append("resignation from completing the course")
    start_time.append(datetime.datetime(2024, 1,19))
    end_time.append(datetime.datetime(2024, 1,19))

    categories.append("exams")
    captions.append("winter exams")
    start_time.append(datetime.datetime(2024, 1,29))
    end_time.append(datetime.datetime(2024, 2,11))

    categories.append("language exams")
    captions.append("language certification exams")
    start_time.append(datetime.datetime(2024, 1,29))
    end_time.append(datetime.datetime(2024, 1,30))

    categories.append("holiday")
    captions.append("intersemester break")
    start_time.append(datetime.datetime(2024, 2,12))
    end_time.append(datetime.datetime(2024, 2,18))

    categories.append("term")
    captions.append("summer term")
    start_time.append(datetime.datetime(2024, 2,19))
    end_time.append(datetime.datetime(2024, 9,30))

    categories.append("classes")
    captions.append("block I")
    start_time.append(datetime.datetime(2024,2,19))
    end_time.append(datetime.datetime(2024,3,17))

    categories.append("exams")
    captions.append("re-take exam winter session")
    start_time.append(datetime.datetime(2024, 2,23))
    end_time.append(datetime.datetime(2024, 3,3))

    categories.append("language exams")
    captions.append("B2 english exams")
    start_time.append(datetime.datetime(2024, 2,24))
    end_time.append(datetime.datetime(2024, 2,24))

    categories.append("decisions")
    captions.append("completing winter semester decisions")
    start_time.append(datetime.datetime(2024, 3,4))
    end_time.append(datetime.datetime(2024, 3,31))

    categories.append("deadline")
    captions.append("linkage deletion request")
    start_time.append(datetime.datetime(2024,3,15))
    end_time.append(datetime.datetime(2024,3,15))    

    categories.append("classes")
    captions.append("block II")
    start_time.append(datetime.datetime(2024, 3, 18))
    end_time.append(datetime.datetime(2024, 4,28))

    categories.append("holiday")
    captions.append("spring break")
    start_time.append(datetime.datetime(2024, 3, 28))
    end_time.append(datetime.datetime(2024,4,2))

    categories.append("classes")
    captions.append("block III")
    start_time.append(datetime.datetime(2024,4,29))
    end_time.append(datetime.datetime(2024, 6, 16))

    categories.append("holiday")
    captions.append("holiday")
    start_time.append(datetime.datetime(2024, 5,2))
    end_time.append(datetime.datetime(2024, 5,2))

    categories.append("holiday")
    captions.append("holiday")
    start_time.append(datetime.datetime(2024, 5,31))
    end_time.append(datetime.datetime(2024,6,2))

    categories.append("holiday")
    captions.append("student carnival")
    start_time.append(datetime.datetime(2024,5,10))
    end_time.append(datetime.datetime(2024,5,11))

    categories.append("deadline")
    captions.append("resignation from completing the course")
    start_time.append(datetime.datetime(2024,6,1))
    end_time.append(datetime.datetime(2024,6,1))

    categories.append("linkage")
    captions.append("linkage period")
    start_time.append(datetime.datetime(2024, 6,1))
    end_time.append(datetime.datetime(2024, 9,30))

    categories.append("exams")
    captions.append("summer exams")
    start_time.append(datetime.datetime(2024,6,17))
    end_time.append(datetime.datetime(2024,7,7))

    categories.append("language exams")
    captions.append("language certification exams")
    start_time.append(datetime.datetime(2024,6,17))
    end_time.append(datetime.datetime(2024,6,18))

    categories.append("holiday")
    captions.append("summer break")
    start_time.append(datetime.datetime(2024,7,8))
    end_time.append(datetime.datetime(2024,9,30))

    categories.append("exams")
    captions.append("re-take exam summer session")
    start_time.append(datetime.datetime(2024, 9,2))
    end_time.append(datetime.datetime(2024, 9,15))

    categories.append("decisions")
    captions.append("completing whole year decisions")
    start_time.append(datetime.datetime(2024, 9,16))
    end_time.append(datetime.datetime(2024,9,30))

    df = pd.DataFrame(list(zip(categories, captions, start_time, end_time)), columns=["Category", "Caption", "Start", "End"])

    return df

print(create_table())