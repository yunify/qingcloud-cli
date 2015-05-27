===============
QingCloud CLI 
===============

qingcloud-cli is the command line interface for managing QingCloud resources,
with it you can check, create, delete and operate all your resources,
it supports Linux, Mac and Windows for now.

This CLI is licensed under
`Apache Licence, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>`_.
  
.. note::
  Requires Python 2.6 or higher, for more information please see
  `QingCloud CLI Documentation <https://docs.qingcloud.com/cli/>`_
  

-------------
Installation
-------------

Install via `pip <http://www.pip-installer.org>`_ ::

    $ pip install qingcloud-cli

If not installed in ``virtualenv``, maybe ``sudo`` is needed ::

    $ sudo pip install qingcloud-cli

Upgrade to the latest version ::

    $ pip install --upgrade qingcloud-cli


--------------------
Command Completion
--------------------

qingcloud-cli has auto-completion (only support Linux and Mac).

If auto-completion doesn't take effect, please activate it manually.::

  $ source ~/.bash_profile

If still doesn't work, please input::

  $ complete -C qingcloud_completer qingcloud

and add this command into your login shell (such as ``~/.bash_profile``).

-----------------
Getting Started
-----------------

To use qingcloud-cli, there must be a configuration file to configure your own
``qy_access_key_id`` , ``qy_secret_access_key`` and ``zone`` , such as::

  qy_access_key_id: 'QINGCLOUDACCESSKEYID'
  qy_secret_access_key: 'QINGCLOUDSECRETACCESSKEYEXAMPLE'
  zone: 'pek1'

access key can be applied for in `Qingcloud Console <https://console.qingcloud.com/access_keys/>`_.
zone is the Node ID where your resources are,
and it can be checked in the switching node on the console,
such as ``pek1``, ``pek2``, ``gd1``, ``ap1`` .

The configuration file is saved in ``~/.qingcloud/config.yaml`` by default,
it also can be assigned by the parameter ``-f /path/to/config``
when executing the command.


----------------
Input Parameters
----------------

The parameters of qingcloud-cli only include ``int`` and ``string`` type.
If the parameters support the list passing,
the values shall be separated by *English comma* . For example::

  qingcloud iaas describe-keypairs -k 'kp-bn2n77ow, kp-b2ivaf15' -L 2

Sometimes, the parameter needs to be string in JSON format, such as::

  qingcloud iaas add-router-statics -r rtr-ba2nbge6 -s '[{"static_type":1,"val1":"80","val2":"192.168.99.2","val3":"8000"}]'


--------------
Command Output
--------------

The returned result of Command is in JSON format.
For example, the returned result of describe-keypair.::

  {
    "action":"DescribeKeyPairsResponse",
    "total_count":2,
    "keypair_set":[
      {
        "description":null,
        "encrypt_method":"ssh-rsa",
        "keypair_name":"kp 1",
        "instance_ids":[
          "i-ogbndull"
        ],
        "create_time":"2013-08-30T05:13:50Z",
        "keypair_id":"kp-bn2n77ow",
        "pub_key":"AAAAB3..."
      },
      {
        "description":null,
        "encrypt_method":"ssh-rsa",
        "keypair_name":"kp 2",
        "create_time":"2013-08-31T05:13:50Z",
        "keypair_id":"kp-b2ivaf15",
        "pub_key":"AAAAB3..."
      }
    ],
    "ret_code":0
  }
