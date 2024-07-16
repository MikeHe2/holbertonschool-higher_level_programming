import os

def generate_invitations(template, attendees):


# Verify instance of template and attendees
    if type(template) != str:
        print("Error: Template is not a string")
        return

    if type(attendees) != list:
        print("Error: Attendees is not a list")
        return

    for i in attendees:
        if not isinstance(i, dict):
            print("Error: Attendees is not a list")
            return


# Verify if template and attendees are empty
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return


# Process each attendee
    for i, attendees in enumerate(attendees, start=1):
        message = template

        name = attendees["name"] if attendees["name"] is not None else "N/A"
        event_title = attendees["event_title"] if attendees["event_title"] is not None else "N/A"
        event_date = attendees["event_date"] if attendees["event_date"] is not None else "N/A"
        event_location = attendees["event_location"] if attendees["event_location"] is not None else "N/A"

        message = message.replace("{name}", name)
        message = message.replace("{event_title}", event_title)
        message = message.replace("{event_date}", event_date)
        message = message.replace("{event_location}", event_location)

        output = f'output_{i}.txt'
        if not os.path.exists(output):
            with open(output, "w") as f:
                f.write(message)
        else:
            print(f"{output}: This file already exists")