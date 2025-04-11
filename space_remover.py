def correct_text(text):
    corrected = ' '.join(text.strip().split())
    return corrected

text_sample = "     How    may    spaces     do    you  think I  can      have  in one  sentence?"
corrected_text = correct_text(text_sample)

print("Original text: ", repr(text_sample))
print("Corrected: ", repr(corrected_text))