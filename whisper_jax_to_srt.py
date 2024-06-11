import re
from pathlib import Path

def time_to_seconds(timestamp):
    m, s = map(float, timestamp.split(':'))
    return m * 60 + s

# Function to format time in seconds as SRT time (hh:mm:ss,ms)
def format_time(seconds):
    milliseconds = int((seconds - int(seconds)) * 1000)
    seconds = int(seconds)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def time_match(source_text: str):
    # Find the pattern in the source text
    match = re.search(r'\[(\d+:\d+\.\d+) -> (\d+:\d+\.\d+)]', source_text)
    if match:
        start_time, end_time = match.groups()
        # Convert start and end times to seconds
        start_seconds = time_to_seconds(start_time)
        end_seconds = time_to_seconds(end_time)
        # Format the times
        formatted_start = format_time(start_seconds)
        formatted_end = format_time(end_seconds)
        # Replace the existing pattern with the formatted times
        new_text = source_text.replace(match.group(0), f"[{formatted_start} --> {formatted_end}]")
        return new_text
    else:
        return "Pattern not found in the source text."

# Example usage
src_file = r'g:/aud_cap/long_narrate.txt'
src_txt = Path(src_file).read_text(encoding='utf-8')
new_text = time_match(src_txt)
print(new_text[:100])


