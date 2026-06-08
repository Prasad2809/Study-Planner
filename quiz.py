import streamlit as st
import random

def quiz_page():
    st.set_page_config(page_title="📝 Quiz Zone", layout="centered")
    st.title("📝 Quiz Zone")
    st.write("Test your knowledge! Refresh the page to get a new set of random questions.")

    # Expanded Question Bank — At least 20 per subject
    question_bank = [
        # General Knowledge
        {"q": "What is the capital of France?", "options": ["Paris", "Rome", "Madrid"], "answer": "Paris"},
        {"q": "Which continent is Egypt in?", "options": ["Asia", "Africa", "Europe"], "answer": "Africa"},
        {"q": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"], "answer": "Leonardo da Vinci"},
        {"q": "What is the largest ocean on Earth?", "options": ["Atlantic", "Pacific", "Indian"], "answer": "Pacific"},
        {"q": "Which language has the most native speakers?", "options": ["Mandarin", "English", "Hindi"], "answer": "Mandarin"},
        {"q": "What is the smallest country in the world?", "options": ["Monaco", "Vatican City", "Malta"], "answer": "Vatican City"},
        {"q": "How many continents are there?", "options": ["5", "6", "7"], "answer": "7"},
        {"q": "What is the national animal of Australia?", "options": ["Kangaroo", "Koala", "Emu"], "answer": "Kangaroo"},
        {"q": "Which country invented tea?", "options": ["China", "India", "Japan"], "answer": "China"},
        {"q": "What is the tallest mountain in the world?", "options": ["Everest", "K2", "Kangchenjunga"], "answer": "Everest"},
        {"q": "In which country is the Taj Mahal?", "options": ["India", "Pakistan", "Nepal"], "answer": "India"},
        {"q": "What is the currency of Japan?", "options": ["Yen", "Won", "Dollar"], "answer": "Yen"},
        {"q": "Which animal is known as the 'Ship of the Desert'?", "options": ["Camel", "Horse", "Donkey"], "answer": "Camel"},
        {"q": "What is the boiling point of water in Celsius?", "options": ["100", "90", "80"], "answer": "100"},
        {"q": "What is the capital of Canada?", "options": ["Toronto", "Ottawa", "Vancouver"], "answer": "Ottawa"},
        {"q": "Which metal is liquid at room temperature?", "options": ["Mercury", "Gold", "Silver"], "answer": "Mercury"},
        {"q": "What is the largest desert in the world?", "options": ["Sahara", "Antarctica", "Gobi"], "answer": "Antarctica"},
        {"q": "What is the fastest land animal?", "options": ["Cheetah", "Lion", "Horse"], "answer": "Cheetah"},
        {"q": "What is the capital of Italy?", "options": ["Rome", "Venice", "Florence"], "answer": "Rome"},
        {"q": "Which bird is the universal symbol of peace?", "options": ["Dove", "Swan", "Eagle"], "answer": "Dove"},

        # Science
        {"q": "Water's chemical formula is:", "options": ["H2O", "CO2", "O2"], "answer": "H2O"},
        {"q": "What planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter"], "answer": "Mars"},
        {"q": "What gas do plants release during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen"], "answer": "Oxygen"},
        {"q": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Chloroplast"], "answer": "Mitochondria"},
        {"q": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "500,000 km/s"], "answer": "300,000 km/s"},
        {"q": "Which vitamin is produced when our skin is exposed to sunlight?", "options": ["Vitamin D", "Vitamin C", "Vitamin A"], "answer": "Vitamin D"},
        {"q": "How many bones are in the adult human body?", "options": ["206", "210", "201"], "answer": "206"},
        {"q": "Which planet has the most moons?", "options": ["Saturn", "Jupiter", "Uranus"], "answer": "Saturn"},
        {"q": "What is the main gas found in Earth's atmosphere?", "options": ["Nitrogen", "Oxygen", "Carbon Dioxide"], "answer": "Nitrogen"},
        {"q": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Gd"], "answer": "Au"},
        {"q": "Which organ purifies blood in humans?", "options": ["Kidney", "Liver", "Heart"], "answer": "Kidney"},
        {"q": "What is the largest organ in the human body?", "options": ["Skin", "Liver", "Brain"], "answer": "Skin"},
        {"q": "What part of the plant conducts photosynthesis?", "options": ["Leaf", "Root", "Stem"], "answer": "Leaf"},
        {"q": "What is the freezing point of water in Celsius?", "options": ["0", "-1", "5"], "answer": "0"},
        {"q": "What is the hardest natural substance on Earth?", "options": ["Diamond", "Gold", "Iron"], "answer": "Diamond"},
        {"q": "What gas do humans exhale?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen"], "answer": "Carbon Dioxide"},
        {"q": "What force keeps us on the ground?", "options": ["Gravity", "Magnetism", "Friction"], "answer": "Gravity"},
        {"q": "What is the study of fossils called?", "options": ["Paleontology", "Geology", "Archaeology"], "answer": "Paleontology"},
        {"q": "What is the nearest star to Earth?", "options": ["Sun", "Alpha Centauri", "Sirius"], "answer": "Sun"},
        {"q": "Which blood type is known as the universal donor?", "options": ["O-", "O+", "AB+"], "answer": "O-"},

        # Math
        {"q": "Square root of 64 is:", "options": ["6", "8", "10"], "answer": "8"},
        {"q": "What is 12 x 9?", "options": ["108", "102", "112"], "answer": "108"},
        {"q": "Value of π up to 2 decimal places?", "options": ["3.14", "3.15", "3.16"], "answer": "3.14"},
        {"q": "What is 15% of 200?", "options": ["30", "25", "20"], "answer": "30"},
        {"q": "What is 7 squared?", "options": ["49", "56", "14"], "answer": "49"},
        {"q": "What is 100 divided by 4?", "options": ["25", "20", "15"], "answer": "25"},
        {"q": "What is 0 factorial?", "options": ["1", "0", "Undefined"], "answer": "1"},
        {"q": "What is 9 x 9?", "options": ["81", "72", "99"], "answer": "81"},
        {"q": "What is the cube root of 27?", "options": ["3", "9", "6"], "answer": "3"},
        {"q": "Simplify: 50% of 80", "options": ["40", "50", "60"], "answer": "40"},
        {"q": "What is 144 divided by 12?", "options": ["12", "14", "10"], "answer": "12"},
        {"q": "What is the sum of angles in a triangle?", "options": ["180°", "360°", "90°"], "answer": "180°"},
        {"q": "What is 11 x 11?", "options": ["121", "111", "131"], "answer": "121"},
        {"q": "What is 2 to the power of 5?", "options": ["32", "25", "64"], "answer": "32"},
        {"q": "What is 5 cubed?", "options": ["125", "25", "15"], "answer": "125"},
        {"q": "What is 75% of 200?", "options": ["150", "100", "125"], "answer": "150"},
        {"q": "What is 3.5 + 4.5?", "options": ["8", "9", "7"], "answer": "8"},
        {"q": "What is 2/3 as a percentage?", "options": ["66.67%", "60%", "70%"], "answer": "66.67%"},
        {"q": "What is 0.25 as a fraction?", "options": ["1/4", "1/3", "1/5"], "answer": "1/4"},
        {"q": "What is 1/2 of 500?", "options": ["250", "200", "300"], "answer": "250"},

        # History
        {"q": "Who was the first President of the USA?", "options": ["George Washington", "Abraham Lincoln", "Thomas Jefferson"], "answer": "George Washington"},
        {"q": "In which year did World War II end?", "options": ["1945", "1939", "1950"], "answer": "1945"},
        {"q": "Which ancient civilization built the pyramids?", "options": ["Egyptians", "Romans", "Greeks"], "answer": "Egyptians"},
        {"q": "Who was the first man to step on the Moon?", "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin"], "answer": "Neil Armstrong"},
        {"q": "In which year did India gain independence?", "options": ["1947", "1950", "1945"], "answer": "1947"},
        {"q": "Which war was fought between the North and South regions in the USA?", "options": ["Civil War", "World War I", "American Revolution"], "answer": "Civil War"},
        {"q": "Who was known as the 'Iron Lady'?", "options": ["Margaret Thatcher", "Indira Gandhi", "Angela Merkel"], "answer": "Margaret Thatcher"},
        {"q": "Which empire was ruled by Genghis Khan?", "options": ["Mongol Empire", "Roman Empire", "Ottoman Empire"], "answer": "Mongol Empire"},
        {"q": "Who was the first Emperor of China?", "options": ["Qin Shi Huang", "Sun Yat-sen", "Mao Zedong"], "answer": "Qin Shi Huang"},
        {"q": "What was the name of the ship that sank in 1912?", "options": ["Titanic", "Britannic", "Lusitania"], "answer": "Titanic"},
        {"q": "Who was the Prime Minister of the UK during WWII?", "options": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee"], "answer": "Winston Churchill"},
        {"q": "Which city was the first capital of the USA?", "options": ["Philadelphia", "New York", "Washington D.C."], "answer": "Philadelphia"},
        {"q": "Who discovered America?", "options": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan"], "answer": "Christopher Columbus"},
        {"q": "Which country gifted the Statue of Liberty to the USA?", "options": ["France", "UK", "Germany"], "answer": "France"},
        {"q": "Who was the leader of Nazi Germany?", "options": ["Adolf Hitler", "Joseph Stalin", "Benito Mussolini"], "answer": "Adolf Hitler"},
        {"q": "Which treaty ended World War I?", "options": ["Treaty of Versailles", "Treaty of Paris", "Treaty of Ghent"], "answer": "Treaty of Versailles"},
        {"q": "Who founded the Mughal Empire in India?", "options": ["Babur", "Akbar", "Humayun"], "answer": "Babur"},
        {"q": "Which ancient wonder was in Babylon?", "options": ["Hanging Gardens", "Colossus of Rhodes", "Great Pyramid"], "answer": "Hanging Gardens"},
        {"q": "Who was known as the 'Father of the Nation' in India?", "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose"], "answer": "Mahatma Gandhi"},
        {"q": "Which ancient city was buried by volcanic ash from Mount Vesuvius?", "options": ["Pompeii", "Athens", "Rome"], "answer": "Pompeii"},
    ]

    # Pick 7 random questions
    selected_questions = random.sample(question_bank, 7)

    # Store answers
    answers = {}

    st.subheader("📋 Answer all 7 questions:")
    for i, q in enumerate(selected_questions):
        answers[i] = st.radio(f"{i+1}. {q['q']}", q["options"], key=f"q{i}")

    # Submit Button
    if st.button("Submit Quiz"):
        score = 0
        for i, q in enumerate(selected_questions):
            if answers[i] == q["answer"]:
                score += 1

        st.success(f"✅ You scored {score}/7")
        st.info("💡 Refresh the page to try a different set of questions.")

# Run standalone
if __name__ == "__main__":
    quiz_page()