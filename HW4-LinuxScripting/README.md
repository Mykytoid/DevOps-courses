# Automated Django Project Installation and Setup Script

This script is designed to automate the process of installing and setting up a Django project using Python 3.7 and MySQL on your server. It performs the following actions:

- Install Python 3.7
- Install MySQL and necessary dependencies
- Create a virtual environment
- Clone the Django project repository
- Install required Python packages from requirements.txt
- Load sample data into MySQL
- Edit project settings
- Run the Django server

## Usage

1. Give execute permissions to the script:

    ```bash
    chmod +x automate_installation.sh
    ```
2. Сhange the user and password

   default user is "root", password is "password"

2. Run the script:

    ```bash
    ./automate_installation.sh 1.2.3 root password localhost 3306 example@gmail.com myemailpassword

    ```


3. After completion, you can open a web browser and navigate to `http://localhost:8001` to access your Django project.

## Important

- Ensure you have execute permissions for all the commands in the script.
- Make sure your server has internet access as the script downloads packages and clones the repository.
- Be cautious with MySQL security settings. It's recommended to set a strong password for the root user.
