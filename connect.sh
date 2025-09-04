
connectVirtualEnv() {
  # check if virtual environment is already active
  if [ -z "$VIRTUAL_ENV" ]; then
      echo "Activating virtual environment..."
      source .venv/bin/activate
      echo "Virtual environment activated."
  else
      echo "Virtual environment is already active."
  fi
}