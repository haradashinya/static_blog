date: 2013-06-27
title: Python3


Python3になって、importの挙動が変わったので今までのやり方ではうまく行かなくなった。

階層が

sand/lib/lib.py

sand/models/user.py

だったとして、lib.pyからuser.pyをimportしたい時は、sys.pathに依存モジュールを追加すればいけた。




    import os
    import sys
    p =  os.path.join(os.path.abspath(""),"models/user")
    sys.path.append(p)

