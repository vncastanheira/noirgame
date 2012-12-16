from cx_Freeze import setup, Executable


setup(
  name = "noirGame",
  version = "0.1 beta",
  description = "Game of shadows",
  executables = [Executable("main.py")])