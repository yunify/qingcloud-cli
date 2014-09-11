# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeJobsAction(BaseAction):

    action = 'DescribeJobs'
    command = 'describe-jobs'
    usage = '%(prog)s [-j "job, ..."] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-j', '--jobs', dest='jobs',
                action='store', type=str, default='',
                help='the comma separated IDs of jobs you want to describe. ')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='the comma separated status of jobs you want to describe. ')

        parser.add_argument('-a', '--job-action', dest='job_action',
                action='store', type=str, default=None,
                help='the action of jobs you want to describe. ')

    @classmethod
    def build_directive(cls, options):
        return {
                'jobs': explode_array(options.jobs),
                'status': explode_array(options.status),
                'job_action': options.job_action,
                'offset':options.offset,
                'limit': options.limit,
                }
