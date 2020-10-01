# Including Components for HangMan Game.
names=['Aaina', 'Aaliyah', 'Aasha', 'Aasiya', 'Abhijeet', 'Aditi', 'Aditya', 'Aishwarya', 'Akshat', 'Amanpreet', 'Amena', 'Amitava', 'Aniruddh', 'Anjali', 'Antara', 'Anubhav', 'Aparna', 'Arjun', 'Armaan', 'Arshpreet', 'Aruna', 'Arunima', 'Arzoo', 'Ashish', 'Ayesha', 'Azad', 'Bahaar', 'Bhagyashree', 'Bhaskar', 'Bhavesh', 'Bhavin', 'Bhavna', 'Bhoomi', 'Bipasha', 'Bipin', 'Chaaya', 'Chandrika', 'Chetas', 'Chhavi', 'Chirag', 'Chiranjeev', 'Chitragandha', 'Daanish', 'Dalbir', 'Daljeet', 'Debashish', 'Debyendu', 'Deepika', 'Devika', 'Dhruv', 'Dipankar', 'Diya', 'Ehsaan', 'Ekta', 'Emir', 'Falguni', 'Farah', 'Fardeen', 'Farhan', 'Fatima', 'Gagandeep', 'Garima', 'Gauhar', 'Gaurav', 'Gautam', 'Gayatri', 'Geetha', 'Girish', 'Gurdeep', 'Gurleen', 'Harbhajan', 'Harini', 'Harpreet', 'Himmat', 'Imraan', 'Indrani', 'Indranuj', 'Ira', 'Jasleen', 'Jayant', 'Jayanti', 'Jayesh', 'Jeet', 'Junaid', 'Jyothsna', 'Jyotiraditya', 'Kabir', 'Kalyani', 'Kanika', 'Kartik', 'Karun', 'Kavya', 'Khalid', 'Kshitij', 'Kuwarjeet', 'Laila', 'Lathika', 'Lavanya', 'Leela', 'Lohith', 'Lopamudra', 'Lovesh', 'Madhav', 'Mahrukh', 'Malavika', 'Manju', 'Maya', 'Meera', 'Meher', 'Mohammed', 'Mridul', 'Naaz', 'Nagma', 'Nalini', 'Nargis', 'Navjot', 'Nikhil', 'Nimit', 'Nishith', 'Nivedita', 'Noor', 'Ojas', 'Om', 'Onkar', 'Paramjit', 'Parinaaz', 'Paritosh', 'Parizaad', 'Parth', 'Parvez', 'Pavan', 'Piya', 'Pooja', 'Prabhjot', 'Pranav', 'Preet', 'Purab', 'Ramandeep', 'Rangana', 'Rasika', 'Rehaan', 'Revati', 'Rihana', 'Rohan', 'Ruchika', 'Sabina', 'Sahil', 'Saira', 'Salman', 'Samarth', 'Samir', 'Sanchit', 'Sanjana', 'Sanjay', 'Santosh', 'Sarabjit', 'Sarah', 'Shaheen', 'Shahnaz', 'Shahzad', 'Shantanu', 'Shereen', 'Shifa', 'Shishir', 'Shivani', 'Shray', 'Shreya', 'Shridevi', 'Shweta', 'Siddharth', 'Simran', 'Sonal', 'Sparsh', 'Sumer', 'Surabhi', 'Surjan', 'Swapan', 'Taahira', 'Tanvi', 'Tara', 'Tarun', 'Tavleen', 'Tejas', 'Tushar', 'Udit', 'Uma', 'Umang', 'Umar', 'Upasana', 'Urvashi', 'Vaishnavi', 'Varun', 'Veer', 'Vidu', 'Vina', 'Yamini', 'Yash', 'Yoshita', 'Zahra', 'Zainab', 'Zeesha', 'ZoyaAngad', 'Zubi']

won='''
                          _______                                                                _______
            \\     /      |       |      |       |                    \\                  /       |       |      |\\     |
             \\   /       |       |      |       |                     \\                /        |       |      | \\    |
              \\ /        |       |      |       |                      \\      /\\      /         |       |      |  \\   |
               |         |       |      |       |                       \\    /  \\    /          |       |      |   \\  |
               |         |       |      |       |                        \\  /    \\  /           |       |      |    \\ |
               |         |_______|      |_______|                         \\/      \\/            |_______|      |     \\|
    '''

lose='''
                          _______                                                 _______        _______        _______
            \\     /      |       |      |       |                    |           |       |      |       |      |
             \\   /       |       |      |       |                    |           |       |      |              |
              \\ /        |       |      |       |                    |           |       |      |_______       |_______
               |         |       |      |       |                    |           |       |              |      |
               |         |       |      |       |                    |           |       |              |      |
               |         |_______|      |_______|                    |_______    |_______|      |_______|      |_______
    '''

draw=[
"""
             _______________
            |               |
            |               |
            |               |
            |
            |
            |
            |
            |
            |
            |
            |
    ________|________
"""
,
"""
             _______________
            |               |
            |               |
            |            ___|___
            |           |       |
            |           |___ ___|
            |               |
            |            \\  |  /
            |             \\ | /
            |              \\|/
            |              / \\
            |             /   \\
    ________|________    /     \\

"""
,
"""
             _______________
            |               |
            |               |
            |            ___|___
            |           |       |
            |           |___ ___|
            |               |
            |            \\  |  /
            |             \\ | /
            |              \\|/
            |                \\
            |                 \\
    ________|________          \\
"""
,
"""
             _______________
            |               |
            |               |
            |            ___|___
            |           |       |
            |           |___ ___|
            |               |
            |            \\  |  /
            |             \\ | /
            |              \\|/
            |
            |
    ________|________
"""
,
"""
             _______________
            |               |
            |               |
            |            ___|___
            |           |       |
            |           |___ ___|
            |               |
            |               |  /
            |               | /
            |               |/
            |
            |
    ________|________
"""
,
"""
             _______________
            |               |
            |               |
            |            ___|___
            |           |       |
            |           |___ ___|
            |               |
            |               |
            |               |
            |               |
            |
            |
    ________|________
"""
,
"""
             _______________
            |               |
            |               |
            |            ___|___
            |           |       |
            |           |___ ___|
            |
            |
            |
            |
            |
            |
    ________|________
"""
]