# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, print_function, unicode_literals
from json import dumps as to_json
from logging import getLogger
log = getLogger('gs.group.member.leave.json.hook')
from zope.component import createObject
from zope.formlib import form
from gs.content.form.api.json import SiteEndpoint
from gs.auth.token import log_auth_error
from gs.group.member.base import user_member_of_group
from gs.group.member.leave.base import leave_group
from .interfaces import ILeaveGroup


class LeaveGroupHook(SiteEndpoint):
    '''The page removes someone from a group'''
    label = 'Remove someone from the group'
    form_fields = form.Fields(ILeaveGroup, render_context=False)
    SUCCESS = 0
    NO_GROUP = 1
    NO_USER = 2
    NOT_MEMBER = 4

    @form.action(label='Leave', name='leave', prefix='',
                 failure='handle_leave_failure')
    def handle_get_groups(self, action, data):
        '''The form action for the *Leave group* page.

:param action: The button that was clicked.
:param dict data: The form data.'''
        r = {'groupId': data['groupId'],
             'userId': data['userId'], }
        groupInfo = createObject('groupserver.GroupInfo', self.context, data['groupId'])
        userInfo = createObject('groupserver.UserFromId', self.context, data['userId'])
        if groupInfo.groupObj is None:
            r['status'] = self.NO_GROUP
            r['message'] = 'No such group "{0}"'.format(data['groupId'])
        elif userInfo.anonymous:
            r['status'] = self.NO_USER
            r['message'] = 'No such user "{0}"'.format(data['userId'])
        elif user_member_of_group(userInfo, groupInfo):
            leave_group(groupInfo, userInfo, self.request)
            r['status'] = self.SUCCESS
            r['message'] = '{0} has left {1}'.format(userInfo.name, groupInfo.name)
        else:
            r['status'] = self.NOT_MEMBER
            r['message'] = '{0} is not a member {1}'.format(userInfo.name, groupInfo.name)

        retval = to_json(r)
        return retval

    def handle_leave_failure(self, action, data, errors):
        log_auth_error(self.context, self.request, errors)
        retval = self.build_error_response(action, data, errors)
        return retval
