import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    text = re.sub(r'<[^>]+>', '', html)
    cleaned_lines = [line.strip() for line in text.split('\n') if line.strip()]
    cleaned_text = '\n'.join(cleaned_lines)
    with codecs.open(result_file, 'w', 'utf-8') as output:
        output.write(cleaned_text)