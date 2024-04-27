import streamlit as st
import streamlit.components.v1 as components

st.header("Resource Adequacy")

# Read the main HTML file
with open("index.html", 'r', encoding='utf-8') as index_file:
    html_content = index_file.read()

# Read the CSS file for the main HTML
with open("index.css", 'r', encoding='utf-8') as style_file1:
    css_content1 = style_file1.read()

# Read other HTML files referenced in index.html
with open("academics.html", 'r', encoding='utf-8') as academics_file:
    academics_html = academics_file.read()
with open("academics.css", 'r', encoding='utf-8') as style_file2:
    css_content2 = style_file2.read()

with open("contact.html", 'r', encoding='utf-8') as contacts_file:
    contacts_html = contacts_file.read()
with open("contact.css", 'r', encoding='utf-8') as style_file3:
  css_content3 = style_file3.read()

with open("personal.html", 'r', encoding='utf-8') as personal_file:
    personal_html = personal_file.read()
with open("personal.css", 'r', encoding='utf-8') as style_file4:
  css_content4 = style_file4.read()

# Read CSS files associated with other HTML files if applicable

# Concatenate all HTML content
full_html_content = html_content + academics_html + contacts_html + personal_html
full_css_content = css_content1 + css_content2 + css_content3 + css_content4

# Display HTML content along with CSS
components.html(full_html_content, height=1500, scrolling=True, css=full_css_content)
