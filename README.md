# task-wizard

This is a helper project used to support daily routine works.

## Setting up the environment

1. Make sure the `init.sh` file is executable:

    ```.sh
    sudo chmod +x init.sh
    ```

2. Go to the project folder in command line and run the below command:

    ```.sh
    source ./init.sh
    ```

## Project Structure

``` text
/task-wizard
├── .cmds
│   ├── requirements.txt
│   └── setup.sh
├── tasks
│   ├── api_key_generator.py
│   ├── epoch_handler.py
|   └── json_comparator.py
├── init.sh
└── README.md
```

## Running Commands

In your command line run the python script to execute the wizard.

```.sh
./start.sh
```

You will see the below message shown:

```.sh
(1) Generate API keys
(2) Extend epochs
(3) Compare JSON files
Enter your choice: 
```

Enter either one of these options and then follow the instructions if further input is needed.
