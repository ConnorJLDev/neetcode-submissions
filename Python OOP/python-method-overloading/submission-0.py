class TextProcessor:

    def format_text(self, text: str, text2: str = None) -> str:
        if text2 is None: 
            return text.upper();
        else:
            return text + text2;


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
