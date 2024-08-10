import random

# Define all scale degrees
SCALE_DEGREES = {
    'Major': ['Tonic', 'Supertonic', 'Mediant', 'Subdominant', 'Dominant', 'Submediant', 'Leading'],
    'Natural Minor': ['Tonic', 'Supertonic', 'Mediant', 'Subdominant', 'Dominant', 'Submediant', 'Subtonic'],
    'Harmonic Minor': ['Tonic', 'Supertonic', 'Mediant', 'Subdominant', 'Dominant', 'Submediant', 'Leading'],
    'Melodic Minor Ascending': ['Tonic', 'Supertonic', 'Mediant', 'Subdominant', 'Dominant', 'Submediant', 'Leading'],
    'Melodic Minor Descending': ['Tonic', 'Supertonic', 'Mediant', 'Subdominant', 'Dominant', 'Submediant', 'Subtonic'],
}

NOTES_IN_KEY = {
    # Major Keys
    'C Major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'G Major': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    'D Major': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    'A Major': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
    'E Major': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    'B Major': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
    'F# Major': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#'],
    'C# Major': ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'],
    'F Major': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
    'Bb Major': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
    'Eb Major': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
    'Ab Major': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
    'Db Major': ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],
    'Gb Major': ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F'],
    'Cb Major': ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb'],

    # Natural Minor Keys
    'A Minor': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'E Minor': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
    'B Minor': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A'],
    'F# Minor': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E'],
    'C# Minor': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
    'G# Minor': ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'],
    'D# Minor': ['D#', 'E#', 'F#', 'G#', 'A#', 'B', 'C#'],
    'A# Minor': ['A#', 'B#', 'C#', 'D#', 'E#', 'F#', 'G#'],
    'D Minor': ['D', 'E', 'F', 'G', 'A', 'Bb', 'C'],
    'G Minor': ['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F'],
    'C Minor': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
    'F Minor': ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb'],
    'Bb Minor': ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab'],
    'Eb Minor': ['Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db'],
    'Ab Minor': ['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb'],
}

# Function to generate a quiz question
def generate_question(scale_type, key):
    notes = NOTES_IN_KEY[key]
    functions = SCALE_DEGREES[scale_type]
    index = random.randint(0, 6)
    note = notes[index]
    function = functions[index]
    return note, function

# Command line interface for the quiz
def quiz():
    print("Welcome to the Note Function Quiz!")
    while True:
        key = input("Enter a key (e.g., C Major, A Minor, etc.): ").strip()
        if key not in NOTES_IN_KEY:
            print("Invalid key. Please try again.")
            continue

        scale_type = 'Major' if 'Major' in key else 'Natural Minor'
        num_questions = int(input("How many questions would you like? "))

        correct_answers = 0
        for _ in range(num_questions):
            note, function = generate_question(scale_type, key)
            answer = input(f"What is the function of the note {note} in the {key} scale? ").strip()
            if answer.lower() == function.lower():
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Incorrect. The correct answer is {function}.")

        print(f"You answered {correct_answers} out of {num_questions} correctly.")

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break


if __name__ == "__main__":
    quiz()
