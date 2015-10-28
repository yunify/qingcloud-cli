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

class IaasHandler(object):
    ''' handle request and send requests to pitrix service '''

    def __init__(self, connection=None):
        self.conn = connection

    def handle(self, action, directive):
        ''' dispatch request to specified handler according to action.
        '''

        handler_map = {
                # jobs
                const.ACTION_DESCRIBE_JOBS: self.conn.describe_jobs,

                # images
                const.ACTION_DESCRIBE_IMAGES: self.conn.describe_images,
                const.ACTION_DELETE_IMAGES: self.conn.delete_images,
                const.ACTION_CAPTURE_INSTANCE: self.conn.capture_instance,
                const.ACTION_MODIFY_IMAGE_ATTRIBUTES: self.conn.modify_image_attributes,

                # instances
                const.ACTION_DESCRIBE_INSTANCES: self.conn.describe_instances,
                const.ACTION_RUN_INSTANCES: self.conn.run_instances,
                const.ACTION_START_INSTANCES: self.conn.start_instances,
                const.ACTION_STOP_INSTANCES: self.conn.stop_instances,
                const.ACTION_RESTART_INSTANCES: self.conn.restart_instances,
                const.ACTION_TERMINATE_INSTANCES: self.conn.terminate_instances,
                const.ACTION_RESIZE_INSTANCES: self.conn.resize_instances,
                const.ACTION_RESET_INSTANCES: self.conn.reset_instances,
                const.ACTION_MODIFY_INSTANCE_ATTRIBUTES: self.conn.modify_instance_attributes,

                # volumes
                const.ACTION_DESCRIBE_VOLUMES: self.conn.describe_volumes,
                const.ACTION_CREATE_VOLUMES: self.conn.create_volumes,
                const.ACTION_DELETE_VOLUMES: self.conn.delete_volumes,
                const.ACTION_ATTACH_VOLUMES: self.conn.attach_volumes,
                const.ACTION_DETACH_VOLUMES: self.conn.detach_volumes,
                const.ACTION_MODIFY_VOLUME_ATTRIBUTES: self.conn.modify_volume_attributes,
                const.ACTION_RESIZE_VOLUMES: self.conn.resize_volumes,

                # key pair
                const.ACTION_DESCRIBE_KEY_PAIRS: self.conn.describe_key_pairs,
                const.ACTION_ATTACH_KEY_PAIRS: self.conn.attach_keypairs,
                const.ACTION_DETACH_KEY_PAIRS: self.conn.detach_keypairs,
                const.ACTION_CREATE_KEY_PAIR: self.conn.create_keypair,
                const.ACTION_DELETE_KEY_PAIRS: self.conn.delete_keypairs,
                const.ACTION_MODIFY_KEYPAIR_ATTRIBUTES: self.conn.modify_keypair_attributes,

                # security groups
                const.ACTION_DESCRIBE_SECURITY_GROUPS: self.conn.describe_security_groups,
                const.ACTION_CREATE_SECURITY_GROUP: self.conn.create_security_group,
                const.ACTION_MODIFY_SECURITY_GROUP_ATTRIBUTES: self.conn.modify_security_group_attributes,
                const.ACTION_APPLY_SECURITY_GROUP: self.conn.apply_security_group,
                const.ACTION_DELETE_SECURITY_GROUPS: self.conn.delete_security_groups,
                const.ACTION_DESCRIBE_SECURITY_GROUP_RULES: self.conn.describe_security_group_rules,
                const.ACTION_ADD_SECURITY_GROUP_RULES: self.conn.add_security_group_rules,
                const.ACTION_DELETE_SECURITY_GROUP_RULES: self.conn.delete_security_group_rules,
                const.ACTION_MODIFY_SECURITY_GROUP_RULE_ATTRIBUTES: self.conn.modify_security_group_rule_attributes,

                # vxnet
                const.ACTION_DESCRIBE_VXNETS: self.conn.describe_vxnets,
                const.ACTION_CREATE_VXNETS: self.conn.create_vxnets,
                const.ACTION_DELETE_VXNETS: self.conn.delete_vxnets,
                const.ACTION_MODIFY_VXNET_ATTRIBUTES: self.conn.modify_vxnet_attributes,
                const.ACTION_JOIN_VXNET: self.conn.join_vxnet,
                const.ACTION_LEAVE_VXNET: self.conn.leave_vxnet,
                const.ACTION_DESCRIBE_VXNET_INSTANCES: self.conn.describe_vxnet_instances,

                # router
                const.ACTION_CREATE_ROUTERS: self.conn.create_routers,
                const.ACTION_UPDATE_ROUTERS: self.conn.update_routers,
                const.ACTION_DELETE_ROUTERS: self.conn.delete_routers,
                const.ACTION_DESCRIBE_ROUTERS: self.conn.describe_routers,
                const.ACTION_POWEROFF_ROUTERS: self.conn.poweroff_routers,
                const.ACTION_POWERON_ROUTERS: self.conn.poweron_routers,
                const.ACTION_JOIN_ROUTER: self.conn.join_router,
                const.ACTION_LEAVE_ROUTER: self.conn.leave_router,
                const.ACTION_DESCRIBE_ROUTER_VXNETS: self.conn.describe_router_vxnets,
                const.ACTION_MODIFY_ROUTER_ATTRIBUTES: self.conn.modify_router_attributes,
                const.ACTION_MODIFY_ROUTER_STATIC_ATTRIBUTES: self.conn.modify_router_static_attributes,
                const.ACTION_DESCRIBE_ROUTER_STATICS: self.conn.describe_router_statics,
                const.ACTION_ADD_ROUTER_STATICS: self.conn.add_router_statics,
                const.ACTION_DELETE_ROUTER_STATICS: self.conn.delete_router_statics,

                # eips
                const.ACTION_DESCRIBE_EIPS: self.conn.describe_eips,
                const.ACTION_ASSOCIATE_EIP: self.conn.associate_eip,
                const.ACTION_DISSOCIATE_EIPS: self.conn.dissociate_eips,
                const.ACTION_ALLOCATE_EIPS: self.conn.allocate_eips,
                const.ACTION_RELEASE_EIPS: self.conn.release_eips,
                const.ACTION_MODIFY_EIP_ATTRIBUTES: self.conn.modify_eip_attributes,
                const.ACTION_CHANGE_EIPS_BANDWIDTH: self.conn.change_eips_bandwidth,
                const.ACTION_CHANGE_EIPS_BILLING_MODE: self.conn.change_eips_billing_mode,

                # dns alias
                const.ACTION_DESCRIBE_DNS_ALIASES: self.conn.describe_dns_aliases,
                const.ACTION_ASSOCIATE_DNS_ALIAS: self.conn.associate_dns_alias,
                const.ACTION_DISSOCIATE_DNS_ALIASES: self.conn.dissociate_dns_aliases,
                const.ACTION_GET_DNS_LABEL: self.conn.get_dns_label,

                # lb
                const.ACTION_DESCRIBE_LOADBALANCERS: self.conn.describe_loadbalancers,
                const.ACTION_CREATE_LOADBALANCER: self.conn.create_loadbalancer,
                const.ACTION_DELETE_LOADBALANCERS: self.conn.delete_loadbalancers,
                const.ACTION_ASSOCIATE_EIPS_TO_LOADBALANCER: self.conn.associate_eips_to_loadbalancer,
                const.ACTION_DISSOCIATE_EIPS_FROM_LOADBALANCER: self.conn.dissociate_eips_from_loadbalancer,
                const.ACTION_UPDATE_LOADBALANCERS: self.conn.update_loadbalancers,
                const.ACTION_STOP_LOADBALANCERS: self.conn.stop_loadbalancers,
                const.ACTION_START_LOADBALANCERS: self.conn.start_loadbalancers,
                const.ACTION_MODIFY_LOADBALANCER_ATTRIBUTES: self.conn.modify_loadbalancer_attributes,
                const.ACTION_DESCRIBE_LOADBALANCER_LISTENERS: self.conn.describe_loadbalancer_listeners,
                const.ACTION_ADD_LOADBALANCER_LISTENERS: self.conn.add_listeners_to_loadbalancer,
                const.ACTION_DELETE_LOADBALANCER_LISTENERS: self.conn.delete_loadbalancer_listeners,
                const.ACTION_MODIFY_LOADBALANCER_LISTENER_ATTRIBUTES: self.conn.modify_loadbalancer_listener_attributes,
                const.ACTION_ADD_LOADBALANCER_BACKENDS: self.conn.add_backends_to_listener,
                const.ACTION_DELETE_LOADBALANCER_BACKENDS: self.conn.delete_loadbalancer_backends,
                const.ACTION_MODIFY_LOADBALANCER_BACKEND_ATTRIBUTES: self.conn.modify_loadbalancer_backend_attributes,
                const.ACTION_DESCRIBE_LOADBALANCER_BACKENDS: self.conn.describe_loadbalancer_backends,

                # monitor
                const.ACTION_GET_MONITOR: self.conn.get_monitoring_data,
                const.ACTION_GET_LOADBALANCER_MONITOR: self.conn.get_loadbalancer_monitoring_data,

                # snapshot
                const.ACTION_DESCRIBE_SNAPSHOTS: self.conn.describe_snapshots,
                const.ACTION_CREATE_SNAPSHOTS: self.conn.create_snapshots,
                const.ACTION_DELETE_SNAPSHOTS: self.conn.delete_snapshots,
                const.ACTION_APPLY_SNAPSHOTS: self.conn.apply_snapshots,
                const.ACTION_MODIFY_SNAPSHOT_ATTRIBUTES: self.conn.modify_snapshot_attributes,
                const.ACTION_CAPTURE_INSTANCE_FROM_SNAPSHOT: self.conn.capture_instance_from_snapshot,
                const.ACTION_CREATE_VOLUME_FROM_SNAPSHOT: self.conn.create_volume_from_snapshot,

                # tags
                const.ACTION_DESCRIBE_TAGS: self.conn.describe_tags,
                const.ACTION_ATTACH_TAGS: self.conn.attach_tags,
                const.ACTION_DETACH_TAGS: self.conn.detach_tags,
                const.ACTION_CREATE_TAG: self.conn.create_tag,
                const.ACTION_DELETE_TAGS: self.conn.delete_tags,
                const.ACTION_MODIFY_TAG_ATTRIBUTES: self.conn.modify_tag_attributes,
        }

        if not isinstance(directive, dict):
            directive = {}

        if action not in handler_map:
            print("can not handle this action: [%s]" % action)

        try:
            return handler_map[action](**directive)
        except Exception as e:
            print(e)
