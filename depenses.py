import pandas as pd
 
depenses = pd.DataFrame({
    "categorie": ["Courses", "Transport", "Loisirs"],
    "montant": [45.50, 12.00, 25.00]
})
print(depenses)
total = depenses["montant"].sum()
print(f"Total : {total:.2f} EUR") 
