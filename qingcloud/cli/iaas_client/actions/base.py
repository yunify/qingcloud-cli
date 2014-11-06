# coding: utf-8

import sys
from argparse import ArgumentParser

from qingcloud.iaas.connection import APIConnection

from qingcloud.cli.iaas_client.handler import IaasHandler
from qingcloud.cli.misc.utils import load_conf, send_request, get_expire_time

class BaseAction(object):

    action = ''
    command = ''
    usage = ''
    description = ''

    @classmethod
    def get_argument_parser(cls):
        parser = ArgumentParser(
                prog='qingcloud iaas %s' % cls.command,
                usage=cls.usage,
                description=cls.description
                )

        cls.add_common_arguments(parser)
        cls.add_ext_arguments(parser)
        return parser

    @classmethod
    def add_common_arguments(cls, parser):
        parser.add_argument('-z', '--zone', dest='zone',
                action='store', type=str, default=None,
                help='the ID of zone you want to access, this will override zone ID in config file.')

        parser.add_argument('-f', '--config', dest='conf_file',
                action='store', type=str, default='~/.qingcloud/config.yaml',
                help='config file of your access keys')

        if cls.command.startswith('describe-'):
            parser.add_argument('-O', '--offset', dest='offset',
                    action='store', type=int, default=0,
                    help='the starting offset of the returning results.')

            parser.add_argument('-L', '--limit', dest='limit',
                    action='store', type=int, default=20,
                    help='specify the number of the returning results.')

    @classmethod
    def add_ext_arguments(cls, parser):
        pass

    @classmethod
    def build_directive(cls, options):
        return None

    @classmethod
    def main(cls, args):
        parser = cls.get_argument_parser()
        options = parser.parse_args(args)

        directive = cls.build_directive(options)
        if directive is None:
            parser.print_help()
            sys.exit(-1)

        # load conf
        conf = load_conf(options.conf_file)
        if conf is None:
            sys.exit(-1)
        conf['expires'] = get_expire_time()

        if options.zone:
            conf.update(zone=options.zone)

        # send request
        connection = APIConnection(**conf)
        handler = IaasHandler(connection)
        return send_request(cls.action, directive, handler)
