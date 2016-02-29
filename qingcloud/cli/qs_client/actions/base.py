# =========================================================================
# Copyright 2016-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

import sys
from argparse import ArgumentParser

from qingcloud.qingstor.connection import QSConnection

from ...misc.utils import load_conf
from ..constants import ENDPOINT

class BaseAction(object):

    command = ""
    usage = ""
    description = ""

    conn = None

    @classmethod
    def add_common_arguments(cls, parser):
        parser.add_argument(
            "-f",
            "--config",
            dest="conf_file",
            action="store",
            type=str,
            default="~/.qingcloud/config.yaml",
            help="config file location"
        )

    @classmethod
    def add_ext_arguments(cls, parser):
        pass

    @classmethod
    def get_argument_parser(cls):
        parser = ArgumentParser(
            prog='qingcloud qs %s' % cls.command,
            usage=cls.usage,
            description=cls.description
        )
        cls.add_common_arguments(parser)
        cls.add_ext_arguments(parser)
        return parser

    @classmethod
    def get_connection(cls, conf):
        if cls.command in ("create-bucket", "list-buckets"):
            host = ENDPOINT
        else:
            host = "%s.%s" % (conf["zone"], ENDPOINT)

        return QSConnection(qy_access_key_id=conf["qy_access_key_id"], \
            qy_secret_access_key=conf["qy_secret_access_key"], host=host)

    @classmethod
    def send_request(cls, options):
        return None

    @classmethod
    def main(cls, args):

        parser = cls.get_argument_parser()
        options = parser.parse_args(args)

        # Load config file
        conf = load_conf(options.conf_file)
        if conf is None:
            sys.exit(-1)

        # Get connection to the server
        cls.conn = cls.get_connection(conf)

        # Send request
        return cls.send_request(options)
