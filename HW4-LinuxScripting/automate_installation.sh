#!/bin/bash

# Install Python
install_python() {
    echo "Installing Python..."
    if ! python3.7.17 --version &>/dev/null; then
        sudo apt-get update
        sudo apt-get install -y python3.7.17
        sudo apt-get install python3-pip
    else
        echo "Python 3.9 is already installed."
    fi
}

install_mysql() {
    echo "Installing MySQL..."
    if ! mysql --version &>/dev/null; then
        sudo apt-get update
        sudo apt-get install -y mysql-server libmysqlclient-dev
    else
        echo "MySQL is already installed."
    fi
}

#install_dependencies() {
#    echo "Installing dependencies..."
#    if ! dpkg -l | grep -q 'python3-dev' || \
#       ! dpkg -l | grep -q 'libxml2-dev' || \
#       ! dpkg -l | grep -q 'libxslt-dev'; then
#        sudo apt-get update
#        sudo apt-get install -y python3-dev libxml2-dev libxslt-dev
#    else
#        echo "Required dependencies are already installed."
#    fi
#}

setup_virtual_environment() {
    echo "Setting up virtual environment..."
    sudo pip3 install virtualenv
    mkdir envs
    virtualenv -p python3.7.17 ./envs/

}

#install_django() {
#    echo "Installing Django..."
#    #source envs/bin/activate
#    #pip3 install django
#    #pip3 install django-haystack
#    #pip3 install phonenumber_field
#}

#grant_mysql_privileges() {
#    echo "Granting MySQL privileges..."
#    mysql -u root -p -e "GRANT ALL PRIVILEGES ON *.* TO 'nikita'@'localhost' WITH GRANT OPTION;"
#    mysql -u root -p -e "FLUSH PRIVILEGES;"
#}

clone_repository() {
    echo "Cloning git repository..."
    git clone "https://github.com/Manisha-Bayya/simple-django-project.git"
    cd simple-django-project/

    # Copy the world.sql file to the home directory
    cp world.sql ~/world.sql
}

install_requirements() {
    echo "Installing Python packages and dependencies..."
#    pip3 list --format=freeze > requirements.txt
    source ../envs/bin/activate
    pip3 install -r requirements.txt
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
    source ../envs/bin/activate

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
    echo "Run server ..."
    echo "Activate virtual environment"
    # Activate virtual environment
    source ../envs/bin/activate

#    pip3.9 install django
    echo "Make migrations"
    # Make migrations
    python3.7 manage.py makemigrations
    python3.7 manage.py migrate

    echo "For search feature we need to index certain tables to the haystack. For that run below command."
    # For search feature we need to index certain tables to the haystack. For that run below command.
    python3.7 manage.py rebuild_index

    # Check if Django is installed in the virtual environment
#    if ! python3 -c "import django" &>/dev/null; then
#        echo "Django is not installed in the virtual environment. Installing..."
#        install_django
#    fi
    echo "Run the server"
    # Run the server
    python3.7 manage.py runserver 0:8001

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
#    install_dependencies
    setup_virtual_environment
#    install_django

    clone_repository
    install_requirements
#    grant_mysql_privileges
    load_sample_data "$mysql_user" "$mysql_password"
    edit_project_setting "$mysql_user" "$mysql_password" "$mysql_host" "$mysql_port" "$email" "$email_password"
    run_server
}

main "$@"