@echo off
javac DeckDataGen.java 
REM Arg1 = FileName, Arg2 = People, Arg3 = Decks, Arg4 = SkillCap
java DeckDataGen tounament.csv 100 100 500
javac Preferances.java
java Preferances tounament2.csv 
python Irvings.py
pause