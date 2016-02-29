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

from qingcloud.cli.iaas_client.actions import job
from qingcloud.cli.iaas_client.actions import instance
from qingcloud.cli.iaas_client.actions import volume
from qingcloud.cli.iaas_client.actions import eip
from qingcloud.cli.iaas_client.actions import image
from qingcloud.cli.iaas_client.actions import keypair
from qingcloud.cli.iaas_client.actions import router
from qingcloud.cli.iaas_client.actions import sg
from qingcloud.cli.iaas_client.actions import vxnet
from qingcloud.cli.iaas_client.actions import lb
from qingcloud.cli.iaas_client.actions import monitor
from qingcloud.cli.iaas_client.actions import snapshot
from qingcloud.cli.iaas_client.actions import dns_alias
from qingcloud.cli.iaas_client.actions import tag

class ActionManager(object):

    @classmethod
    def get_action(cls, action):
        return cls.action_table.get(action)

    @classmethod
    def get_valid_actions(cls):
        return sorted(ActionManager.action_table.keys())

    action_table = {
            ## job ##
            'describe-jobs': job.DescribeJobsAction,

            ## instance ##
            'run-instances': instance.RunInstancesAction,
            'modify-instance-attributes': instance.ModifyInstanceAttributesAction,
            'reset-instances': instance.ResetInstancesAction,
            'resize-instances': instance.ResizeInstancesAction,
            'describe-instances': instance.DescribeInstancesAction,
            'restart-instances': instance.RestartInstancesAction,
            'start-instances': instance.StartInstancesAction,
            'stop-instances': instance.StopInstancesAction,
            'terminate-instances': instance.TerminateInstancesAction,

            ## volume ##
            'create-volumes': volume.CreateVolumesAction,
            'modify-volume-attributes': volume.ModifyVolumeAttributesAction,
            'describe-volumes': volume.DescribeVolumesAction,
            'attach-volumes': volume.AttachVolumesAction,
            'detach-volumes': volume.DetachVolumesAction,
            'delete-volumes': volume.DeleteVolumesAction,
            'resize-volumes': volume.ResizeVolumesAction,

            ## eip ##
            'describe-eips': eip.DescribeEipsAction,
            'allocate-eips': eip.AllocateEipsAction,
            'release-eips': eip.ReleaseEipsAction,
            'modify-eip-attributes': eip.ModifyEipAttributesAction,
            'associate-eip': eip.AssociateEipAction,
            'dissociate-eips': eip.DissociateEipsAction,
            'change-eips-bandwidth': eip.ChangeEipsBandwidthAction,
            'change-eips-billing-mode': eip.ChangeEipsBillingModeAction,

            ## sg ##
            'create-security-group': sg.CreateSecurityGroupAction,
            'describe-security-groups': sg.DescribeSecurityGroupsAction,
            'modify-security-group-attributes': sg.ModifySecurityGroupAttributesAction,
            'apply-security-group': sg.ApplySecurityGroupAction,
            'delete-security-groups': sg.DeleteSecurityGroupsAction,
            'describe-security-group-rules': sg.DescribeSecurityGroupRulesAction,
            'modify-security-group-rule-attributes': sg.ModifySecurityGroupRuleAttributesAction,
            'add-security-group-rules': sg.AddSecurityGroupRulesAction,
            'delete-security-group-rules': sg.DeleteSecurityGroupRulesAction,

            ## keypair ##
            'create-keypair': keypair.CreateKeyPairAction,
            'describe-keypairs': keypair.DescribeKeyPairsAction,
            'attach-keypairs': keypair.AttachKeyPairsAction,
            'detach-keypairs': keypair.DetachKeyPairsAction,
            'modify-keypair-attributes': keypair.ModifyKeyPairAttributesAction,
            'delete-keypairs': keypair.DeleteKeyPairsAction,

            ## vxnet ##
            'create-vxnets': vxnet.CreateVxnetsAction,
            'describe-vxnet-instances': vxnet.DescribeVxnetInstancesAction,
            'describe-vxnets': vxnet.DescribeVxnetsAction,
            'join-vxnet': vxnet.JoinVxnetAction,
            'leave-vxnet': vxnet.LeaveVxnetAction,
            'modify-vxnet-attributes': vxnet.ModifyVxnetAttributesAction,
            'delete-vxnets': vxnet.DeleteVxnetsAction,

            ## router ##
            'add-router-statics': router.AddRouterStaticsAction,
            'join-router': router.JoinRouterAction,
            'leave-router': router.LeaveRouterAction,
            'create-routers': router.CreateRoutersAction,
            'modify-router-attributes': router.ModifyRouterAttributesAction,
            'modify-router-static-attributes': router.ModifyRouterStaticAttributesAction,
            'delete-router-statics': router.DeleteRouterStaticsAction,
            'delete-routers': router.DeleteRoutersAction,
            'poweroff-routers': router.PowerOffRoutersAction,
            'poweron-routers': router.PowerOnRoutersAction,
            'describe-routers': router.DescribeRoutersAction,
            'describe-router-statics': router.DescribeRouterStaticsAction,
            'describe-router-vxnets': router.DescribeRouterVxnetsAction,
            'update-routers': router.UpdateRoutersAction,

            ## image ##
            'describe-images': image.DescribeImagesAction,
            'modify-image-attributes': image.ModifyImageAttributesAction,
            'capture-instance': image.CaptureInstanceAction,
            'delete-images': image.DeleteImagesAction,

            ## load balancer ##
            'add-loadbalancer-backends': lb.AddLoadBalancerBackendsAction,
            'add-loadbalancer-listeners': lb.AddLoadBalancerListenersAction,
            'associate-eips-to-loadbalancer': lb.AssociateEipsToLoadBalancerAction,
            'create-loadbalancers': lb.CreateLoadBalancerAction,
            'delete-loadbalancer-backends': lb.DeleteLoadBalancerBackendsAction,
            'delete-loadbalancer-listeners': lb.DeleteLoadBalancerListenersAction,
            'delete-loadbalancers': lb.DeleteLoadBalancersAction,
            'describe-loadbalancer-backends': lb.DescribeLoadBalancerBackendsAction,
            'describe-loadbalancer-listeners': lb.DescribeLoadBalancerListenersAction,
            'describe-loadbalancers': lb.DescribeLoadBalancersAction,
            'dissociate-eips-from-loadbalancer': lb.DissociateEipsFromLoadBalancerAction,
            'modify-loadbalancer-attributes': lb.ModifyLoadBalancerAttributesAction,
            'modify-loadbalancer-backend-attributes': lb.ModifyLoadBalancerBackendAttributesAction,
            'modify-loadbalancer-listener-attributes': lb.ModifyLoadBalancerListenerAttributessAction,
            'start-loadbalancers': lb.StartLoadBalancersAction,
            'stop-loadbalancers': lb.StopLoadBalancersAction,
            'update-loadbalancers': lb.UpdateLoadBalancersAction,

            ## monitor ##
            'get-monitoring-data': monitor.GetMonitorAction,
            'get-loadbalancer-monitoring-data': monitor.GetLoadBalancerMonitorAction,

            ## snapshot ##
            'describe-snapshots': snapshot.DescribeSnapshotsAction,
            'create-snapshots': snapshot.CreateSnapshotsAction,
            'delete-snapshots': snapshot.DeleteSnapshotsAction,
            'apply-snapshots': snapshot.ApplySnapshotsAction,
            'modify-snapshot-attributes': snapshot.ModifySnapshotAttributesAction,
            'capture-instance-from-snapshot': snapshot.CaptureInstanceFromSnapshotAction,
            'create-volume-from-snapshot': snapshot.CreateVolumeFromSnapshotAction,

            ## dns alias ##
            'describe-dns-aliases': dns_alias.DescribeDNSAliasesAction,
            'associate-dns-alias': dns_alias.AssociateDNSAliasAction,
            'dissociate-dns-aliases': dns_alias.DissociateDNSAliasesAction,
            'get-dns-label': dns_alias.GetDNSLabelAction,

            ## tag ##
            'create-tag': tag.CreateTagAction,
            'describe-tags': tag.DescribeTagsAction,
            'attach-tags': tag.AttachTagsAction,
            'detach-tags': tag.DetachTagsAction,
            'modify-tag-attributes': tag.ModifyTagAttributesAction,
            'delete-tags': tag.DeleteTagsAction,

            }
