def calculate_love_score(name_one, name_two):
        true_score = 0
        love_score = 0
        fullname = name_one.lower() + name_two.lower()

        for letter in 'true':
            true_score += fullname.count(letter)
            
        for letter in 'love':
            love_score += fullname.count(letter)
            
        print(f"{true_score}{love_score}")
