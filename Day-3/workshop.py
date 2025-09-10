day1 = ["Jeshu@example.com", "suji@example.com", "venkAt@example.com", "Raju@example.com"]
day2 = ["Raju@example.com", "David@example.com", "venkAt@example.com", "Eve@example.com"]
day3 = ["Jeshu@example.com", "mahi@example.com", "frank@example.com"]

def clean_list(emails):
    return set(email.lower() for email in emails)

day1_clean = clean_list(day1)
day2_clean = clean_list(day2)
day3_clean = clean_list(day3)


all_unique = day1_clean | day2_clean | day3_clean

all_three = day1_clean & day2_clean & day3_clean

exactly_one = (day1_clean - day2_clean - day3_clean) | \
              (day2_clean - day1_clean - day3_clean) | \
              (day3_clean - day1_clean - day2_clean)

day1_day2 = day1_clean & day2_clean
day2_day3 = day2_clean & day3_clean
day1_day3 = day1_clean & day3_clean

print(" TECH WORKSHOP ATTENDEE REPORT \n")

print(f"Total unique attendees: {len(all_unique)}")
print("List of all unique attendees:", sorted(all_unique), "\n")

print(f"Attendees who attended all three days: {len(all_three)}")
print("List:", sorted(all_three), "\n")

print(f"Attendees who attended exactly one day: {len(exactly_one)}")
print("List:", sorted(exactly_one), "\n")

print(f"Pairwise overlaps:")
print(f"Day1 & Day2: {len(day1_day2)}, Attendees: {sorted(day1_day2)}")
print(f"Day2 & Day3: {len(day2_day3)}, Attendees: {sorted(day2_day3)}")
print(f"Day1 & Day3: {len(day1_day3)}, Attendees: {sorted(day1_day3)}")
