import csv
from datetime import datetime
import os

def get_column_display_name(original_name):
    # Mapping of original column names to display names
    column_map = {
        'model': 'GPU',
        'price': 'Pris',
        '1440p Ultra FPS': 'FPS*',
        'Price per FPS': 'PPFPS†',
        'canonical_url': 'Link'
    }
    return column_map.get(original_name, original_name)

def format_cell(cell, header):
    # Add kr to price column
    if header.lower() == 'price':
        return f"{cell} kr"

    # Make link for canonical_url column
    if header == 'canonical_url':
        return f'<a href="{cell}" target="_blank">Finn annonse</a>'

    return cell

def csv_to_html(csv_file):
    mod_time = os.path.getmtime(csv_file)
    mod_time_str = datetime.fromtimestamp(mod_time).strftime('%d.%m.%Y - %H:%M')

    html = []
    html.append(f'<div class="timestamp">Updated: {mod_time_str}</div>')
    html.append('<div class="table-container">')
    html.append('<table cellspacing="0" cellpadding="0">')

    with open(csv_file) as f:
        reader = csv.reader(f)
        headers = next(reader)

        html.append('<tr>')
        html.append('<th>#</th>')
        for header in headers:
            display_name = get_column_display_name(header)
            if display_name == 'FPS*':
                html.append(f'<th>FPS<a href="#fps-note">*</a></th>')
            elif display_name == 'PPFPS†':
                html.append(f'<th>PPFPS<a href="#ppfps-note">†</a></th>')
            else:
                html.append(f'<th>{display_name}</th>')
        html.append('</tr>')

        # Add data rows
        for rank, row in enumerate(reader, 1):
            html.append('<tr>')
            html.append(f'<td class="rank">{rank}</td>')
            for cell, header in zip(row, headers):
                html.append(f'<td>{format_cell(cell, header)}</td>')
            html.append('</tr>')

    html.append('</table>')
    html.append('</div>')

    # Add footnote
    html.append('<div id="fps-note" class="footnote">')
    html.append('* FPS ved 1440p Ultra, hentet fra: ')
    html.append('<a href="https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html" target="_blank">')
    html.append("Tom's Hardware GPU Hierarchy</a>")
    html.append('</div>')

    html.append('<div id="ppfps-note" class="footnote">')
    html.append('† Pris Per FPS')
    html.append('</div>')
    return '\n'.join(html)

if __name__ == '__main__':
    finngpu_dir = os.path.dirname(os.path.abspath(__file__))
    analysis_file = os.path.join(finngpu_dir, 'analysis.csv')
    
    with open(os.path.join(finngpu_dir, 'table.html'), 'w') as f:
        f.write(csv_to_html(analysis_file))
