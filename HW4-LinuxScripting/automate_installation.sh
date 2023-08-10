#!/bin/bash

# Install Python
install_python() {
    echo "Installing Python..."
    sudo apt-get update
    sudo apt-get install -y python3.11 python3-pip
}

install_mysql() {
    echo "Installing MySQL..."
    sudo apt-get update
    sudo apt-get install -y mysql-server libmysqlclient-dev
}

setup_virtual_environment() {
    echo "Setting up virtual environment..."
    sudo pip install virtualenv
    mkdir envs
    virtualenv -p python3.11 ./envs/
}

clone_repository() {
    echo "Cloning git repository..."
    git clone "https://github.com/Manisha-Bayya/simple-django-project.git"
    cd simple-django-project/

    # Copy the world.sql file to the home directory
    cp world.sql ~/world.sql
}

install_requirements() {
    echo "Installing Python packages and dependencies..."
    #sudo apt-get update
    #sudo apt-get install -y libxml2-dev libxslt-dev
    #source envs/bin/activate
    pip install -r requirements.txt
}

load_sample_data() {
    echo "Loading sample data into MySQL..."

    # Make sure the world.sql file exists in the home directory
    if [ -f ~/world.sql ]; then
        # Load sample data into MySQL
        mysql -u "$1" -p"$2" < ~/world.sql
    else
        echo "world.sql not found in the home directory. Please make sure the file exists and contains the sample data."
        exit 1
    fi
}

edit_project_setting() {
    echo "Editing project settings..."
    settings_file="panorbit/settings.py"

    # Write the contents of the settings.py file to a variable
    settings_content=$(cat "$settings_file")

    # Replace the values in settings_content with the passed arguments
    settings_content=${settings_content//<mysql-user>/$1}
    settings_content=${settings_content//<mysql-password>/$2}
    settings_content=${settings_content//<mysql-host>/$3}
    settings_content=${settings_content//<mysql-port>/$4}
    settings_content=${settings_content//<your-email>/$5}
    settings_content=${settings_content//<your-email-password>/$6}

    # Write the updated content back to the settings.py file
    echo "$settings_content" > "$settings_file"
}

run_server() {
    # Activate virtual environment
    source envs/bin/activate

    # Make migrations
    python3.11 manage.py makemigrations
    python3.11 manage.py migrate

    # For search feature we need to index certain tables to the haystack. For that run below command.
    python3.11 manage.py rebuild_index

    # Run the server
    python3.11 manage.py runserver 0:8001

    # your server is up on port 8001
}

main() {
    version=$1
    mysql_user=$2
    mysql_password=$3
    mysql_host=$4
    mysql_port=$5
    email=$6
    email_password=$7

    install_python
    install_mysql
    setup_virtual_environment
    clone_repository
    install_requirements
    load_sample_data "$mysql_user" "$mysql_password"
    edit_project_setting "$mysql_user" "$mysql_password" "$mysql_host" "$mysql_port" "$email" "$email_password"
    run_server
}

main "$@"

