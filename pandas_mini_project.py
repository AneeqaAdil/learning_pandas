import pandas as pd

student = {
    "Name": ["Aneeqa", "Ali", "Sara"],
    "Marks": [95, None, 91]
}

df = pd.DataFrame(student)

print(df.isnull())
