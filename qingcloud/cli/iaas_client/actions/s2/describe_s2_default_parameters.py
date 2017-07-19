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

from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeS2DefaultParametersAction(BaseAction):
    action = 'DescribeS2DefaultParameters'
    command = 'describe-s2-default-parameters'
    usage = '%(prog)s [-T <service_type> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-T", "--service-type", dest="service_type",
                            action="store", type=str, default=None,
                            help="valid values is vsan or vnas.")

        parser.add_argument("-t", "--target-type", dest="target_type",
                            action="store", type=str, default=None,
                            help="valid values is ISCSI, FCoE, NFS or SMB.")


    @classmethod
    def build_directive(cls, options):
        directive = {
            "service_type": options.service_type,
            "target_type": options.target_type,
        }
        
        return directive
