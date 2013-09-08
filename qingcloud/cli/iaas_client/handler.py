'''
Created on 2012-6-25

@author: yunify
'''
from constants import ACTION_DESCRIBE_IMAGES, ACTION_DESCRIBE_INSTANCES, \
                      ACTION_RUN_INSTANCES, ACTION_STOP_INSTANCES, \
                      ACTION_TERMINATE_INSTANCES, ACTION_START_INSTANCES, \
                      ACTION_CREATE_VOLUMES, ACTION_DELETE_VOLUMES, \
                      ACTION_ATTACH_VOLUMES, ACTION_DETACH_VOLUMES, \
                      ACTION_DESCRIBE_VOLUMES, ACTION_CAPTURE_INSTANCE, \
                      ACTION_DELETE_IMAGES, ACTION_DESCRIBE_KEY_PAIRS, ACTION_MODIFY_IMAGE_ATTRIBUTES, \
                      ACTION_MODIFY_INSTANCE_ATTRIBUTES, ACTION_MODIFY_VOLUME_ATTRIBUTES, \
                      ACTION_DESCRIBE_EIPS, ACTION_ATTACH_KEY_PAIRS, ACTION_DETACH_KEY_PAIRS, \
                      ACTION_CREATE_KEY_PAIR, ACTION_DELETE_KEY_PAIRS, \
                      ACTION_DESCRIBE_SECURITY_GROUPS, ACTION_CREATE_SECURITY_GROUP, \
                      ACTION_MODIFY_SECURITY_GROUP_ATTRIBUTES, ACTION_APPLY_SECURITY_GROUP, \
                      ACTION_DELETE_SECURITY_GROUPS, \
                      ACTION_DESCRIBE_VXNETS, ACTION_CREATE_VXNETS, ACTION_DELETE_VXNETS, \
                      ACTION_MODIFY_KEYPAIR_ATTRIBUTES, ACTION_MODIFY_VXNET_ATTRIBUTES, \
                      ACTION_RESTART_INSTANCES, ACTION_JOIN_VXNET, ACTION_LEAVE_VXNET, ACTION_ASSOCIATE_EIP, \
                      ACTION_DISSOCIATE_EIPS, ACTION_ALLOCATE_EIPS, ACTION_RELEASE_EIPS, \
                      ACTION_MODIFY_EIP_ATTRIBUTES, ACTION_RESIZE_INSTANCES, ACTION_RESIZE_VOLUMES, \
                      ACTION_CHANGE_EIPS_BANDWIDTH, ACTION_DESCRIBE_SECURITY_GROUP_RULES, ACTION_ADD_SECURITY_GROUP_RULES, \
                      ACTION_DELETE_SECURITY_GROUP_RULES, ACTION_MODIFY_SECURITY_GROUP_RULE_ATTRIBUTES, \
                      ACTION_RESET_INSTANCES, ACTION_CREATE_ROUTERS, ACTION_UPDATE_ROUTERS, ACTION_DELETE_ROUTERS, \
                      ACTION_DESCRIBE_ROUTERS, ACTION_MODIFY_ROUTER_ATTRIBUTES, ACTION_DESCRIBE_ROUTER_STATICS, \
                      ACTION_ADD_ROUTER_STATICS, ACTION_DELETE_ROUTER_STATICS, ACTION_DESCRIBE_VXNET_INSTANCES, \
                      ACTION_JOIN_ROUTER, ACTION_LEAVE_ROUTER, ACTION_DESCRIBE_ROUTER_VXNETS, \
                      ACTION_POWEROFF_ROUTERS, ACTION_POWERON_ROUTERS

class IaasHandler(object):
    ''' handle request and send requests to pitrix service '''
    
    def __init__(self, connection = None):
        self.conn = connection
        pass
    
    def _check_integer(self, value):
        ''' check if value is integer '''
        try:
            _ = int(value)
        except:
            return False
        return True
    
    def _check_integer_params(self, directive, params):
        ''' 
            @param directive: the directive to check
            @param params: the params that should be integer type.
        '''
        for param in params:
            if param not in directive:
                continue
            val = directive[param]
            if self._check_integer(val):
                directive[param] = int(val)
            else:
                print("parameter [%s] should be integer in directive [%s]" % (param, directive))
                return False
        return True   
    
    def _check_list_params(self, directive, params):
        ''' 
            @param directive: the directive to check
            @param params: the params that should be list type.
        '''
        for param in params:
            if param not in directive:
                continue
            if not isinstance(directive[param], list):
                print("parameter [%s] should be list in directive [%s]" % (param, directive))
                return False
        return True    
    
    def _check_required_params(self, directive, params):
        ''' 
            @param directive: the directive to check
            @param params: the params that should be list type.
        '''
        for param in params:
            if param not in directive:
                print("[%s] should be specified in directive [%s]" % (param, directive))
                return False
        return True  
    
    def _check_params(self, directive, required_params=[], integer_params=[], list_params=[]):
        ''' check the param type for directive 
        '''
        return self._check_required_params(directive, required_params) and \
            self._check_integer_params(directive, integer_params) and \
            self._check_list_params(directive, list_params) 
            
    def _trim_directive(self, directive):
        ''' trim directive '''
        param_to_trim = []
        for param in directive:
            if directive[param] is not None:
                continue
            param_to_trim.append(param)
            
        for param in param_to_trim:
            del directive[param]
    
    def describe_images(self, directive):
        ''' Action:DescribeImages     
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["offset", "limit", "verbose"], 
                                  list_params = ["images"]):
            return None
            
        return self.conn.describe_images(**directive)
    
    def capture_instance(self, directive):
        ''' Action:CaptureInstance  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["instance"], 
                                  integer_params = [], 
                                  list_params = []):
            return None 
            
        return self.conn.capture_instance(**directive) 

    def delete_images(self, directive):
        ''' Action:DeleteImages  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["images"], 
                                  integer_params = [], 
                                  list_params = ["images"]):
            return None 
            
        return self.conn.delete_images(**directive) 
    
    def modify_image_attributes(self, directive):
        '''  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["image"], 
                                  integer_params = [], 
                                  list_params = []):
            return None
            
        return self.conn.modify_image_attributes(**directive)
    
    def describe_instances(self, directive):
        ''' Action:DescribeInstances  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["offset", "limit", "verbose"], 
                                  list_params = ["instances"]):
            return None   
            
        return self.conn.describe_instances(**directive)  
    
    def run_instances(self, directive):
        ''' Action:RunInstance        
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["image_id"], 
                                  integer_params = ["count", "cpu", "memory"], 
                                  list_params = []):
            return None
        
        return self.conn.run_instances(**directive)
    
    def terminate_instances(self, directive):
        ''' Action:TerminateInstance        
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["instances"], 
                                  integer_params = [], 
                                  list_params = ["instances"]):
            return None
        
        return self.conn.terminate_instances(**directive)

    def stop_instances(self, directive):
        ''' Action:StopInstances      
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["instances"], 
                                  integer_params = ["force"], 
                                  list_params = ["instances"]):
            return None
        
        return self.conn.stop_instances(**directive)
    
    def restart_instances(self, directive):
        ''' Action:RestartInstances      
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["instances"], 
                                  integer_params = [], 
                                  list_params = ["instances"]):
            return None
        
        return self.conn.restart_instances(**directive)    
    
    def start_instances(self, directive):
        ''' Action:StartInstances
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["instances"], 
                                  integer_params = [], 
                                  list_params = ["instances"]):
            return None
        
        return self.conn.start_instances(**directive)   
    
    def reset_instances(self, directive):
        ''' Action:ResetInstances
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["instances"], 
                                  integer_params = [], 
                                  list_params = ["instances"]):
            return None
        
        return self.conn.reset_instances(**directive)
    
    def modify_instance_attributes(self, directive):
        '''  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["instance"], 
                                  integer_params = [], 
                                  list_params = []):
            return None 
            
        return self.conn.modify_instance_attributes(**directive) 
    
    def resize_instances(self, directive):
        '''  
            @param directive : the dictionary of params
        '''            
        if not self._check_params(directive, 
                                  required_params = ["instances"], 
                                  integer_params = ["cpu", "memory"], 
                                  list_params = ["instances"]):
            return None 
            
        return self.conn.resize_instances(**directive)
    
    def describe_volumes(self, directive):
        ''' Action:DescribeVolumes  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["offset", "limit", "verbose"], 
                                  list_params = ["volumes"]):
            return None
            
        return self.conn.describe_volumes(**directive)
    
    def create_volumes(self, directive):
        ''' Action:CreateVolumes      
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["size"], 
                                  integer_params = ["size", "count"], 
                                  list_params = []):
            return None 
        
        return self.conn.create_volumes(**directive)

    def delete_volumes(self, directive):
        ''' Action:DeleteVolumes      
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["volumes"], 
                                  integer_params = [], 
                                  list_params = ["volumes"]):
            return None
        
        return self.conn.delete_volumes(**directive)
    
    def attach_volumes(self, directive):
        ''' Action:AttachVolumes    
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["volumes", "instance"], 
                                  integer_params = [], 
                                  list_params = ["volumes"]):
            return None
        
        return self.conn.attach_volumes(**directive)
    
    def detach_volumes(self, directive):
        ''' Action:DetachVolumes      
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["volumes", "instance"], 
                                  integer_params = [], 
                                  list_params = ["volumes"]):
            return None
        
        return self.conn.detach_volumes(**directive)
    
    def modify_volume_attributes(self, directive):
        '''  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["volume"], 
                                  integer_params = [], 
                                  list_params = []):
            return None 
            
        return self.conn.modify_volume_attributes(**directive)
    
    def resize_volumes(self, directive):
        '''  
            @param directive : the dictionary of params
        '''            
        if not self._check_params(directive, 
                                  required_params = ["volumes", "size"], 
                                  integer_params = ["size"], 
                                  list_params = ["volumes"]):
            return None 
            
        return self.conn.resize_volumes(**directive) 

    def describe_key_pairs(self, directive):
        ''' Action:describe_key_pairs      
            @param directive : the dictionary of params
            @param check : if true, do not handle the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''       
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["offset", "limit", "verbose"], 
                                  list_params = ["keypairs"]):
            return None 
        
        return self.conn.describe_key_pairs(**directive) 
    
    def attach_keypairs(self, directive):
        '''  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["keypairs", "instances"], 
                                  integer_params = [], 
                                  list_params = ["keypairs", "instances"]):
            return None 
            
        return self.conn.attach_keypairs(**directive) 
    
    def detach_keypairs(self, directive):
        '''  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["keypairs", "instances"], 
                                  integer_params = [], 
                                  list_params = ["keypairs", "instances"]):
            return None 
            
        return self.conn.detach_keypairs(**directive) 
    
    def create_keypair(self, directive):
        '''  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["keypair_name"], 
                                  integer_params = [], 
                                  list_params = []):
            return None 
            
        return self.conn.create_keypair(**directive) 

    def delete_keypairs(self, directive):
        '''  
            @param directive : the dictionary of params
            @param check : if true, do not send the request, just check the validity of request
                           return true if request is valid, otherwise return false
        '''
        if not self._check_params(directive, 
                                  required_params = ["keypairs"], 
                                  integer_params = [], 
                                  list_params = ["keypairs"]):
            return None 
            
        return self.conn.delete_keypairs(**directive) 
    
    def modify_keypair_attributes(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["keypair"], 
                                  integer_params = [], 
                                  list_params = []):
            return None 
            
        return self.conn.modify_keypair_attributes(**directive)
    
    def describe_security_groups(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["offset", "limit", "verbose"], 
                                  list_params = ["security_groups"]):
            return None 
            
        return self.conn.describe_security_groups(**directive) 
    
    def create_security_group(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["security_group_name"], 
                                  integer_params = [], 
                                  list_params = []):
            return None 
            
        return self.conn.create_security_group(**directive) 
    
    def modify_security_group_attributes(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["security_group"], 
                                  integer_params = [], 
                                  list_params = ["rules"]):
            return None
        
        if "rules" in directive:
            for rule in directive["rules"]:
                if not isinstance(rule, dict):
                    print("illeagl parameter format [rule] in directive [%s]" % (directive))
                    return None
                if not self._check_params(rule, 
                                          required_params = ["priority", "protocol"], 
                                          integer_params = ["priority"], 
                                          list_params = []):
                    return None 
            
        return self.conn.modify_security_group_attributes(**directive) 
    
    def apply_security_group(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["security_group"], 
                                  integer_params = [], 
                                  list_params = ["instances"]):
            return None 
            
        return self.conn.apply_security_group(**directive) 
    
    def delete_security_groups(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["security_groups"], 
                                  integer_params = [], 
                                  list_params = ["security_groups"]):
            return None 
            
        return self.conn.delete_security_groups(**directive)
    
    def describe_security_group_rules(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = [],
                                  integer_params = ["offset", "limit"], 
                                  list_params = []):
            return None 
            
        return self.conn.describe_security_group_rules(**directive) 
    
    def add_security_group_rules(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["security_group", "rules"], 
                                  integer_params = [], 
                                  list_params = ["rules"]):
            return None 
            
        return self.conn.add_security_group_rules(**directive)  
    
    def delete_security_group_rules(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["security_group_rules"], 
                                  integer_params = [], 
                                  list_params = ["security_group_rules"]):
            return None 
            
        return self.conn.delete_security_group_rules(**directive) 
    
    def modify_security_group_rule_attributes(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["security_group_rule", "priority"],
                                  integer_params = ["priority"], 
                                  list_params = []):
            return None
        
        return self.conn.modify_security_group_rule_attributes(**directive) 
    
    def describe_vxnets(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["limit", "offset", "verbose"], 
                                  list_params = ["vxnets"]):
            return None 
            
        return self.conn.describe_vxnets(**directive) 
    
    def create_vxnets(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["vxnet_name"], 
                                  integer_params = ["vxnet_type", "count"], 
                                  list_params = []):
            return None 
            
        return self.conn.create_vxnets(**directive)

    def join_vxnet(self, directive):
        ''' Action:JoinVxnet
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["vxnet", "instances"], 
                                  integer_params = [], 
                                  list_params = []):
            return None
        
        return self.conn.join_vxnet(**directive)
    
    def leave_vxnet(self, directive):
        ''' Action:LeaveVxnet      
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["vxnet", "instances"], 
                                  integer_params = [], 
                                  list_params = []):
            return None
        
        return self.conn.leave_vxnet(**directive)
    
    def delete_vxnets(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["vxnets"], 
                                  integer_params = [], 
                                  list_params = ["vxnets"]):
            return None 
            
        return self.conn.delete_vxnets(**directive)
    
    def modify_vxnet_attributes(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["vxnet"], 
                                  integer_params = [], 
                                  list_params = []):
            return None 
            
        return self.conn.modify_vxnet_attributes(**directive)
    
    def describe_vxnet_instances(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["vxnet"],
                                  integer_params = ["limit", "offset", "verbose"], 
                                  list_params = ["instances"]):
            return None 
            
        return self.conn.describe_vxnet_instances(**directive)
    
    def describe_routers(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["limit", "offset", "verbose"], 
                                  list_params = []):
            return None 
            
        return self.conn.describe_routers(**directive) 
    
    def create_routers(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["count"], 
                                  list_params = []):
            return None
            
        return self.conn.create_routers(**directive)  
    
    def delete_routers(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["routers"],
                                  integer_params = [], 
                                  list_params = ["routers"]):
            return None
            
        return self.conn.delete_routers(**directive)   
    
    def update_routers(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["routers"],
                                  integer_params = [], 
                                  list_params = ["routers"]):
            return None
            
        return self.conn.update_routers(**directive)     
    
    def poweroff_routers(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["routers"],
                                  integer_params = [], 
                                  list_params = ["routers"]):
            return None
            
        return self.conn.poweroff_routers(**directive)       
    
    def poweron_routers(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["routers"],
                                  integer_params = [], 
                                  list_params = ["routers"]):
            return None
            
        return self.conn.poweron_routers(**directive)
    
    def join_router(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["vxnet", "router", "ip_network"], 
                                  integer_params = ["features"], 
                                  list_params = []):
            return None 
            
        return self.conn.join_router(**directive)  
    
    def leave_router(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["vxnets", "router"], 
                                  integer_params = [], 
                                  list_params = ["vxnets"]):
            return None
            
        return self.conn.leave_router(**directive)  
    
    def describe_router_vxnets(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["limit", "offset"], 
                                  list_params = []):
            return None
            
        return self.conn.describe_router_vxnets(**directive) 
    
    def modify_router_attributes(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["router"], 
                                  integer_params = ["features"], 
                                  list_params = []):
            return None
            
        return self.conn.modify_router_attributes(**directive)  
    
    def describe_router_statics(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["limit", "offset", "verbose", "static_type"], 
                                  list_params = []):
            return None 
            
        return self.conn.describe_router_statics(**directive) 
    
    def add_router_statics(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["statics", "router"], 
                                  integer_params = [], 
                                  list_params = ["statics"]):
            return None
            
        return self.conn.add_router_statics(**directive)  
    
    def delete_router_statics(self, directive):
        '''  
            @param directive : the dictionary of params
        '''
        if not self._check_params(directive, 
                                  required_params = ["router_statics"], 
                                  integer_params = [], 
                                  list_params = ["router_statics"]):
            return None 
            
        return self.conn.delete_router_statics(**directive)
    
    def describe_eips(self, directive):
        '''  
            @param directive : the dictionary of params
        '''            
        if not self._check_params(directive, 
                                  required_params = [], 
                                  integer_params = ["offset", "limit"], 
                                  list_params = ["eips"]):
            return None 
            
        return self.conn.describe_eips(**directive) 
    
    def associate_eip(self, directive):
        '''  
            @param directive : the dictionary of params
        '''            
        if not self._check_params(directive, 
                                  required_params = ["eip", "instance"], 
                                  integer_params = [], 
                                  list_params = []):
            return None 
            
        return self.conn.associate_eip(**directive) 
    
    def dissociate_eips(self, directive):
        '''  
            @param directive : the dictionary of params
        '''            
        if not self._check_params(directive, 
                                  required_params = ["eips"], 
                                  integer_params = [], 
                                  list_params = ["eips"]):
            return None 
            
        return self.conn.dissociate_eips(**directive) 
    
    def allocate_eips(self, directive):
        '''  
            @param directive : the dictionary of params
        '''            
        if not self._check_params(directive, 
                                  required_params = ["bandwidth"], 
                                  integer_params = ["bandwidth", "count", "need_icp"], 
                                  list_params = []):
            return None
            
        return self.conn.allocate_eips(**directive) 
    
    def release_eips(self, directive):
        '''  
            @param directive : the dictionary of params
        '''            
        if not self._check_params(directive, 
                                  required_params = ["eips"], 
                                  integer_params = ["force"], 
                                  list_params = ["eips"]):
            return None 
            
        return self.conn.release_eips(**directive)  
    
    def change_eips_bandwidth(self, directive):
        '''  
            @param directive : the dictionary of params
        '''            
        if not self._check_params(directive, 
                                  required_params = ["eips", "bandwidth"], 
                                  integer_params = ["bandwidth"], 
                                  list_params = ["eips"]):
            return None  
            
        return self.conn.change_eips_bandwidth(**directive) 
    
    def modify_eip_attributes(self, directive):
        '''  
            @param directive : the dictionary of params
        '''            
        if not self._check_params(directive, 
                                  required_params = ["eip"], 
                                  integer_params = ["need_icp"], 
                                  list_params = []):
            return None 
            
        return self.conn.modify_eip_attributes(**directive)

    def handle(self, action, directive):
        ''' dispatch request to specified handler according to action.
        '''
        
        handler_map = {# images
                       ACTION_DESCRIBE_IMAGES : self.describe_images,
                       ACTION_DELETE_IMAGES : self.delete_images,
                       ACTION_CAPTURE_INSTANCE : self.capture_instance,
                       ACTION_MODIFY_IMAGE_ATTRIBUTES : self.modify_image_attributes,
                       # instances
                       ACTION_DESCRIBE_INSTANCES : self.describe_instances,
                       ACTION_RUN_INSTANCES : self.run_instances,
                       ACTION_START_INSTANCES : self.start_instances,
                       ACTION_STOP_INSTANCES : self.stop_instances,
                       ACTION_RESTART_INSTANCES : self.restart_instances,
                       ACTION_TERMINATE_INSTANCES : self.terminate_instances,
                       ACTION_RESIZE_INSTANCES : self.resize_instances, 
                       ACTION_RESET_INSTANCES : self.reset_instances,
                       ACTION_MODIFY_INSTANCE_ATTRIBUTES : self.modify_instance_attributes,
                       # volumes
                       ACTION_DESCRIBE_VOLUMES : self.describe_volumes,
                       ACTION_CREATE_VOLUMES  : self.create_volumes,
                       ACTION_DELETE_VOLUMES : self.delete_volumes,
                       ACTION_ATTACH_VOLUMES : self.attach_volumes,
                       ACTION_DETACH_VOLUMES : self.detach_volumes,
                       ACTION_MODIFY_VOLUME_ATTRIBUTES : self.modify_volume_attributes,
                       ACTION_RESIZE_VOLUMES : self.resize_volumes,
                       # key pair
                       ACTION_DESCRIBE_KEY_PAIRS : self.describe_key_pairs,
                       ACTION_ATTACH_KEY_PAIRS : self.attach_keypairs,
                       ACTION_DETACH_KEY_PAIRS : self.detach_keypairs,
                       ACTION_CREATE_KEY_PAIR :self.create_keypair,
                       ACTION_DELETE_KEY_PAIRS : self.delete_keypairs,
                       ACTION_MODIFY_KEYPAIR_ATTRIBUTES : self.modify_keypair_attributes,
                       # security groups
                       ACTION_DESCRIBE_SECURITY_GROUPS: self.describe_security_groups,
                       ACTION_CREATE_SECURITY_GROUP : self.create_security_group,
                       ACTION_MODIFY_SECURITY_GROUP_ATTRIBUTES : self.modify_security_group_attributes,
                       ACTION_APPLY_SECURITY_GROUP : self.apply_security_group,
                       ACTION_DELETE_SECURITY_GROUPS : self.delete_security_groups,
                       ACTION_DESCRIBE_SECURITY_GROUP_RULES : self.describe_security_group_rules, 
                       ACTION_ADD_SECURITY_GROUP_RULES : self.add_security_group_rules,
                       ACTION_DELETE_SECURITY_GROUP_RULES : self.delete_security_group_rules, 
                       ACTION_MODIFY_SECURITY_GROUP_RULE_ATTRIBUTES : self.modify_security_group_rule_attributes,
                       # vxnet
                       ACTION_DESCRIBE_VXNETS : self.describe_vxnets,
                       ACTION_CREATE_VXNETS : self.create_vxnets,
                       ACTION_DELETE_VXNETS : self.delete_vxnets,
                       ACTION_MODIFY_VXNET_ATTRIBUTES : self.modify_vxnet_attributes,
                       ACTION_JOIN_VXNET : self.join_vxnet,
                       ACTION_LEAVE_VXNET : self.leave_vxnet,
                       ACTION_DESCRIBE_VXNET_INSTANCES : self.describe_vxnet_instances,
                       # router
                       ACTION_CREATE_ROUTERS : self.create_routers, 
                       ACTION_UPDATE_ROUTERS : self.update_routers, 
                       ACTION_DELETE_ROUTERS : self.delete_routers,
                       ACTION_DESCRIBE_ROUTERS : self.describe_routers, 
                       ACTION_POWEROFF_ROUTERS : self.poweroff_routers, 
                       ACTION_POWERON_ROUTERS : self.poweron_routers, 
                       ACTION_JOIN_ROUTER : self.join_router, 
                       ACTION_LEAVE_ROUTER: self.leave_router, 
                       ACTION_DESCRIBE_ROUTER_VXNETS: self.describe_router_vxnets,
                       ACTION_MODIFY_ROUTER_ATTRIBUTES : self.modify_router_attributes, 
                       ACTION_DESCRIBE_ROUTER_STATICS : self.describe_router_statics,
                       ACTION_ADD_ROUTER_STATICS : self.add_router_statics, 
                       ACTION_DELETE_ROUTER_STATICS : self.delete_router_statics, 
                       # eips
                       ACTION_DESCRIBE_EIPS : self.describe_eips,
                       ACTION_ASSOCIATE_EIP : self.associate_eip, 
                       ACTION_DISSOCIATE_EIPS : self.dissociate_eips, 
                       ACTION_ALLOCATE_EIPS : self.allocate_eips, 
                       ACTION_RELEASE_EIPS : self.release_eips,
                       ACTION_MODIFY_EIP_ATTRIBUTES : self.modify_eip_attributes,
                       ACTION_CHANGE_EIPS_BANDWIDTH : self.change_eips_bandwidth,
                       }

        if directive is None or not isinstance(directive, dict):
            directive = {}

        if action is not None and action in handler_map:
            return handler_map[action](directive)
        else:
            print "can not handler this action: [%s]" % action
    
