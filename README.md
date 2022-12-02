## Install

- Linux : `python3 -m pip install easydb-json`
- Windows : `python -m pip install easydb-json`

# Author

**Discord** : *[Lactua#6319](https://discord.com/users/679390415929081856)*

**Github**: *[https://github.com/lactua](https://github.com/lactua)*

# Documentation

* ## Get started

    To start, you have to create your database in your code by using the *init* function.

    ### init (function)

    The *init* function return you a dict that you can edit and that will be saved in the *path* that you gave.

    |Parameter|Type|Description|
    |:-|:-|:-|
    |path|string|The path of the database file

    Example : 
    ```py
    from easydb-json import init

    mydb = init('NiceDir/NiceFile.json')
    ```

* ## Interact with the database

    When you edit the dict that is return from the init function, it automaticly edit the database file. So to interact with the database, interact with the dict.

    Example :
    ```py
    from easydb-json import init

    mydb = init('NiceDir/NiceFile.json')

    mydb['name'] = 'Lactua'
    print(mydb['name'])

    mydb['name'] = 'Luctau'
    print(mydb['name'])

    del mydb['name']
    ```
    Output :
    ```txt
    Lactua
    Luctau
    ```

