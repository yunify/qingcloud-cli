# coding: utf-8

from qingcloud.cli.iaas_client.actions import instance
from qingcloud.cli.iaas_client.actions import volume
from qingcloud.cli.iaas_client.actions import eip
from qingcloud.cli.iaas_client.actions import image
from qingcloud.cli.iaas_client.actions import keypair
from qingcloud.cli.iaas_client.actions import router
from qingcloud.cli.iaas_client.actions import sg
from qingcloud.cli.iaas_client.actions import vxnet

class ActionManager(object):

    @classmethod
    def get_action(cls, action):
        return cls.action_table().get(action)

    @classmethod
    def action_table(cls):
        return {
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
                }
