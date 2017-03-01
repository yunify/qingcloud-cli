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

import os
import sys

from .base import BaseAction
from ...misc.utils import prints_body, json_dumps
from ..constants import (
    BUFSIZE,
    HTTP_OK,
    HTTP_OK_CREATED,
    HTTP_OK_NO_CONTENT,
    HTTP_OK_PARTIAL_CONTENT,
)

class CreateObjectAction(BaseAction):

    command = "create-object"
    usage = "%(prog)s -b <bucket> -k <key> -d <data> [-t <type> -f <conf_file>]"

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
            "-k",
            "--key",
            dest="key",
            help="The object name"
        )
        parser.add_argument(
            "-F",
            "--file",
            dest="file",
            help="The object file"
        )
        parser.add_argument(
            "-d",
            "--data",
            dest="data",
            help="The object data"
        )
        parser.add_argument(
            "-t",
            "--type",
            dest="type",
            default="application/octet-stream",
            help="The object type"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        if options.file:
            if not os.path.isfile(options.file):
                print("No such file: %s" % options.file)
                sys.exit(-1)
            key = options.key or os.path.basename(options.file)
            data = open(options.file, "rb")
        elif options.data:
            key = options.key
            if not key:
                print("Must specify --key parameter")
                sys.exit(-1)
            data = options.data
        else:
            print("Must specify --file or --data parameter")
            sys.exit(1)

        headers = {}
        if options.type:
            headers["Content-Type"] = options.type

        resp = cls.conn.make_request("PUT", options.bucket, key,
                                     headers=headers, data=data)

        if resp.status != HTTP_OK_CREATED:
            prints_body(resp)


class GetObjectAction(BaseAction):

    command = "get-object"
    usage = "%(prog)s -b <bucket> -k <key> [-F <file> -B <bytes> -z <zone> -f <conf_file>]"

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
            "-k",
            "--key",
            dest="key",
            required=True,
            help="The object name"
        )
        parser.add_argument(
            "-F",
            "--file",
            dest="file",
            help="The file that the object content should save to"
        )
        parser.add_argument(
            "-B",
            "--bytes",
            dest="bytes",
            help="The object data range"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        if options.file:
            if os.path.isdir(options.file):
                path = "%s/%s" % (options.file, options.key)
            else:
                path = options.file
        else:
            path = "%s/%s" % (os.getcwd(), options.key)

        directory = os.path.dirname(path)
        if not os.path.isdir(directory):
            print("No such directory: %s" % directory)
            sys.exit(-1)

        headers = {}
        if options.bytes:
            headers["Range"] = "bytes=%s" % options.bytes

        resp = cls.conn.make_request("GET", options.bucket, options.key, headers=headers)

        if resp.status in (HTTP_OK, HTTP_OK_PARTIAL_CONTENT):
            with open(path, "w") as f:
                while True:
                    buf = resp.read(BUFSIZE)
                    if not buf:
                        break
                    f.write(buf)
        else:
            prints_body(resp)


class DeleteObjectAction(BaseAction):

    command = "delete-object"
    usage = "%(prog)s -b <bucket> -k <key> [-f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-b",
            "--bucket",
            dest="bucket",
            type=str,
            required=True,
            help="The bucket name"
        )
        parser.add_argument(
            "-k",
            "--key",
            dest="key",
            required=True,
            help="The object name"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        resp = cls.conn.make_request("DELETE", options.bucket, options.key)
        if resp.status != HTTP_OK_NO_CONTENT:
            prints_body(resp)


class HeadObjectAction(BaseAction):

    command = "head-object"
    usage = "%(prog)s -b <bucket> -k <key> [-f <conf_file>]"

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument(
            "-b",
            "--bucket",
            dest="bucket",
            action="store",
            type=str,
            required=True,
            help="The bucket name"
        )
        parser.add_argument(
            "-k",
            "--key",
            dest="key",
            required=True,
            help="The object name"
        )
        return parser

    @classmethod
    def send_request(cls, options):
        resp = cls.conn.make_request("HEAD", options.bucket, options.key)
        if resp.status == HTTP_OK:
            data = {
                "Content-Length": resp.getheader("content-length"),
                "Content-Type": resp.getheader("content-type"),
                "ETag": resp.getheader("etag"),
                "Last-Modified": resp.getheader("last-modified")
            }
            print(json_dumps(data, indent=2))
        else:
            print("Error: %s %s" % (resp.status, resp.reason))
