import os


def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            output = output.replace("{" + key + "}", str(value) if value is not None else "N/A")

        filename = f"output_{index}.txt"
        with open(filename, 'w') as f:
            f.write(output)
        print(f"Generated: {filename}")