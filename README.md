# Lateral slack formatter

## Requirements

* python3
* venv

## Installation

```
git clone git@github.com:filipbec/lateral-slack-formatter.git
cd lateral-slack-formatter
bash install.sh
```

## Instructions

1. Copy email content
2. Go root project directory and run command:
```
bash run.sh
```
3. Open Slack, create a new post and paste formetted content.

## Known issues

#### Single menu item is spread across multiple lines
When one menu item is spread across multiple lines, you will get:

```
ValueError: could not convert string to float:
```

##### Workaround
Copy content of the email in a text editor, remove newlines for items which did not fit into a single line, copy content and run the script again.
