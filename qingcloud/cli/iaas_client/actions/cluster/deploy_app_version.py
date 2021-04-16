# =========================================================================
# Copyright 2012-present Yunify, Inc.
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

from qingcloud.iaas import constants as const
from qingcloud.cli.iaas_client.actions.base import BaseAction


class DeployAppVersionAction(BaseAction):

    action = const.ACTION_DEPLOY_APP_VERSION
    command = 'deploy-app-version'
    usage = '%(prog)s -v <version_id> -c <conf> [-d <debug>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-v', '--version_id', dest='version_id',
                            action='store', type=str, default=None,
                            help='the ID of application version which you want to create.')

        parser.add_argument('-c', '--conf', dest='conf',
                            action="store", type=str,  default=None,
                            help='the json format string of config to create the cluster')

        parser.add_argument('-d', '--debug', dest='debug',
                            action="store", type=int, default=0,
                            help='whether to open debug mode [0 or 1]')

    @classmethod
    def build_directive(cls, options):
        if options.version_id is None:
            print('error: version_id should be specified.')
            return None

        if options.conf is None:
            print('error: conf should be specified.')
            return None

        directive = {
            "version_id": options.version_id,
            "conf": options.conf,
            "debug": options.debug}

        return directive
