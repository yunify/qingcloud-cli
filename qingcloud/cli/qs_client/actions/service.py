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

from .base import BaseAction
from ...misc.utils import prints_body

class ListBucketsAction(BaseAction):

    command = "list-buckets"
    usage = "%(prog)s [-z <zone> -f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-z",
            "--zone",
            dest="zone",
            help="On which zone to create the bucket"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        headers = {}
        if options.zone:
            headers["Location"] = options.zone
        resp = cls.conn.make_request("GET", headers=headers)
        prints_body(resp)
