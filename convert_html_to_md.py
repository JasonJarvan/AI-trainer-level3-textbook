#!/usr/bin/env python3
"""
Convert HTML files to Markdown format.
Extracts body content from HTML files and converts to Markdown.
"""

import os
import re
import glob
from pathlib import Path

def html_to_markdown(html_content):
    """
    Convert HTML content to Markdown format.
    This is a basic conversion that handles common HTML tags.
    """
    # Extract content between <body> and </body> tags
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
    if body_match:
        content = body_match.group(1)
    else:
        # If no body tags found, use the entire content
        content = html_content
    
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Convert headers (h1-h6)
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Convert bold and italic
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Convert code blocks and inline code
    content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Convert links
    content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Convert images
    content = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*/?>', r'![\2](\1)', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<img[^>]*alt=["\']([^"\']*)["\'][^>]*src=["\']([^"\']*)["\'][^>]*/?>', r'![\1](\2)', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*/?>', r'![](\1)', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Convert lists
    content = re.sub(r'<ul[^>]*>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'</ul>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<ol[^>]*>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'</ol>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Convert paragraphs
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Convert line breaks
    content = re.sub(r'<br\s*/?>', '\n', content, flags=re.IGNORECASE)
    
    # Convert horizontal rules
    content = re.sub(r'<hr[^>]*/?>', '\n---\n', content, flags=re.IGNORECASE)
    
    # Convert blockquotes
    content = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'> \1', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Convert tables (basic conversion)
    content = re.sub(r'<table[^>]*>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'</table>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<tr[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'</tr>', '\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<th[^>]*>(.*?)</th>', r'| \1 ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<td[^>]*>(.*?)</td>', r'| \1 ', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove any remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Clean up whitespace
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)  # Remove excessive blank lines
    content = re.sub(r'^\s+', '', content, flags=re.MULTILINE)  # Remove leading whitespace
    content = content.strip()
    
    # Decode HTML entities
    content = content.replace('&amp;', '&')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = content.replace('&quot;', '"')
    content = content.replace('&#39;', "'")
    content = content.replace('&nbsp;', ' ')
    
    return content

def convert_html_file(html_file_path):
    """
    Convert a single HTML file to Markdown.
    """
    try:
        # Read the HTML file
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Convert to Markdown
        markdown_content = html_to_markdown(html_content)
        
        # Create the output file path
        md_file_path = html_file_path.replace('.html', '.md')
        
        # Write the Markdown file
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✓ Converted: {html_file_path} -> {md_file_path}")
        return True
    
    except Exception as e:
        print(f"✗ Error converting {html_file_path}: {str(e)}")
        return False

def main():
    """
    Main function to convert all HTML files to Markdown.
    """
    # Get current working directory
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")
    
    # Get all HTML files in numbered folders
    html_files = glob.glob('**/*.html', recursive=True)
    
    # Also try with explicit path patterns
    if not html_files:
        # Try pattern matching for numbered folders
        for pattern in ['*.*.*/*.html', '[0-9].*.*/*.html']:
            found_files = glob.glob(pattern)
            html_files.extend(found_files)
    
    # Filter to only include files in numbered folders (like 1.1.1, 2.1.1, etc.)
    # Use os.path.sep for cross-platform compatibility
    numbered_folder_pattern = re.compile(r'^\d+\.\d+\.\d+[/\\]')
    html_files = [f for f in html_files if numbered_folder_pattern.match(f.replace(os.path.sep, '/'))]
    
    print(f"Found {len(html_files)} HTML files to convert:")
    for file in html_files:
        print(f"  - {file}")
    
    print("\nStarting conversion...")
    
    successful_conversions = 0
    failed_conversions = 0
    
    for html_file in html_files:
        if convert_html_file(html_file):
            successful_conversions += 1
        else:
            failed_conversions += 1
    
    print(f"\nConversion complete!")
    print(f"✓ Successfully converted: {successful_conversions}")
    print(f"✗ Failed conversions: {failed_conversions}")

if __name__ == "__main__":
    main()