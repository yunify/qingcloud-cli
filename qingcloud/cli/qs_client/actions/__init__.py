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

from qingcloud.cli.qs_client.actions import key
from qingcloud.cli.qs_client.actions import bucket
from qingcloud.cli.qs_client.actions import service
from qingcloud.cli.qs_client.actions import multipart

class ActionManager(object):

    @classmethod
    def get_action(cls, action):
        for item in cls.action_table:
            if item[0] == action:
                return item[1]

    @classmethod
    def get_valid_actions(cls):
        return [item[0] for item in cls.action_table]

    action_table = [
        ## service ##
        ('list-buckets', service.ListBucketsAction),
        ## bucket ##
        ('create-bucket', bucket.CreateBucketAction),
        ('delete-bucket', bucket.DeleteBucketAction),
        ('head-bucket', bucket.HeadBucketAction),
        ('stats-bucket', bucket.StatsBucketAction),
        ('list-objects', bucket.ListObjectsAction),
        ('get-bucket-acl', bucket.GetBucketAclAction),
        ('set-bucket-acl', bucket.SetBucketAclAction),
        ## object ##
        ('create-object', key.CreateObjectAction),
        ('get-object', key.GetObjectAction),
        ('delete-object', key.DeleteObjectAction),
        ('head-object', key.HeadObjectAction),
        ## multipart ##
        ('initiate-multipart', multipart.InitiateMultipartAction),
        ('upload-multipart', multipart.UploadMultipartAction),
        ('list-multipart', multipart.ListMultipartAction),
        ('complete-multipart', multipart.CompleteMultipartAction),
        ('abort-multipart', multipart.AbortMultipartAction),
    ]
