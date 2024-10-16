from transformers import pipeline 

# Load a pre-trained grammar correction model 
grammar_correction = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws") 

def correct_grammar(text): 
    corrected_text = grammar_correction(text, max_length=512, num_return_sequences=1)[0]['generated_text'] 
    return corrected_text 

# Example usage 
input_text = "She go to the store yesterday." 
corrected_text = correct_grammar(input_text) 
print(f"Corrected Text: {corrected_text}") 