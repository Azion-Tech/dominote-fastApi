
#check if vitual environment is active
disconnectVirtualEnv() {
  # check if virtual environment is active
    if [ -z "$VIRTUAL_ENV" ]; then
        echo "No virtual environment is active. Please activate it first."
    else
        echo "Deactivating virtual environment..."
        deactivate
        echo "Virtual environment deactivated."
    fi
}
