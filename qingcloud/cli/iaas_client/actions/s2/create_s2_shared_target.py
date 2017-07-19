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
from qingcloud.cli.misc.utils import explode_array

from qingcloud.cli.iaas_client.actions.base import BaseAction

class CreateS2SharedTargetAction(BaseAction):
    action = 'CreateS2SharedTarget'
    command = 'create-s2-shared-target'
    usage = '%(prog)s -s <s2_server_id> -n <export_name> -T <target_type> [-d <description> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-server-id", dest="s2_server_id",
                            action="store", type=str, default=None,
                            help="the ID of s2 server.")

        parser.add_argument("-n", "--export-name", dest="export_name",
                            action="store", type=str, default=None,
                            help="the name of shared target.")

        parser.add_argument("-T", "--target-type", dest="target_type",
                            action="store", type=str, default=None,
                            help="valid values includes 'ISCSI', 'FCoE','NFS' and 'SMB'.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="the detailed description of the resource.")

        parser.add_argument("-v", "--volumes", dest="volumes",
                            action="store", type=str, default=None,
                            help="the IDs of volumes will be attached as backstore.")

        parser.add_argument("-i", "--initiator-names", dest="initiator_names",
                            action="store", type=str, default=None,
                            help="specify client IQN, available in vsan.")


    @classmethod
    def build_directive(cls, options):
        for key in ['s2_server_id', 'export_name', 'target_type']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "s2_server_id": options.s2_server_id,
            "export_name": options.export_name,
            "target_type": options.target_type,
            "description": options.description,
            "volumes": explode_array(options.volumes),
            "initiator_names": explode_array(options.initiator_names),
        }
        
        return directive
