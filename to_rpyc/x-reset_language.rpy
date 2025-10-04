## File ini untuk load bahasa yang tersimpan saat game start
## Letakkan di folder game/

init -100 python:
    ## Load bahasa dari persistent saat game start
    if hasattr(persistent, 'language'):
        if persistent.language is not None:
            try:
                # Coba load bahasa yang tersimpan
                renpy.change_language(persistent.language)
            except:
                # Jika gagal, gunakan English (default)
                persistent.language = None
                renpy.change_language(None)
    else:
        # Jika belum pernah set, default ke English
        persistent.language = None