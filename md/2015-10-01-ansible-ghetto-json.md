title: ghetto_json for Ansible
slug: ansible-ghetto-json
date: 2015-10-01T20:37:28+0100

[ansible-ghetto-json](https://github.com/FauxFaux/ansible-ghetto-json) is an
ansible module for making quick edits to JSON files.

Ansible has great [built-in support for ini files](https://docs.ansible.com/ansible/ini_file_module.html),
 but a number of more modern applications are using JSON for config files.

`ghetto_json` lets you make some types of edits to JSON files, and remains simple enough that
 it's hopefully easier just to extend than to switch to a different module, and you won't feel
 too guilty just copy-pasting it into your codebase.

More details are in its README, which you can view on the above github link.

It offers an interesting oppotunity to think about type conversion:
JSON actually supports more types than you would normally think of;
ints, floats, `null`s, booleans, as well as the trusty string type. Python,
which I still don't think of as a typed language, uses and honours these types
in its JSON module, meaning you have to do conversion.

And, if it explicitly supports `null`, how do you do removals?  I made up a new
keyword, `unset`, which removes the key.  Pretty ghetto.

