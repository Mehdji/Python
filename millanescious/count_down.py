
from rich import print as rprint
from rich.progress import track
from rich.console import Console
from time import sleep
import pyfiglet

console = Console()
count_down = 10

for x in range(10,-1,-1):
	sleep(1)
	console.log(f"[red] {pyfiglet.figlet_format(str(x))}[/red]")
	track(range(10),description='df')
console.log(f"[red] BOOM[/red]")



