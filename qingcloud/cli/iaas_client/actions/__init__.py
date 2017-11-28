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
from qingcloud.cli.iaas_client.actions import nic
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
from qingcloud.cli.iaas_client.actions import notification
from qingcloud.cli.iaas_client.actions import s2
from qingcloud.cli.iaas_client.actions import alarm_policy
from qingcloud.cli.iaas_client.actions import billing

class ActionManager(object):

    @classmethod
    def get_action(cls, action):
        return cls.action_table.get(action)

    @classmethod
    def get_valid_actions(cls):
        return sorted(ActionManager.action_table.keys())

    action_table = {
            ## notification ##
            'describe-notification-center-user-posts': notification.DescribeNotificationCenterUserPostsAction,

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

            ## nic ##
            'create-nics': nic.CreateNicsAction,
            'modify-nic-attributes': nic.ModifyNicAttributesAction,
            'describe-nics': nic.DescribeNicsAction,
            'attach-nics': nic.AttachNicsAction,
            'detach-nics': nic.DetachNicsAction,
            'delete-nics': nic.DeleteNicsAction,

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
            'describe-security-group-ipsets': sg.DescribeSecurityGroupIPSetsAction,
            'modify-security-group-ipset-attributes': sg.ModifySecurityGroupIPSetAttributesAction,
            'create-security-group-ipset': sg.CreateSecurityGroupIPSetAction,
            'delete-security-group-ipsets': sg.DeleteSecurityGroupIPSetsAction,

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
            'add-router-static-entries': router.AddRouterStaticEntriesAction,
            'join-router': router.JoinRouterAction,
            'leave-router': router.LeaveRouterAction,
            'create-routers': router.CreateRoutersAction,
            'modify-router-attributes': router.ModifyRouterAttributesAction,
            'modify-router-static-attributes': router.ModifyRouterStaticAttributesAction,
            'modify-router-static-entry-attributes': router.ModifyRouterStaticEntryAttributesAction,
            'delete-router-statics': router.DeleteRouterStaticsAction,
            'delete-router-static-entries': router.DeleteRouterStaticEntriesAction,
            'delete-routers': router.DeleteRoutersAction,
            'poweroff-routers': router.PowerOffRoutersAction,
            'poweron-routers': router.PowerOnRoutersAction,
            'describe-routers': router.DescribeRoutersAction,
            'describe-router-statics': router.DescribeRouterStaticsAction,
            'describe-router-static-entries': router.DescribeRouterStaticEntriesAction,
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
            'add-loadbalancer-policy-rules': lb.AddLoadBalancerPolicyRulesAction,
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

            ## S2 ##
            'create-s2-server': s2.CreateS2ServerAction,
            'describe-s2-servers': s2.DescribeS2ServersAction,
            'modify-s2-server': s2.ModifyS2ServerAttributesAction,
            'resize-s2-servers': s2.ResizeS2ServersAction,
            'delete-s2-servers': s2.DeleteS2ServersAction,
            'poweron-s2-servers': s2.PowerOnS2ServersAction,
            'poweroff-s2-servers': s2.PowerOffS2ServersAction,
            'update-s2-servers': s2.UpdateS2ServersAction,
            'change-s2-server-vxnet': s2.ChangeS2ServerVxnetAction,
            'create-s2-shared-target': s2.CreateS2SharedTargetAction,
            'describe-s2-shared-targets': s2.DescribeS2SharedTargetsAction,
            'delete-s2-shared-targets': s2.DeleteS2SharedTargetsAction,
            'enable-s2-shared-targets': s2.EnableS2SharedTargetsAction,
            'disable-s2-shared-targets': s2.DisableS2SharedTargetsAction,
            'modify-s2-shared-target-attributes': s2.ModifyS2SharedTargetAttributesAction,
            'attach-to-s2-shared-target': s2.AttachToS2SharedTargetAction,
            'detach-from-s2-shared-target': s2.DetachFromS2SharedTargetAction,
            'describe-s2-default-parameters': s2.DescribeS2DefaultParametersAction,
            'create-s2-group': s2.CreateS2GroupAction,
            'describe-s2-groups': s2.DescribeS2GroupsAction,
            'modify-s2-group': s2.ModifyS2GroupAction,
            'delete-s2-group': s2.DeleteS2GroupsAction,
            'create-s2-account': s2.CreateS2AccountAction,
            'describe-s2-accounts': s2.DescribeS2AccountsAction,
            'modify-s2-account': s2.ModifyS2AccountAction,
            'delete-s2-accounts': s2.DeleteS2AccountsAction,
            'associate-s2-account-group': s2.AssociateS2AccountGroupAction,
            'dissociate-s2-account-group': s2.DissociateS2AccountGroupAction,

            ## alarm policy ##
            'describe-alarm-policies': alarm_policy.DescribeAlarmPoliciesAction,
            'add-alarm-policy-actions': alarm_policy.AddAlarmPolicyActionsAction,
            'add-alarm-policy-rules': alarm_policy.AddAlarmPolicyRulesAction,
            'apply-alarm-policy': alarm_policy.ApplyAlarmPolicyAction,
            'associate-alarm-policy': alarm_policy.AssociateAlarmPolicyAction,
            'create-alarm-policy': alarm_policy.CreateAlarmPolicyAction,
            'delete-alarm-policies': alarm_policy.DeleteAlarmPoliciesAction,
            'delete-alarm-policy-actions': alarm_policy.DeleteAlarmPolicyActionsAction,
            'delete-alarm-policy-rules': alarm_policy.DeleteAlarmPolicyRulesAction,
            'describe-alarm-history': alarm_policy.DescribeAlarmHistoryAction,
            'describe-alarm-policy-actions': alarm_policy.DescribeAlarmPolicyActionsAction,
            'describe-alarm-policy-rules': alarm_policy.DescribeAlarmPolicyRulesAction,
            'describe-alarms': alarm_policy.DescribeAlarmsAction,
            'dissociate-alarm-policy': alarm_policy.DissociateAlarmPolicyAction,
            'modify-alarm-policy-action-attributes': alarm_policy.ModifyAlarmPolicyActionAttributesAction,
            'modify-alarm-policy-attributes': alarm_policy.ModifyAlarmPolicyAttributesAction,
            'modify-alarm-policy-rule-attributes': alarm_policy.ModifyAlarmPolicyRuleAttributesAction,

            ## billing ##
            'get-balance': billing.GetBalanceAction,
            'get-lease-info': billing.GetLeaseInfoAction,
            }
