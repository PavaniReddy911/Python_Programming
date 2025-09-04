

amount=int(input("Enter the amount\n"))
notes=[500,200,100,50,20,10]
nc={}
for note in notes:
    if amount>=note:
        count=amount//note
        amount=amount%note
        nc[note]=count
print("Breakdown of notes:")
tn=0
for note,count in nc.items():
    print(f"{note} : {count}")
    tn+=count

print("Total number of notes:", tn)

amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
note_count = {}

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        note_count[note] = count

print("Breakdown of notes:")
total_notes = 0
for note, count in note_count.items():
    print(f"{note} : {count}")
    total_notes += count

print("Total number of notes:", total_notes)
