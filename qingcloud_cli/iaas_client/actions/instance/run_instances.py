# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class RunInstancesAction(BaseAction):

    action = 'RunInstances'
    command = 'run-instances'
    usage = '%(prog)s --image_id <image_id> --instance_type <instance_type> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--image_id', dest='image_id',
                action='store', type=str, default='',
                help='映像ID')

        parser.add_argument('-t', '--instance_type', dest='instance_type',
                action='store', type=str, default=None,
                help='主机类型: small_b, small_c, medium_a, medium_b, medium_c,\
                large_a, large_b, large_c')

        parser.add_argument('-c', '--count', dest = 'count',
                action='store', type=int, default=1,
                help='创建的主机数量，默认是1')

        parser.add_argument('-C', '--cpu', dest='cpu',
                action='store', type=int, default=0,
                help='CPU 目前支持: 1, 2, 4, 8, 16')

        parser.add_argument('-M', '--memory', dest='memory',
                action='store', type=int, default=0,
                help='内存 目前支持: 512, 1024, 2048, 4096, 8192, 16384')

        parser.add_argument('-N', '--instance_name', dest='instance_name',
                action='store', type=str, default='',
                help='主机名称')

        parser.add_argument('-n', '--vxnets', dest='vxnets',
                action='store', type=str, default='',
                help='私有网络ID，默认使用系统基础网络')

        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default='',
                help='自建防火墙ID，默认使用系统缺省防火墙')

        parser.add_argument('-m', '--login_mode', dest='login_mode',
                action='store', type=str, default='',
                help='登录模式：keypair or passwd')

        parser.add_argument('-p', '--login_passwd', dest='login_passwd',
                action='store', type=str, default='',
                help='登录密码，当登录模式为`passwd`时需要')

        parser.add_argument('-k', '--login_keypair', dest='login_keypair',
                action='store', type=str, default='',
                help='登录密钥，当登录模式为`keypair`时需要')

        return parser

    @classmethod
    def build_directive(cls, options):

        required_params = {
                'image_id': options.image_id,
                'instance_type': options.instance_type,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: param [%s] should be specified' % param
                return None

        return {
                'image_id': options.image_id,
                'instance_type' : options.instance_type,
                'cpu': options.cpu,
                'memory': options.memory,
                'instance_name' : options.instance_name,
                'count' : options.count,
                'vxnets': explode_array(options.vxnets),
                'security_group': options.security_group,
                'login_mode': options.login_mode,
                'login_passwd': options.login_passwd,
                'login_keypair': options.login_keypair,
                }
