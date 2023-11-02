import openai
import config
import typer
from rich import print
from rich.table import Table

def main():
    openai.api_key = config.api_key

    #Bienvenida del la aplicación
    print("💬[bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando","Descripción")
    table.add_row("'exit'","Salir de la aplicación")
    table.add_row("'new'","Iniciar una nueva conversación con el asistente")

    print(table)

    #Contexto del asistente
    context = {"role": "system", "content": "Eres una asistete muy util" }
    messages = [context]

    while True:
        #Propmt es la entrada de texto que da el usuario al asistente
        
        content = __prompt()

        if content == "new":
            print("\n---💻Nueva convesación creada---\n")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content" : content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages)

        response_content = response.choices[0].message.content

        messages.append({"role":"assistant", "content":response_content})

        print(f"[bold green]> [/bold green][green] {response_content}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar?")
        
    if prompt == "exit":
        exit = typer.confirm("✋ ❗❗¿Estás seguro de que deseas salir?")
        if exit:
            print("¡Hasta Luego! ✌")
            raise typer.Abort()
        return __prompt

    return prompt

if __name__ == "__main__":
    typer.run(main)
