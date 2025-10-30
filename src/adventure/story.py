from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("You wake up in a dark forest.", style="bold magenta")
    console.print("You can go left or right.", style="bold magenta")

    while True:
        choice = Prompt.ask("[bold cyan]Which direction do you choose?[/bold cyan] (left/right/exit)").strip().lower()
        if choice == 'exit':
            console.print("Thanks for playing! Goodbye.", style="bold magenta")
            break
        
        result = step(choice, events)
        # Wrap the string in Rich Text with styles
        if "left" in result.lower():
            console.print(result, style="bold green")
        elif "right" in result.lower():
            console.print(result, style="bold blue")
        else:
            console.print(result, style="bold red")
