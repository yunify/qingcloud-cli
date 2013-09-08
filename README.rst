==============
qingcloud-cli
==============

*Command Line Interface for QingCloud*

qingcloud-cli 是 `QingCloud 青云 <https://www.qingcloud.com>`_ 的命令行接口，
可以通过它对青云的资源进行查看、创建和操作。

.. note:: 更多文档及样例可查看
  `QingCloud CLI 文档 <https://docs.qingcloud.com/cli/>`_


------------
Installation
------------

可使用 ``pip`` 安装::

    $ pip install qingcloud-cli

如果不是在 ``virtualenv`` 上安装，则需要 ``sudo`` ::

    $ sudo pip install qingcloud-cli

如果你已安装 qingcloud-cli 并需要更新到最新版本，则可以::

    $ pip install --upgrade qingcloud-cli


------------------
Command Completion
------------------

qingcloud-cli 包含命令自动补全功能 (目前只支持 linux 系统)。

如果补全功能没有自动生效，请手动激活一下::

  $ source ~/.bashrc

如果还不行，则输入 ``complete`` 命令::

  $ complete -C qingcloud_completer qingcloud

并可将这条命令加到你的启动脚本中 (如 ``~/.bash_profile``) 方便以后使用。


---------------
Getting Started
---------------

使用 qingcloud-cli 必需一个配置文件，配置你自己的 ``qy_access_key_id`` 和
``qy_secret_access_key`` 以及 ``zone`` 。比如::

  qy_access_key_id: 'QINGCLOUDACCESSKEYID'
  qy_secret_access_key: 'QINGCLOUDSECRETACCESSKEYEXAMPLE'
  zone: 'pek1'

access key 可在 `青云控制台 <https://console.qingcloud.com>`_ 申请，
zone 目前只有一个: pek1 。

配置文件默认放在 ``~/.qingcloud/config.yaml`` ，也可在每次执行命令时以参数
``-f /path/to/config`` 方式来指定。


--------------------
Parameter Input
--------------------

qingcloud-cli 的参数只有 int 和 string 类型。如果参数支持传递列表，则多个值之间以
*英文逗号* ``,`` 分隔。如::

  qingcloud iaas describe-keypairs -k kp-bn2n77ow,kp-b2ivaf15 -L 2

有时参数需要是 JSON 格式的字符串，如::

  qingcloud iaas add-router-statics -r rtr-ba2nbge6 -s '[{"static_type":1,"val1":"80","val2":"192.168.99.2","val3":"8000"}]'


----------------
Command Output
----------------

Command 的返回结果为 JSON 结构。例如 describe-keypair 的返回结果::

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
