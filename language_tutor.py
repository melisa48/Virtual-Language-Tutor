from collections import deque
import random
import datetime
import math

class VirtualLanguageTutor:
    def __init__(self, language):
        self.language = language
        self.vocabulary = {}  # {word: {'translation': translation, 'examples': [examples]}}
        self.grammar_rules = {}  # {rule_name: {'description': description, 'examples': [examples]}}
        self.user_progress = {'vocabulary': {}, 'grammar': {}}

    def add_vocabulary(self, word, translation, examples=[]):
        self.vocabulary[word] = {'translation': translation, 'examples': examples}

    def add_grammar_rule(self, rule_name, description, examples=[]):
        self.grammar_rules[rule_name] = {'description': description, 'examples': examples}

    def user_vocabulary_test(self):
        """Simple vocabulary quiz with multiple choice."""
        if not self.vocabulary:
            print("No vocabulary words available for testing.")
            return

        score = 0
        total = len(self.vocabulary)
        for word, data in self.vocabulary.items():
            translation = data['translation']
            options = [translation] + [self.vocabulary[w]['translation'] for w in random.sample(list(self.vocabulary.keys()), min(3, len(self.vocabulary)-1))]
            random.shuffle(options)
            print(f"\nTranslate '{word}':")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            user_answer = input("Enter the number of your answer: ")
            try:
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(options):
                    if options[user_answer-1] == translation:
                        score += 1
                        print("Correct!")
                    else:
                        print(f"Incorrect. The correct translation is '{translation}'.")
                else:
                    print("Invalid input. Skipping this word.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print(f"\nYour score: {score}/{total} ({(score/total)*100:.2f}%)") 
        self.user_progress['vocabulary'] = score / total

    def user_grammar_test(self):
        """Simple grammar exercise with sentence correction."""
        if not self.grammar_rules:
            print("No grammar rules available for testing.")
            return

        score = 0
        total = len(self.grammar_rules)
        for rule_name, data in self.grammar_rules.items():
            description = data['description']
            example = random.choice(data['examples'])
            print(f"\nApply the rule: {rule_name}")
            print(f"Description: {description}")
            print(f"Example: {example}")
            user_answer = input("Enter your own example: ")

            # Basic check for subject-verb agreement (simplified)
            if rule_name == "Subject-Verb Agreement":
                if self.language == "English":
                    if any(verb in user_answer.lower() for verb in ["am", "is", "are", "was", "were"]): 
                        score += 1
                        print("Correct!")
                    else:
                        print("Incorrect. The verb does not agree with the subject.") 
                elif self.language == "Spanish":
                    if any(verb in user_answer.lower() for verb in ["hablo", "hablas", "habla", "hablamos", "habláis", "hablan"]): 
                        score += 1
                        print("Correct!")
                    else:
                        print("Incorrect. The verb does not agree with the subject.")
                elif self.language == "French":
                    if any(verb in user_answer.lower() for verb in ["parle", "parles", "parle", "parlons", "parlez", "parlent"]): 
                        score += 1
                        print("Correct!")
                    else:
                        print("Incorrect. The verb does not agree with the subject.")
                elif self.language == "Italian":
                    if any(verb in user_answer.lower() for verb in ["parlo", "parli", "parla", "parliamo", "parlate", "parlano"]): 
                        score += 1
                        print("Correct!")
                    else:
                        print("Incorrect. The verb does not agree with the subject.")
                elif self.language == "Turkish":
                    if any(verb in user_answer.lower() for verb in ["konuşuyorum", "konuşuyorsun", "konuşuyor", "konuşuyoruz", "konuşuyorsunuz", "konuşuyorlar"]): 
                        score += 1
                        print("Correct!")
                    else:
                        print("Incorrect. The verb does not agree with the subject.")
                else:
                    print("This feature is a work in progress. Keep practicing!") 
            else:
                print("This feature is a work in progress. Keep practicing!") 

        print(f"\nYour score: {score}/{total} ({(score/total)*100:.2f}%)") 
        self.user_progress['grammar'] = score / total

    def start_learning(self):
        """Guide the user through the learning process."""
        print(f"Welcome to the {self.language} Language Tutor!")
        while True:
            print("\nChoose a learning phase:")
            print("1. Vocabulary")
            print("2. Grammar")
            print("3. Quit") 
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.user_vocabulary_test()
            elif choice == '2':
                self.user_grammar_test()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

# Example Usage
languages = ["English", "Spanish", "French", "Turkish", "Italian"]
print("Available languages:")
for i, lang in enumerate(languages, 1):
    print(f"{i}. {lang}")
language_choice = int(input("Choose a language by entering the corresponding number: "))
chosen_language = languages[language_choice - 1]

tutor = VirtualLanguageTutor(chosen_language)

# Add some vocabulary and grammar rules
if chosen_language == "English":
    tutor.add_vocabulary("hello", "hola")
    tutor.add_vocabulary("thank you", "gracias")
    tutor.add_vocabulary("goodbye", "adiós")
    tutor.add_grammar_rule("Subject-Verb Agreement", "The verb must agree with the subject in number and person.", 
                           ["I speak English.", "We speak English."])
elif chosen_language == "Spanish":
    tutor.add_vocabulary("hola", "hello")
    tutor.add_vocabulary("gracias", "thank you")
    tutor.add_vocabulary("adiós", "goodbye")
    tutor.add_grammar_rule("Subject-Verb Agreement", "The verb must agree with the subject in number and person.", 
                           ["Yo hablo español.", "Nosotros hablamos español."])
elif chosen_language == "French":
    tutor.add_vocabulary("bonjour", "hello")
    tutor.add_vocabulary("merci", "thank you")
    tutor.add_vocabulary("au revoir", "goodbye")
    tutor.add_grammar_rule("Subject-Verb Agreement", "The verb must agree with the subject in number and person.", 
                           ["Je parle français.", "Nous parlons français."])
elif chosen_language == "Turkish":
    tutor.add_vocabulary("merhaba", "hello")
    tutor.add_vocabulary("teşekkür ederim", "thank you")
    tutor.add_vocabulary("güle güle", "goodbye")
    tutor.add_grammar_rule("Subject-Verb Agreement", "The verb must agree with the subject in number and person.", 
                           ["Ben Türkçe konuşuyorum.", "Biz Türkçe konuşuyoruz."])
elif chosen_language == "Italian":
    tutor.add_vocabulary("ciao", "hello")
    tutor.add_vocabulary("grazie", "thank you")
    tutor.add_vocabulary("arrivederci", "goodbye")
    tutor.add_grammar_rule("Subject-Verb Agreement", "The verb must agree with the subject in number and person.", 
                           ["Io parlo italiano.", "Noi parliamo italiano."])

# Start the learning process
tutor.start_learning()





