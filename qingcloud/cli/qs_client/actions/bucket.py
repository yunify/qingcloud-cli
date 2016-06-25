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
from ...misc.utils import prints_body, json_dumps
from ..constants import HTTP_OK, HTTP_OK_CREATED, HTTP_OK_NO_CONTENT

class CreateBucketAction(BaseAction):

    command = "create-bucket"
    usage = "%(prog)s -b <bucket> [-z <zone> -f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-b",
            "--bucket",
            dest="bucket",
            required=True,
            help="The bucket name"
        )

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
        resp = cls.conn.make_request("PUT", options.bucket, headers=headers)
        if resp.status == HTTP_OK_CREATED:
            print "Bucket [%s] is created" % options.bucket
        else:
            prints_body(resp)


class DeleteBucketAction(BaseAction):

    command = "delete-bucket"
    usage = "%(prog)s -b <bucket> [-f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-b",
            "--bucket",
            dest="bucket",
            required=True,
            help="The bucket name"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        resp = cls.conn.make_request("DELETE", options.bucket)
        if resp.status != HTTP_OK_NO_CONTENT:
            prints_body(resp)


class HeadBucketAction(BaseAction):

    command = "head-bucket"
    usage = "%(prog)s -b <bucket> [-f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-b",
            "--bucket",
            dest="bucket",
            required=True,
            help="The bucket name"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        resp = cls.conn.make_request("HEAD", options.bucket)
        if resp.status != HTTP_OK:
            print "Error: %s %s" % (resp.status, resp.reason)


class StatsBucketAction(BaseAction):

    command = "stats-bucket"
    usage = "%(prog)s -b <bucket> [-f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-b",
            "--bucket",
            dest="bucket",
            required=True,
            help="The bucket name"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        params = {"stats": None}
        resp = cls.conn.make_request("GET", options.bucket, params=params)
        prints_body(resp)


class ListObjectsAction(BaseAction):

    command = "list-objects"
    usage = "%(prog)s -b <bucket> [-p <prefix> -d <delimiter> -m <marker> -l " \
            + "<limit> -f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-b",
            "--bucket",
            dest="bucket",
            required=True,
            help="The bucket name"
        )
        parser.add_argument(
            "-p",
            "--prefix",
            dest="prefix",
            help="The specified prefix that returned keys should start with"
        )
        parser.add_argument(
            "-d",
            "--delimiter",
            dest="delimiter",
            help="Which character to use for grouping the keys"
        )
        parser.add_argument(
            "-m",
            "--marker",
            dest="marker",
            help="The key to start with when listing objects in the bucket"
        )
        parser.add_argument(
            "-l",
            "--limit",
            dest="limit",
            type=int,
            default=20,
            help="The maximum number of keys returned"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        params = {}
        if options.prefix:
            params["prefix"] = options.prefix
        if options.delimiter:
            params["delimiter"] = options.delimiter
        if options.marker:
            params["marker"] = options.marker
        if options.limit is not None:
            params["limit"] = str(options.limit)
        resp = cls.conn.make_request("GET", options.bucket, params=params)
        prints_body(resp)


class GetBucketAclAction(BaseAction):

    command = "get-bucket-acl"
    usage = "%(prog)s -b <bucket> [-f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-b",
            "--bucket",
            dest="bucket",
            required=True,
            help="The bucket name"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        params = {"acl": None}
        resp = cls.conn.make_request("GET", options.bucket, params=params)
        prints_body(resp)


class SetBucketAclAction(BaseAction):

    command = "set-bucket-acl"
    usage = "%(prog)s -b <bucket> -A <acl> [-f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-b",
            "--bucket",
            dest="bucket",
            required=True,
            help="The bucket name"
        )
        parser.add_argument(
            "-A",
            "--acl",
            required=True,
            nargs="*",
            help="ACL entries, each entry is in format "
                 "user_id,permission. permission can be READ, "
                 "WRITE or FULL_CONTROL. Multiple entries are separated by spaces"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        params = {"acl": None}
        body = {}
        for pairs in options.acl:
            grantee, perm = pairs.split(",")
            body[grantee] = perm
        resp = cls.conn.make_request("PUT", options.bucket, params=params,
                                     data=json_dumps(body))
        if resp.status != HTTP_OK:
            prints_body(resp)
