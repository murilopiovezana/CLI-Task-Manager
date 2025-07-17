# CLI Task Manager

A feature-rich, command-line task manager built with Python. This project was developed as an assignment for the MC102 course, focusing on object-oriented programming, data persistence, and building a complete, interactive application.

The application allows users to manage their to-do items directly from the terminal, organizing them into lists, setting priorities, and scheduling recurring tasks. All data is saved locally, so your tasks are never lost between sessions.

## Features

-   **Create, Edit, and Delete Tasks:** Full CRUD (Create, Read, Update, Delete) functionality for your to-do items.
-   **Organize with Lists:** Group related tasks into lists (e.g., "Work," "University," "Personal") for better organization.
-   **Prioritize Your Work:** Assign one of four priority levels (High, Medium, Low, None) to focus on what matters most.
-   **Recurring Tasks:** Set tasks to repeat daily, weekly, monthly, or yearly. Completing a recurring task automatically schedules the next one.
-   **Search & Filter:** A powerful search function to find tasks by name or notes. You can also filter tasks by list, due date, or completion status.
-   **Persistent Storage:** The application uses a simple file-based system to save all tasks and lists, ensuring your data persists after the program closes.

## How to Use

This project runs entirely in your terminal and requires only a standard Python installation.

1.  **Open your terminal** in the project directory.
2.  **Run the application** using the following command:
    ```bash
    python lista_de_tarefas.py
    ```

3.  **Follow the on-screen menus** to manage your tasks.

**Important Note:** The program follows a single-action-per-execution model. After you complete an action (like creating a task), the script will save your changes and exit. Simply run it again to perform the next action. Your data is always preserved.

### Example Session

```
$ python lista_de_tarefas.py
Ola
O que voce quer fazer?
(C): Criar uma nova tarefa ou lista
(L): Buscar uma lista de tarefas
(B): Buscar uma tarefa
(V): Ver tarefas Concluidas
(Q): Fechar programa
C
O que deseja criar?
(T): Tarefa (L): Lista (R): Retornar
T
digite o titulo do nota:
Finish the project report
Por favor, informe a data no formato YY MM DD
2024 10 28
...
```

## File Structure

The application's data is stored in hidden files within the project directory:

-   `.maximo_id` & `.maximo_id_lista`: Counters to ensure unique IDs for new tasks and lists.
-   `.arquivo_tarefas` & `.arquivo_listas`: Index files that list all existing task and list IDs.
-   `.tarefa<ID>`: A separate file for each task, containing its title, due date, priority, etc.
-   `.lista<ID>`: A file containing the name of a specific list.

This simple persistence model makes the application portable and easy to understand.
