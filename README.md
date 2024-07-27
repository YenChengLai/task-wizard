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
