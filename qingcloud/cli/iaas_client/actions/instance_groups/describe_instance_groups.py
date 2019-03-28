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


class DescribeInstanceGroupsAction(BaseAction):

    action = 'DescribeInstanceGroups'
    command = 'describe-instance-groups'
    usage = '%(prog)s [-i "instance_group_id,..."] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-g', '--instance_groups', dest='instance_groups',
                            action='store', type=str, default=None,
                            help='the comma separated IDs of groups you want to describe.')

        parser.add_argument('-r', '--relation', dest='relation',
                            action='store', type=str,
                            help='relations: repel, attract.')

        parser.add_argument('-o', '--owner', dest='owner',
                            action='store', type=str,
                            help='filter condition: the owner id.')

        parser.add_argument('-v', '--verbose', dest='verbose',
                            action='store', type=str, default=0,
                            help='default is 0，i.e. doesn\'t return the instance info in this group.')

    @classmethod
    def build_directive(cls, options):

        return {
            'instance_groups': explode_array(options.instance_groups),
            'relation': options.relation,
            'tags': explode_array(options.tags),
            'owner': options.owner,
            'verbose': options.verbose,
            'offset': options.offset,
            'limit': options.limit
        }
