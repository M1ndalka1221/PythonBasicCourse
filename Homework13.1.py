import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    text_without_tags = re.sub(r'<[^>]+>', '', html)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(text_without_tags)

delete_html_tags('draft.html')