# LEX-encrypt

Made this simple python encryption program in a few hours as an afternoon project because I was bored.
You can use this if you want, just make sure to remember the passwd because there's no password reset/strip like some ZIPs!!
Made this open-source because everything should be open-source.

# USAGE
lex encrypt <filename> <!-- this is to encrypt
lex decrypt <filename including the .lex that encrypt added!> <!-- this is to decrypt

#Building and how to use and stuff
In releases there should be binaries for both Windows (virgin OS) and Linux (based OS)
Windows: You can use it portably in any directory or add it to your path
Linux: Just: sudo cp lex /bin/

If you want to build this program yourself instead of using the prebuilt binaries then you can run this command:
pyinstaller --onefile --icon=icon.ico lex.py
