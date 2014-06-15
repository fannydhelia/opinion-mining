opinion-mining
==============

A simple opinion mining tool for estonian.


The tool asks user's opinion (about anything) and returns an opinion score. 
Tool also allows to add words to dictionaries (the dictionaries available are created by the authors of this project and only contain a small amount of opinion related words).
As the tool is meant for estonian language, it is only available in estonian.
For more information about the tool, see the poster (in english).


To run, use Python 3 (call "python3 opinion.py").
Also needs a lemmatizer and morf analyzer called t3mesta (H.-J. Kaalep, T.Vaino 1998, OU Filosoft), available in frogger.at.mt.ut.ee server.
Path to t3mesta: /usr/local/materjalid/vaino/korpuslingvistika/prog-lin64/t3mesta
Path to dictionaries of t3mesta:  /usr/local/materjalid/vaino/korpuslingvistika/prog-lin64/
The path to t3mesta and its dictionaries can also be given to the tool, in frogger default paths should work.
re about t3mesta: https://docs.google.com/document/d/1Eqon7wVpNtMjw0P-X8qq1RSqCzlVL7vdiHmVk3dwKKI/edit)
