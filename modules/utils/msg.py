from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.text import Text

console = Console()

def showTitle(title: str):
    """Show a title in the console"""
    console.print(
        Panel.fit(
            f"[bold cyan]{title}[/bold cyan]",
            border_style="cyan"
        )
    )

def showError(message: str):
    """Show an error message in the console"""
    console.print(
        f"[bold red]Error: {message}[/bold red]"
    )

def showSuccess(message: str):
    """Show a success message in the console"""
    console.print(
        f"[bold green]Success: {message}[/bold green]"
    )

def showMenu():
    """Show main menu in the console and return the option selected"""
    options = [
        "[bold cyan]1. Check balance.[/bold cyan]", 
        "[bold cyan]2. Withdraw money.[/bold cyan]", 
        "[bold cyan]3. Deposit money.[/bold cyan]", 
        "[bold cyan]4. Exit.[/bold cyan]"
        ]

    console.print(
        Panel.fit(
            "\n".join(options),
            border_style="cyan",
        )
    )

    option = IntPrompt.ask(
        "[bold cyan]Enter an option[/bold cyan]",
        choices=[str(i) for i in range(1, len(options) + 1)],
        default=1
    )

    return int(option)


def showLoginMenu():
    """Show login menu in the console and return the option selected"""

    options = [
        "[bold cyan]1. Log in.[/bold cyan]", 
        "[bold cyan]2. Sign up.[/bold cyan]", 
        "[bold cyan]3. Exit.[/bold cyan]"
        ]

    console.print(
        Panel.fit(
            "\n".join(options),
            border_style="cyan",
        )
    )

    option = IntPrompt.ask(
        "[bold cyan]Enter an option[/bold cyan]",
        choices=[str(i) for i in range(1, len(options) + 1)],
        default=1
    )
    return int(option)

def showInput(message: str):
    """Show an input message in the console and return the input"""
    return Prompt.ask(Text(message, style="bold cyan"))