# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class AllocateEipsAction(BaseAction):

    action = 'AllocateEips'
    command = 'allocate-eips'
    usage = '%(prog)s --bandwidth <bandwidth> --count <count> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-c', '--count', dest='count',
                action='store', type=int, default=1,
                help='the number of the eips you want to allocate. Default 1')

        parser.add_argument('-b', '--bandwidth', dest='bandwidth',
                action='store', type=int, default=None,
                help='the bandwidth of the eip. Unit is MB.')

        parser.add_argument('-i', '--need_icp', dest='need_icp',
                action='store', type=int, default=0,
                help='whether need ICP code.')

        parser.add_argument('-n', '--eip_name', dest='eip_name',
                action='store', type=str, default='',
                help='the short name of eip')

    @classmethod
    def build_directive(cls, options):
        required_params = {'bandwidth': options.bandwidth}
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None

        return {
                'count': options.count,
                'bandwidth': options.bandwidth,
                'eip_name' : options.eip_name,
                'need_icp': options.need_icp,
                }
