sp = {"Студент1": ["Русский", "Английский"], "Студент2": ["Русский", "Английский", "Немецкий"], "Студент3": ["Китайский", "Английский", "Немецкий"], "Студент4": ["Китайский", "Французский", "Немецкий"], "Студент5": ["Русский", "Французский", "Японский"]}
lang = []
st = []
for i in sp:
    for a in sp[i]:
        lang.append(a)

print("Студенты знают: ", len(set(lang)), " различных языков")
lang_sort = list(set(lang))
lang_sort.sort()
print(lang_sort)

for i in sp:
    for a in sp[i]:
        if a == "Китайский":
            st.append(i)
print(st)